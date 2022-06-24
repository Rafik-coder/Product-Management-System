from tkinter import *
from tkinter.ttk import Treeview


def Add_product():
    add = Toplevel()
    
    # Getting the height and width of current Machine
    x = add.winfo_screenwidth()
    y = add.winfo_screenheight()

    # Using the got Height and Width to set up the Size of the App's Main Window
    add.geometry(f"{x}x{y}")
    add.title("made by xCoder")
    control_title = Frame(add, width=x, height=y/154)
    control_title.pack(anchor="center")
    control_title_lbl = Label(control_title, text="ADD PRODUCTS", font=("ALGERIAN", int(((x+y))//54)),
                            bg="green", fg="blue", relief=RIDGE, bd= int(((x+y))//213.4))
    control_title_lbl.pack()

    # Main Frame for adding Products
    adding_main_frame = Frame(add, width=x, height=y, bg="grey", relief=RIDGE, bd=int(((x+y))//213.4))
    adding_main_frame.pack(anchor="center")

    # Frame for the Entries and Buttons for adding products
    adding_product_frame = Frame(adding_main_frame, width=int(x/2.5), height=y, bg="light grey", relief=RIDGE, bd=5)
    adding_product_frame.pack(side="left")

    # Frame to show Products Added to the Database
    added_products_frame = Frame(adding_main_frame, width=int(x/1.5), height=y, bg="light grey", relief=RIDGE, bd=5)
    added_products_frame.pack(side="right")
    
    # Creating a Table for the Database of the Added Products
    cols = ("Stock/Qnt.", "Product Name", "Brand", "Price", "Expiry")
    produc_list = Treeview(added_products_frame, column=cols, show="headings", height=200)
    
    # Passing the values in the cols Tuple into the Table as headings
    for col in cols:
        produc_list.heading(col, text=col)
        produc_list.grid(row=1, column=0, columnspan=2)
        produc_list.place(x=5, y=5)


    product_name_lbl = Label(adding_product_frame, text="Product Name:", font=("Arial", 15))
    product_name_lbl.place(x=10, y=20)
    product_name_entry = Entry(adding_product_frame, width=int(x//30.35))
    product_name_entry.place(x=190, y=22)

    product_brand_lbl = Label(adding_product_frame, text="Product Brand:", font=("Arial", 15))
    product_brand_lbl.place(x=10, y=60)
    product_brand_entry = Entry(adding_product_frame, width=int(x//30.35))
    product_brand_entry.place(x=190, y=62)

    product_price_lbl = Label(adding_product_frame, text="Product Price:", font=("Arial", 15))
    product_price_lbl.place(x=10, y=100)
    product_price_entry = Entry(adding_product_frame, width=int(x//30.35))
    product_price_entry.place(x=190, y=102)

    product_quantity_lbl = Label(adding_product_frame, text="Stock:", font=("Arial", 15))
    product_quantity_lbl.place(x=10, y=140)
    product_quantity_entry = Entry(adding_product_frame, width=int(x//30.35))
    product_quantity_entry.place(x=190, y=142)

    add_pic = Label(adding_product_frame, text="Upload Product Picture:", font=("Arial", 15))
    add_pic.place(x=10, y=180)

    add_pic_btn = Button(adding_product_frame, text="Upload Photo")
    add_pic_btn.place(x=170, y=240)

    add__product_btb = Button(adding_product_frame, text="Add product", width=10, bg="blue")
    add__product_btb.place(x=300, y=340)
    
    back_to_home_btn = Button(adding_product_frame, text="<< BACK TO MAIN FRAME", width=20, height=3)
    back_to_home_btn.place(x=10, y=530)
    

    add.mainloop()
    
Add_product()
    