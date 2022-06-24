from math import prod
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from turtle import width
import sqlite3

# Getting the height and width of current Machine
# Using the gotten Height and Width of the Machine to set up the Size of the App's Main Window


class Employee:
    def __init__(self, root):
        self.root = root


    def get_chosen(self):
        chosen_row = produc_list.focus()
        contents = produc_list.item(chosen_row)
        row = contents["values"]

        product_name_entry.set(row[0])
        product_brand_entry.set(row[0])
        product_price_entry.set(row[0])
        product_quantity_state_entry.set(row[0])
        product_quantity_entry.set(row[0])
        product_name_entry.set(row[0])

    def sell(self, sel, hom):
        x = hom.winfo_screenwidth()
        y = hom.winfo_screenheight()
        control_title = Frame(sel, width=x, height=y/154)
        control_title.pack()
        control_title_lbl = Label(control_title, text="SELL PRODUCTS", font=("ALGERIAN", int(((x+y))//54)),
                                bg="green", fg="blue", relief=RIDGE, bd= int(((x+y))//213.4))
        control_title_lbl.pack()

        # Main Frame for adding Products
        selling_main_frame = Frame(sel, width=x, bg="grey", relief=RIDGE, bd=int(((x+y))//213.4))
        selling_main_frame.pack()
        
        ############################ Frame for the Entries and Buttons for adding products ################################
        selling_product_frame = Frame(selling_main_frame, width=x/2.5, height=y-(y/154), bg="light grey", relief=RIDGE, bd=5)
        selling_product_frame.pack(side="left")

        to_sell_frame = Frame(selling_product_frame, width=x/2.5, height=300, bg="light grey", relief=RIDGE, bd=5)
        to_sell_frame.grid(row=0, column=0)
        
        # Labels and Entries for the Product 
        product_name_lbl = Label(to_sell_frame, text="Product Name:", font=("Arial", 15))
        product_name_lbl.place(x=10, y=20)
        product_name = StringVar()
        global product_name_entry
        product_name_entry = Entry(to_sell_frame, width=int(x//35.35), textvariable=product_name)
        product_name_entry.place(x=190, y=22)

        product_brand_lbl = Label(to_sell_frame, text="Product Brand:", font=("Arial", 15))
        product_brand_lbl.place(x=10, y=60)
        product_brand = StringVar()
        global product_brand_entry
        brands = ("PAIN_KILLER", "STOMACH_UPSETS", "MALARIA", "ANIBIOTIC", "SKIN_GEL", "COUGH_MIXTURE", "BLOOD_TONIC", "APITIZER", "")
        product_brand_entry = ttk.Combobox(to_sell_frame, width=int(x//50.35), values=brands, state="readonly")
        product_brand_entry.place(x=190, y=62)

        product_price_lbl = Label(to_sell_frame, text="Product Price:", font=("Arial", 15))
        product_price_lbl.place(x=10, y=100)
        product_price = StringVar()
        global product_price_entry
        product_price_entry = Entry(to_sell_frame, width=int(x//35.35), textvariable=product_price)
        product_price_entry.place(x=190, y=102)

        product_quantity_lbl_state = Label(to_sell_frame, text="Stock State:", font=("Arial", 15))
        product_quantity_lbl_state.place(x=10, y=140)
        product_quantity_lbl_state = StringVar()
        global product_quantity_state_entry
        state = ("SACHET", "PACKET", "BOX")
        product_quantity_state_entry = ttk.Combobox(to_sell_frame, width=int(x//50.35), values=state, state="readonly")
        product_quantity_state_entry.place(x=190, y=142)

        product_quantity_lbl = Label(to_sell_frame, text="Stock/Quantity:", font=("Arial", 15))
        product_quantity_lbl.place(x=10, y=180)
        product_quantity = StringVar()
        global product_quantity_entry
        product_quantity_entry = Entry(to_sell_frame, width=int(x//35.35), textvariable=product_quantity)
        product_quantity_entry.place(x=190, y=182)

        # Button To Sell Product
        sell__product_btb = Button(to_sell_frame, text="Sell product", width=12, bg="yellow")
        sell__product_btb.place(x=370, y=220)

        #####################################################################################################################
        ReceitFrame = Frame(selling_product_frame, width=x/2.5, height=200, bg="light grey", relief=RIDGE, bd=5)
        to_sell_frame.grid(row=1, column=0)

        Receit = StringVar()
        receit = Text(ReceitFrame, height=15)
        receit.pack()

        print_btn = Button(ReceitFrame, width=10, text="PRINT")
        print_btn.pack()
        
        
        # #############################################################################################################################

        ########################### Frame to show Products Added to the Database #############################################
        produc_st_main = Frame(selling_main_frame, width=x, height=y/2, bg="light green")
        produc_st_main.pack()

        ########################### Frame for searching items in the Data Base ################################################
        prod_search = Frame(produc_st_main, width=int(x/1.65), height=y/12, bg="light green", relief=RIDGE, bd=5)
        prod_search.pack()

        search_by_lbl = Label(prod_search, text="Search By", font=("Arial black", 12))
        search_by_lbl.place(x=5, y=10)

        cols = ("Select Option","PRODUCT NAME", "TYPE OF PRODUCT", "PRICE", "STOCK/QUANTITY", "EXPIRY DATE")
        search_box = ttk.Combobox(prod_search, width=18, values=cols, state="readonly")
        search_box.current(0)
        search_box.place(x=110, y=14)

        search_entry = Entry(prod_search, width=20)
        search_entry.place(x=270, y=14)

        search_button = Button(prod_search, text="Search", width=8, background="red")
        search_button.place(x=445, y=13)

        show_all_btn = Button(prod_search, text="Show All Products", width=15, background="yellow")
        show_all_btn.place(x=540, y=13)
        
        #########################################
        conn = sqlite3.connect("Products.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Retail_Products")
        result = c.fetchall()
        
        added_products_frame = Frame(produc_st_main, width=x/2, height=y, bg="light grey", relief=RIDGE, bd=5)
        added_products_frame.pack(side="right")
        
        scroll_x = Scrollbar(added_products_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        
        scroll_y = Scrollbar(added_products_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        # Creating a Table for the Database of the Added Products
        global produc_list
        produc_list = Treeview(added_products_frame, column=cols[1:], show="headings", height=y/2, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_y.config(command=produc_list.yview)
        scroll_x.config(command=produc_list.xview)
        
        # Passing the values in the cols Tuple into the Table as headings
        for col in cols[1:]:
            produc_list.heading(col, text=col)
            produc_list.pack()

        produc_list.bind("<<ButtonRelease-1>>", Employee.get_chosen)

if __name__=='__main__':
    root = Tk()
    app = Employee(root)
    app.sell(root, root)
    root.mainloop()