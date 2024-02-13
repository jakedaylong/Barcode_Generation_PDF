# Barcode Generation

Script written in Python to allow for the input of user shipping addresses in order to generate a 2D barcode for easier input into a shipping system. 

Developed as a stop-gap measure, pending new feature creation, in order to reduce processing time for shipping personnel taking in customer orders and processing them in the shipping system UI.

Barcode generation happens all within the local system. Address input information and barcodes are then rendered to an HTML page and finally converted into a PDF for printing. 

Each barcode contains information that is both hardcoded and user-defined with <TAB> injected in between to support navigation between UI input fields to facilitate data input on screen. 
