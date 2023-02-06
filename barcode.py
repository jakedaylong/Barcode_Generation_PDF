import treepoem as tp
import gui_test

def barcode_test():
    alias_barcode = tp.generate_barcode(alias.get(), 'test')
    barcode.convert('1').save('alias_barcode.png')