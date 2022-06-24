from ast import Add
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox
import sqlite3
from tkinter.ttk import Combobox
from turtle import bgcolor
from unittest import result
from django.forms import FloatField
from pyparsing import White
from tkcalendar import *
import datetime


# Creating Function for main Administrator Page
def Administrator():
    
    admin = Tk()
    
    # Creating a Notebook to place all Other windows thal will open when a button is clicked as Tabs
    home = ttk.Notebook(admin)
    home.pack()

    # Getting the height and width of current Machine
    x = admin.winfo_screenwidth()
    y = admin.winfo_screenheight()

    # Using the gotten Height and Width of the Machine to set up the Size of the App's Main Window
    admin.geometry(f"{x}x{y}+0+0")
    admin.title("made by xCoder")
    
    # Setting Up the Main Tab for the Administrator
    home_tab = Frame(home, width=x, height=y)
    home.add(home_tab, text="Administrator")
    
    # Setting Up the Tab for Adding Products
    add_tab = Frame(home, width=x, height=y)
    home.add(add_tab)
    home.hide(1)
    
    # Setting Up the Tab for Adding Products
    sell_tab = Frame(home, width=x, height=y)
    home.add(sell_tab)
    # home.hide(2)
    
    # Setting Up the Tab for Adding Products
    transactions_tab = Frame(home, width=x, height=y)
    home.add(transactions_tab)
    home.hide(3)
    
    # Adding Product to data Base
    class Add_product_db():
        
        def creat():
            
            conn = sqlite3.connect("Products.db")
            c = conn.cursor()

            c.execute("""CREATE TABLE IF NOT EXISTS Retail_Products (
                Product_Name TEXT,
                Brand TEXT,
                Price FLOAT,
                Stock_State TEXT,                                                                                                                               
                Stock_Qtn INT,
                Expiry TEXT
                )""")
            conn.commit()
            conn.close()
            
        def check():
            prod_name = product_name_entry.get()
            prod_brand = product_brand_entry.get()
            prod_price = product_price_entry.get()
            stock_state = product_quantity_state_entry.get()
            prod_quantity = product_quantity_entry.get()
            prod_expiry = product_expiry_entry.get()
            
            if prod_name=="" or prod_brand=="" or prod_price=="" or prod_quantity=="":
                messagebox.showerror("Error", "Please fill all Entry Fields")
                
            else:
                conn = sqlite3.connect("Products.db")
                c = conn.cursor()
                alert = messagebox.askyesno("Confirm", "Do you want to Add Product?")
                if alert==1:
                    
                    c.execute("INSERT INTO Retail_Products VALUES (?, ?, ?, ?, ?, ?)", (prod_name.upper(), prod_brand, prod_price, stock_state, prod_quantity, prod_expiry))

                    conn.commit()
                    conn.close()
                    showRetail()
                    
                    messagebox.showinfo("Info", "Product Added")
                    product_name_entry.delete(0, END)
                    product_brand_entry.delete(0, END)
                    product_price_entry.delete(0, END)
                    product_quantity_entry.delete(0, END)
                    
                elif alert==0:
                    messagebox.showinfo("Resubmit", "Make your Changes And Add Product")

    
    def update_db():
        prod_name = product_name.get()
        prod_brand = product_brand.get()
        prod_price = product_price.get()
        stock_state = product_quantity_state.get()
        prod_quantity = product_quantity.get()
        prod_expiry = product_expiry.get()
        
        
        if prod_name=="" or prod_brand=="" or prod_price=="" or prod_quantity=="":
            messagebox.showerror("Error", "Please Choose A Product to Update")
            
        else:
            alert = messagebox.askyesno("Confirm", "Press YES to Update Product!!")
            if alert==1:
                conn = sqlite3.connect("Products.db")
                c = conn.cursor()
                id = c.execute("SELECT * FROM Retail_Products")
                ids = id.fetchall()

                if prod_name != "":
                    c.execute(f"""UPDATE Retail_Products SET Product_Name='{prod_name.upper()}',
                            Brand='{prod_brand.upper()}',
                            Price='{prod_price}',
                            Stock_State='{stock_state.upper()}',
                            Stock_Qtn='{prod_quantity}',
                            Expiry='{prod_expiry}'
                            """)

                messagebox.showinfo("Info", "Product Updated")

                product_name_entry.delete(0, END)
                product_brand_entry.set("")
                product_brand_entry.delete(0, END)
                product_price_entry.delete(0, END)
                product_quantity_state_entry.set("")
                product_quantity_entry.delete(0, END)
                product_expiry_entry.delete(0, END)
                

                conn.commit()
                conn.close()
                showRetail()
                
    def delete_db():
        prod_name = product_name.get()
        prod_brand = product_brand.get()
        prod_price = product_price.get()
        stock_state = product_quantity_state.get()
        prod_quantity = product_quantity.get()
        prod_expiry = product_expiry.get()
        
        if prod_name=="" or prod_brand=="" or prod_price=="" or prod_quantity=="":
            messagebox.showerror("Error", "Please Choose A Product to Delete")
            
        else:
            alert = messagebox.askyesno("Alert", "This will Delete the Product Permenently, Do you want to Proceed?")
            if alert==1:
                conn = sqlite3.connect("Products.db")
                c = conn.cursor()
                fetch = c.execute(f"SELECT * FROM Retail_Products WHERE Product_Name='{prod_name}'")
                result = fetch.fetchall()
                
                c.execute(f"DELETE FROM Retail_Products WHERE Product_Name='{result[0][0]}'")

                product_name_entry.delete(0, END)
                product_brand_entry.delete(0, END)
                product_price_entry.delete(0, END)
                product_quantity_entry.delete(0, END)
                messagebox.showinfo("Info", "Product DELETED")

                conn.commit()
                conn.close()
            showRetail()




    def showRetail():
        conn = sqlite3.connect("Products.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Retail_Products")
        list = c.fetchall()

        if len(list) != 0:
            produc_list.delete(*produc_list.get_children())
            for item in list:
                produc_list.insert('', END, values=item)
            conn.commit()
        conn.close()

    def get_chosen(self):
        product_name_entry.delete(0, END)
        product_brand.set("")
        product_brand_entry.delete(0, END)
        product_price_entry.delete(0, END)
        product_quantity.set("")
        product_quantity_entry.delete(0, END)
        product_expiry_entry.delete(0, END)
        
        view_prod = produc_list.focus()
        prod_detail = produc_list.item(view_prod)
        row = prod_detail['values']

        product_name.set(row[0])
        product_brand.set(row[1])
        product_price.set(row[2])
        product_quantity_state.set(row[3])
        product_quantity.set(row[4])
        product_expiry.get_date()

    # Function to Create Adding products Page
    def add_page():
        Add_product_db.creat()
        # showData()
        home.hide(0)
        home.select(1)
        control_title = Frame(add_tab, width=x, height=y/154)
        control_title.pack()
        control_title_lbl = Label(control_title, text="ADD PRODUCTS", font=("ALGERIAN", int(((x+y))//54)),
                                bg="green", fg="blue", relief=RIDGE, bd= int(((x+y))//213.4))
        control_title_lbl.pack()

        # Main Frame for adding Products
        adding_main_frame = Frame(add_tab, width=x, height=y-(y/154), bg="grey", relief=RIDGE, bd=int(((x+y))//213.4))
        adding_main_frame.pack()
        
        ############################ Frame for the Entries and Buttons for adding products ################################
        adding_product_frame = Frame(adding_main_frame, width=x/2.5, height=y-(y/154), bg="light grey", relief=RIDGE, bd=5)
        adding_product_frame.pack(side="left")
        
        # Labels and Entries for the Product 
        product_name_lbl = Label(adding_product_frame, text="Product Name:", font=("Arial", 15))
        product_name_lbl.place(x=10, y=20)
        global product_name
        product_name = StringVar()
        global product_name_entry
        product_name_entry = Entry(adding_product_frame, width=int(x//35.35), textvariable=product_name)
        product_name_entry.place(x=190, y=22)

        product_brand_lbl = Label(adding_product_frame, text="Product Brand:", font=("Arial", 15))
        product_brand_lbl.place(x=10, y=60)
        global product_brand
        product_brand = StringVar()
        global product_brand_entry
        brands = ("PAIN_KILLER", "STOMACH_UPSETS", "MALARIA", "ANTIBIOTIC", "SKIN_GEL", "COUGH_MIXTURE", "BLOOD_TONIC", "APITIZER", "")
        product_brand_entry = ttk.Combobox(adding_product_frame, textvariable=product_brand, width=int(x//50.35), values=brands, state="readonly")
        product_brand_entry.place(x=190, y=62)

        product_price_lbl = Label(adding_product_frame, text="Product Price:", font=("Arial", 15))
        product_price_lbl.place(x=10, y=100)
        global product_price
        product_price = DoubleVar()
        global product_price_entry
        product_price_entry = Entry(adding_product_frame, width=15, textvariable=product_price)
        product_price_entry.place(x=190, y=102)

        product_quantity_lbl_state = Label(adding_product_frame, text="For:", font=("Arial", 15))
        product_quantity_lbl_state.place(x=320, y=100)
        global product_quantity_state
        product_quantity_state = StringVar()
        global product_quantity_state_entry
        state = ("A SACHET", "A PACKET", "A BOX")
        product_quantity_state_entry = ttk.Combobox(adding_product_frame, textvariable=product_quantity_state,width=int(x//70.35), values=state, state="readonly")
        product_quantity_state_entry.place(x=365, y=107)

        product_quantity_lbl = Label(adding_product_frame, text="Stock/Quantity:", font=("Arial", 15))
        product_quantity_lbl.place(x=10, y=180)
        global product_quantity
        product_quantity = IntVar()
        global product_quantity_entry
        product_quantity_entry = Entry(adding_product_frame, width=int(x//35.35), textvariable=product_quantity)
        product_quantity_entry.place(x=190, y=182)

        product_expiry_lbl = Label(adding_product_frame, text="Product Expiry", font=("Arial", 15))
        product_expiry_lbl.place(x=10, y=220)
        global product_expiry
        product_expiry = DateEntry()
        global product_expiry_entry
        product_expiry_entry = DateEntry(adding_product_frame, width=int(x//35.35),
                                         textvariable=product_expiry, selectmode="day",
                                         state="readonly") 
        product_expiry_entry.place(x=190, y=222)

        add_pic = Label(adding_product_frame, text="Upload Product Picture:", font=("Arial", 15))
        add_pic.place(x=10, y=260)

        add_pic_btn = Button(adding_product_frame, text="Upload Photo")
        add_pic_btn.place(x=170, y=320)

        # Button To Add Product to Data Base
        add__product_btb = Button(adding_product_frame, text="Add product", width=12, bg="yellow", command=Add_product_db.check, padx=5)
        add__product_btb.place(x=200, y=410)
        
        # Button To Delete Product ffrom Data Base
        delete__product_btb = Button(adding_product_frame, text="Delete product", width=13, bg="yellow", command=delete_db, padx=5)
        delete__product_btb.place(x=310, y=410)
        
        # Button To Update Product from Data Base
        update__product_btb = Button(adding_product_frame, text="Update product", width=12, bg="yellow", command=update_db, padx=5)
        update__product_btb.place(x=425, y=410)
        
        # Button to Navigate Back to the Administrator Page
        back_to_home_btn = Button(adding_product_frame, text="<< BACK TO MAIN MENU", width=20, height=3, command=home_Page, padx=5)
        back_to_home_btn.place(x=10, y=490)
        # #############################################################################################################################

        ########################### Frame to show Products Added to the Database #############################################
        produc_st_main = Frame(adding_main_frame, width=x, height=y/2, bg="light green")
        produc_st_main.pack()

        ########################### Frame for searching items in the Data Base ################################################
        
        def search_db(column, prod):
            conn = sqlite3.connect("Products.db")
            c = conn.cursor()
            fetch = c.execute(f"SELECT * FROM Retail_Products WHERE {column}='{prod}'")
            results = fetch.fetchall()
            
            if len(results) != 0:
                produc_list.delete(produc_list.get_children())
                for row in results:
                    produc_list.insert('', END, values=row)
                    
            else:
                messagebox.showinfo("Missing", "No Product Matched")
            
        
        
        prod_search = Frame(produc_st_main, width=int(x/1.65), height=y/12, bg="light green", relief=RIDGE, bd=5)
        prod_search.pack()

        search_by_lbl = Label(prod_search, text="Search By", font=("Arial black", 12))
        search_by_lbl.place(x=5, y=10)

        bar = ("", "Product_Name", "Brand", "Price", "Stock_Type", "Stock/Qnt.", "Expiry")
        search_box = ttk.Combobox(prod_search, width=18, values=bar, state="readonly")
        search_box.current(0)
        search_box.place(x=110, y=14)

        search_entry = Entry(prod_search, width=20)
        search_entry.place(x=270, y=14)

        search_button = Button(prod_search, text="Search", width=8, background="red", command= lambda: search_db(search_box.get(), search_entry.get()))
        search_button.place(x=445, y=13)

        show_all_btn = Button(prod_search, text="Show All Products", width=15, background="yellow")
        show_all_btn.place(x=540, y=13)
        
        #########################################
        
        added_products_frame = Frame(produc_st_main, width=x/2, height=y, bg="light grey", relief=RIDGE, bd=5)
        added_products_frame.pack(side="right")
        
        scroll_x = Scrollbar(added_products_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        
        scroll_y = Scrollbar(added_products_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        cols = ("Product_Name", "Brand", "Price", "Stock_Type", "Stock/Qnt.", "Expiry")
        
        # Creating a Table for the Database of the Added Products
        global produc_list
        produc_list = Treeview(added_products_frame, column=cols, show="headings", height=y/2, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_y.config(command=produc_list.yview)
        scroll_x.config(command=produc_list.xview)
        
        # Passing the values in the cols Tuple into the Table as headings
        for col in cols:
            produc_list.heading(col, text=col)
            produc_list.pack(fill=BOTH, expand=1)

        showRetail()
        produc_list.bind("<ButtonRelease-1>", get_chosen)
        

        
    def Sell():
        home.hide(0)
        home.select(2)
        from employee_pannel import Employee
        Employee(home).sell(sell_tab, home)
        
        # Button to Navigate Back to the Administrator Page
        back_to_home_btn = Button(sell_tab, text="<< BACK TO MAIN MENU", width=20, height=3, command=home_Page)
        back_to_home_btn.place(x=13, y=580)
        # ##################################
        # return selll
        
    
    def Transactions():
        home.hide(0)
        add_tab = Frame(home, width=x, height=y)
        home.select(3)
        control_title = Frame(transactions_tab, width=x, height=y/154)
        control_title.pack(anchor="center")
        control_title_lbl = Label(control_title, text="TRANSACTIONS MADE", font=("ALGERIAN", int(((x+y))//54)),
                                bg="green", fg="blue", relief=RIDGE, bd= int(((x+y))//213.4))
        control_title_lbl.pack()

        # Main Frame for adding Products
        adding_main_frame = Frame(transactions_tab, width=x, height=y, bg="grey", relief=RIDGE, bd=int(((x+y))//213.4))
        adding_main_frame.pack(anchor="center")
        
        
        back_to_home_btn = Button(adding_main_frame, text="<< BACK TO MAIN MENU", width=20, height=3, command=home_Page)
        back_to_home_btn.place(x=10, y=510)
        
        
    # Function to Create the Administrator Pannel
    def home_Page(): 
        home.hide(1) 
        home.hide(2) 
        home.hide(3)
        home.select(0)
        control_title = Frame(home_tab, width=x, height=y/154)
        control_title.pack(anchor="center")
        control_title_lbl = Label(control_title, text="COMPANY NAME", font=("ALGERIAN", int(((x+y))//54)),
                                bg="green", fg="blue", relief=RIDGE, bd= int(((x+y))//213.4))
        control_title_lbl.pack()
        
        # Creating a main Frame for other Frames
        main_frame = Frame(home_tab, width=x, height=y, bg="grey", relief=RIDGE, bd=int(((x+y))//213.4))
        main_frame.pack(anchor="center")

        # Creating a Left main Frame
        left_frame = Frame(main_frame, width=int(x/1.5), height=y, borderwidth=int(((x+y))//1067), bg="grey", relief=RIDGE, bd=int(((x+y))//213.4))
        left_frame.pack(side="left")

        # Creating a right main Frame
        right_frame = Frame(main_frame, width=int(x/2.5), height=y, borderwidth=2, bg="grey", relief=RIDGE, bd=int(((x+y))//213.4))
        right_frame.pack(side="right")

        # Creating a Frame for Buttons in the Administator Pannel (Addimg Products, Selling Products, Transactions Feedback) 
        business_frame = Frame(right_frame, width=int(x/2.5)-int(x/2.5)/5, relief=RIDGE, bd=int(((x+y))//213.4), height=y//26, bg="grey")
        business_frame.pack()

        # Label As title fo
        business_frame_lbl = Label(business_frame, text="BUSINESS FEEDBACK", font=("ALGERIAN", int(((x+y))//107)), bg="yellow")
        business_frame_lbl.pack(side="top")

        # Definning the Buttons
        buttons_frame = Frame(right_frame, width=int(x/2.5)-int(x/2.5)/5, relief=RIDGE, bd=int(((x+y))//213.4), height=y, bg="grey")
        buttons_frame.pack()

        add_btn = Button(buttons_frame, text="ADD PRODUCT", width=int(x//30.35), relief=RIDGE, bd=int(((x+y))//427), command=add_page)
        add_btn.place(x=10, y=20)

        sell_btn = Button(buttons_frame, text="RETAIL PRODUCTS", width=int(x//30.35), relief=RIDGE, bd=int(((x+y))//427), command=Sell)
        sell_btn.place(x=10, y=90)

        my_transaction_btn = Button(right_frame, text="WHOLESALE PRODUCTS", width=int(x//30.35), relief=RIDGE, bd=int(((x+y))//427), command=Transactions)
        my_transaction_btn.place(x=20, y=240)

        my_transaction_btn = Button(right_frame, text="MY FEEDBACK", width=int(x//30.35), relief=RIDGE, bd=int(((x+y))//427), command=Transactions)
        my_transaction_btn.place(x=20, y=350)
        

        calender_frame = Frame(left_frame, width=int(x/2.5), height=y/2, bd=5)
        calender_frame.grid(row=0, column=0)
        calender = Calendar(calender_frame, selectmode="day", date_pattern="dd-mm-yyyy", font=('arial', 8, 'bold'))
        calender.grid(row=0, column=0)


        feedframe = Text(left_frame, width=42, height=14, bd=3)
        feedframe.grid(row=1, column=0)
        # sold_lbl = Label(feedframe, text="Number Of Sold Products")
        # sold_lbl.pack()

    
    home_Page()
    
    admin.mainloop()

Administrator()
