# pylint: disable=line-too-long
'''Personal Shipping Form to temporarily replace shipping from generation and simplify data entry.'''
import os
from tkinter import Label, Entry, Button, Tk, font, Frame
import treepoem as tp
import jinja2
import pdfkit
from PIL import Image, ImageTk


user_path = os.path.expanduser("~")
win = Tk()
win.title('Mail & Ship - Shipping Form')
win.geometry('1100x650')
win.configure(bg='#F4F3F5')

# Frames
shipping_frame = Frame(win, bg='#F4F3F5')
shipping_frame.pack(fill='x')

button_frame = Frame(win, bg='#F4F3F5')
button_frame.pack(fill='both')

logo_frame = Frame(win, bg='#F4F3F5')
logo_frame.pack(side='bottom', fill='both')

# Colors
LABEL_COLOR = '#F4F3F5'

# Fonts
ui_font = font.Font(family='Segoe UI', size='12', weight='normal')
section_font = font.Font(family='Segoe UI', size='16', weight='normal')
button_font = font.Font(family='Segoe UI', size='12', weight='bold')

# Form Fields and Labels
ship_from_label = Label(shipping_frame, bg=LABEL_COLOR, font=section_font, text='Ship From:')
ship_from_label.grid(row=0, pady=15, padx=5)

alias_label = Label(shipping_frame, bg=LABEL_COLOR, font=ui_font, text='Alias')
alias = Entry(shipping_frame, font=ui_font, relief='flat', highlightbackground='grey', highlightthickness=1)
alias_label.grid(row=1, column=1, padx=5, pady=5)
alias.grid(row=1, column=2, padx=5, pady=10)

ship_from_label = Label(shipping_frame, bg=LABEL_COLOR, font=ui_font, text='Name')
ship_from_name = Entry(shipping_frame, font=ui_font, relief='flat', highlightbackground='grey', highlightthickness=1)
ship_from_label.grid(row=1, column=3, padx=5, pady=5)
ship_from_name.grid(row=1, column=4, padx=5, pady=10)

ship_from_phone_label = Label(shipping_frame, bg=LABEL_COLOR, font=ui_font,text='Phone')
ship_from_phone = Entry(shipping_frame, font=ui_font, relief='flat', highlightbackground='grey', highlightthickness=1)
ship_from_phone_label.grid(row=1, column=5, padx=5, pady=5)
ship_from_phone.grid(row=1, column=6, padx=5, pady=10)

ship_to_label = Label(shipping_frame, bg=LABEL_COLOR, font=section_font, text='Ship To:')
ship_to_label.grid(row=2, pady=15, padx=5)

company_name_label = Label(shipping_frame, bg=LABEL_COLOR, font=ui_font, text='Company')
company_name = Entry(shipping_frame, font=ui_font, relief='flat', highlightbackground='grey', highlightthickness=1)
company_name_label.grid(row=3, column=1, padx=5, pady=10)
company_name.grid(row=3, column=2)

contact_name_label = Label(shipping_frame, bg=LABEL_COLOR, font=ui_font, text='Contact Name')
contact_name = Entry(shipping_frame, font=ui_font, relief='flat', highlightbackground='grey', highlightthickness=1)
contact_name_label.grid(row=3, column=3, padx=5, pady=10)
contact_name.grid(row=3, column=4)

address_line1_label = Label(shipping_frame, bg=LABEL_COLOR, font=ui_font, text='Address Line 1')
address_line1 = Entry(shipping_frame, font=ui_font, relief='flat', highlightbackground='grey', highlightthickness=1)
address_line1_label.grid(row=4, column=1, padx=5, pady=10)
address_line1.grid(row=4, column=2)

address_line2_label = Label(shipping_frame, bg=LABEL_COLOR, font=ui_font, text='Address Line 2')
address_line2 = Entry(shipping_frame, font=ui_font, relief='flat', highlightbackground='grey', highlightthickness=1)
address_line2_label.grid(row=4, column=3, padx=5, pady=10)
address_line2.grid(row=4, column=4)

address_line3_label = Label(shipping_frame, bg=LABEL_COLOR, font=ui_font, text='Address Line 3')
address_line3 = Entry(shipping_frame, font=ui_font, relief='flat', highlightbackground='grey', highlightthickness=1)
address_line3_label.grid(row=5, column=1, padx=5, pady=10)
address_line3.grid(row=5, column=2)

city_label = Label(shipping_frame, bg=LABEL_COLOR, font=ui_font, text='City')
city = Entry(shipping_frame, font=ui_font, relief='flat', highlightbackground='grey', highlightthickness=1)
city_label.grid(row=5, column=3, padx=5, pady=10)
city.grid(row=5, column=4)

country_label = Label(shipping_frame, bg=LABEL_COLOR, font=ui_font, text='Country')
country = Entry(shipping_frame, font=ui_font, relief='flat', highlightbackground='grey', highlightthickness=1)
country_label.grid(row=6, column=1, padx=5, pady=10)
country.grid(row=6, column=2)

state_label = Label(shipping_frame, bg=LABEL_COLOR, font=ui_font, text='State')
state = Entry(shipping_frame, font=ui_font, relief='flat', highlightbackground='grey', highlightthickness=1)
state_label.grid(row=6, column=3, padx=5, pady=10)
state.grid(row=6, column=4)

zip_code_label = Label(shipping_frame, bg=LABEL_COLOR, font=ui_font, text='Zip Code')
zip_code = Entry(shipping_frame, font=ui_font, relief='flat', highlightbackground='grey', highlightthickness=1)
zip_code_label.grid(row=6, column=5, padx=15, pady=10)
zip_code.grid(row=6, column=6)

phone_label = Label(shipping_frame, bg=LABEL_COLOR, font=ui_font, text='Phone')
phone = Entry(shipping_frame, font=ui_font, relief='flat', highlightbackground='grey', highlightthickness=1)
phone_label.grid(row=7, column=1, padx=5, pady=10)
phone.grid(row=7, column=2)

email_label = Label(shipping_frame, bg=LABEL_COLOR, font=ui_font, text='Email')
email = Entry(shipping_frame, font=ui_font, relief='flat', highlightbackground='grey', highlightthickness=1)
email_label.grid(row=7, column=3, padx=5, pady=10)
email.grid(row=7, column=4)

def generate_barcode():
    '''generates barcodes from form entires, triggers generation of HTML --> PDF converstion and prints the resulting PDF.'''

    T ='\t'

    alias_barcode = tp.generate_barcode('datamatrix', data=alias.get())
    alias_barcode.convert('1').save(user_path+r'\Documents\Barcodes\alias_barcode.png')

    barcode_company_city_concat = company_name.get()+T+contact_name.get()+T+address_line1.get()+T+address_line2.get()+T+address_line3.get()+T+city.get()+T+T+T+zip_code.get()+T+phone.get()+T+email.get()
    company_city_barcode = tp.generate_barcode('datamatrix', data=barcode_company_city_concat)
    company_city_barcode.convert('1').save(user_path+r'\Documents\Barcodes\company_city_barcode.png')

    data_elements = {
        'alias': alias.get(),
        'ship_from_name': ship_from_name.get(),
        'ship_from_phone': ship_from_phone.get(),
        'company_name': company_name.get(),
        'city': city.get(),
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
    '''clearing form fields'''
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

# Button
button = Button(button_frame,
                relief='flat',
                bg='#0078D4',
                fg='white',
                font=button_font,
                text='Generate Barcode',
                command=lambda: [generate_barcode(), clear_entries()])
button.pack(side='top', expand=True, pady=10)

# Logo
packaged_img = Image.open(
    user_path+r'\OneDrive - Microsoft\Documents\Barcode_Test\placeholder-logo-1.png').resize((260, 123))
packaged_logo = ImageTk.PhotoImage(packaged_img)
Label(logo_frame, bg='#F4F3F5', image=packaged_logo).pack(
    side='bottom', pady=10, padx=10, anchor='sw', expand=True)

win.mainloop()
