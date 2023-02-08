#pylint: disable=line-too-long
'''Personal Shipping Form to temporarily replace shipping from generation and simplify data entry.'''
import os
from tkinter import Label, Entry, Button, Tk, font, Frame
from PIL import Image, ImageTk
import treepoem as tp
import jinja2
import pdfkit

user_path = os.path.expanduser("~")
win = Tk()
win.title('Mail & Ship - Shipping Form')
win.geometry('1100x650')
win.configure(bg='#F4F3F5')

shipping_frame=Frame(win, bg='#F4F3F5')
shipping_frame.pack(fill='x')

button_frame=Frame(win, bg='#F4F3F5')
button_frame.pack(fill='both')

logo_frame=Frame(win, bg='#F4F3F5')
logo_frame.pack(side='bottom', fill='both')

label_color = '#F4F3F5'

ui_font = font.Font(family='Segoe UI', size='12', weight='normal')
section_font = font.Font(family='Segoe UI', size='16', weight='normal')
button_font = font.Font(family='Segoe UI', size='12', weight='bold')

Label(shipping_frame, bg=label_color, font=section_font, text='Ship From:').grid(row=0, pady=15, padx=5)

Label(shipping_frame, bg=label_color, font=ui_font, text='Alias').grid(row=1, column=1, padx=5, pady=5)
alias = Entry(shipping_frame, font=ui_font)
alias.grid(row=1, column=2, padx=5, pady=10)

Label(shipping_frame, bg=label_color, font=ui_font, text='Name').grid(row=1, column=3, padx=5, pady=5)
ship_from_name = Entry(shipping_frame, font=ui_font)
ship_from_name.grid(row=1, column=4, padx=5, pady=10)

Label(shipping_frame, bg=label_color, font=ui_font, text='Phone').grid(row=1, column=5, padx=5, pady=5)
ship_from_phone = Entry(shipping_frame, font=ui_font)
ship_from_phone.grid(row=1, column=6, padx=5, pady=10)

Label(shipping_frame, bg=label_color, font=section_font, text='Ship To:').grid(row=2, pady=15, padx=5)

Label(shipping_frame, bg=label_color, font=ui_font, text='Company').grid(row=3, column=1, padx=5, pady=10)
company_name = Entry(shipping_frame, font=ui_font)
company_name.grid(row=3,column=2)

Label(shipping_frame, bg=label_color, font=ui_font, text='Contact Name').grid(row=3, column=3, padx=5, pady=10)
contact_name = Entry(shipping_frame, font=ui_font)
contact_name.grid(row=3, column=4)

Label(shipping_frame, bg=label_color, font=ui_font, text='Address Line 1').grid(row=4, column=1, padx=5, pady=10)
address_line1 = Entry(shipping_frame, font=ui_font)
address_line1.grid(row=4, column=2)

Label(shipping_frame, bg=label_color, font=ui_font, text='Address Line 2').grid(row=4, column=3, padx=5, pady=10)
address_line2 = Entry(shipping_frame, font=ui_font)
address_line2.grid(row=4, column=4)

Label(shipping_frame, bg=label_color, font=ui_font, text='Address Line 3').grid(row=5, column=1, padx=5, pady=10)
address_line3 = Entry(shipping_frame, font=ui_font)
address_line3.grid(row=5, column=2)

Label(shipping_frame, bg=label_color, font=ui_font, text='City').grid(row=5, column=3, padx=5, pady=10)
city = Entry(shipping_frame, font=ui_font)
city.grid(row=5, column=4)

Label(shipping_frame, bg=label_color, font=ui_font, text='Country').grid(row=6, column=1, padx=5, pady=10)
country = Entry(shipping_frame, font=ui_font)
country.grid(row=6, column=2)

Label(shipping_frame, bg=label_color, font=ui_font, text='State').grid(row=6, column=3, padx=5, pady=10)
state = Entry(shipping_frame, font=ui_font)
state.grid(row=6, column=4)

Label(shipping_frame, bg=label_color, font=ui_font, text='Zip Code').grid(row=6, column=5, padx=15, pady=10)
zip_code = Entry(shipping_frame, font=ui_font)
zip_code.grid(row=6, column=6)

Label(shipping_frame, bg=label_color, font=ui_font, text='Phone').grid(row=7, column=1, padx=5, pady=10)
phone = Entry(shipping_frame, font=ui_font)
phone.grid(row=7, column=2)

Label(shipping_frame, bg=label_color, font=ui_font, text='Email').grid(row=7, column=3, padx=5, pady=10)
email = Entry(shipping_frame, font=ui_font)
email.grid(row=7, column=4)

t ='\t'

def generate_barcode():
    '''generates barcodes from form entires, triggers generation of HTML --> PDF converstion and prints the resulting PDF.'''

    alias_barcode = tp.generate_barcode('datamatrix', data=alias.get())
    alias_barcode.convert('1').save(user_path+r'\Documents\Barcodes\alias_barcode.png')

    barcode_company_city_concat = company_name.get()+t+contact_name.get()+t+address_line1.get()+t+address_line2.get()+t+address_line3.get()+t+city.get()+t+t+t+zip_code.get()+t+phone.get()+t+email.get()
    company_city_barcode = tp.generate_barcode('datamatrix', data=barcode_company_city_concat)
    company_city_barcode.convert('1').save(user_path+r'\Documents\Barcodes\company_city_barcode.png')

    data_elements = {
        'alias': alias.get(),
        'ship_from_name': ship_from_name.get(),
        'ship_from_phone': ship_from_phone.get(),
        'company_name': company_name.get(),
        'city':city.get(),
        'contact_name': contact_name.get(),
        'address_line1': address_line1.get(),
        'address_line2': address_line2.get(),
        'address_line3': address_line3.get(),
        'country': country.get(),
        'state': state.get(),
        'zip_code': zip_code.get(),
        'phone': phone.get(),
        'email': email.get()
        }

    template_loader = jinja2.FileSystemLoader(user_path+r'\Documents\Barcodes')
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template('pdf_html.html')
    output_text = template.render(data_elements)

    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe")
    pdfkit.from_string(output_text, user_path+r'\Documents\Barcodes\pdf_generated.pdf', configuration=config, options={"enable-local-file-access": ""})

    os.startfile(user_path+r'\Documents\Barcodes\pdf_generated.pdf', "print")

def clear_entries():
    '''clearing fields'''
    alias.delete(0,"end")
    ship_from_name.delete(0,"end")
    ship_from_phone.delete(0,"end")
    company_name.delete(0,"end")
    contact_name.delete(0,"end")
    address_line1.delete(0,"end")
    address_line2.delete(0,"end")
    address_line3.delete(0,"end")
    city.delete(0,"end")
    country.delete(0,"end")
    state.delete(0,"end")
    zip_code.delete(0,"end")
    phone.delete(0,"end")
    email.delete(0,"end")

button = Button(button_frame, bg='#0078D4', fg='white', font=button_font, text='Generate Barcode', command=lambda:[generate_barcode(), clear_entries()])
button.pack(side='top', expand=True, pady=10)

packaged_img=Image.open(user_path+r'\OneDrive - Microsoft\Documents\Barcode_Test\placeholder-logo-1.png').resize((260,123))
packaged_logo = ImageTk.PhotoImage(packaged_img)
Label(logo_frame, bg='#F4F3F5', image=packaged_logo).pack(side='bottom', pady=10, padx=10, anchor='sw', expand=True)

win.mainloop()
