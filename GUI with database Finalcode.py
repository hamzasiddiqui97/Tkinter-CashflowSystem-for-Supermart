# Modules
from tkinter import *
import sqlite3
from tkinter import messagebox


class Product:
    def __init__(self, window):
        self.window = window
        self.window.title('Cash Flow System')
        # self.window.geometry("1366x768")
        self.window.resizable(0, 0)
        self.window.config(bg='grey')

        ##DataBase Record Reference
        rec = Record()
        rec.sql_connect()

        product_tag = StringVar()
        product_name = StringVar()
        
        product_weight = StringVar()
        product_price =StringVar()
        product_expire = StringVar()
        product_stock = StringVar()
        product_dealer_details = StringVar()
        

        
        # Create_Frames
        # =============
        MainFrame = Frame(self.window, bg='white')
        MainFrame.grid()

        # Create_Header
        HeadFrame = Frame(MainFrame, bd=1, padx=60, pady=10, bg='white', relief=FLAT)
        HeadFrame.pack(side=TOP)
        self.Head_label = Label(HeadFrame, font=('arial', 30, 'bold'), text=' HyperMart Cash Flow System ', fg='black',
                                bg='white')
        self.Head_label.grid()

        # Create_ButtonFrame
        ButtonFrame = Frame(MainFrame, bd=1, width=1400, height=80, padx=60, pady=10, bg='grey', relief=FLAT)
        ButtonFrame.pack(side=BOTTOM)

        # Create_CentreFrame
        CenterFrame = Frame(MainFrame, bd=1, width=1250, height=300, padx=30, pady=10, bg='white', relief=FLAT)
        CenterFrame.pack(side=BOTTOM)

        # Create_left_body
        leftBody = LabelFrame(CenterFrame, bd=5, width=400, height=300, padx=30, pady=10, bg='white',
                              text='Details Section', font=('arial', 25, 'underline'), relief=FLAT)
        leftBody.pack(side=LEFT)

        # Create_right_body
        rightBody = LabelFrame(CenterFrame, bd=5, width=400, height=300, padx=30, pady=10, bg='white', text='DATA',
                               font=('arial', 25, 'underline'), relief=FLAT)
        rightBody.pack(side=RIGHT)



#================================================FUNCTIONS================================================
        def show_all():
            list_box.delete(0, END)
            
            for row in rec.sql_fetchAll():
                list_box.insert(END,row, str(''))
                
                
        def clear(): 
            self.textproduct_name.delete(0, END)
            self.textproduct_tag.delete(0, END)
            self.textproduct_weight.delete(0, END)
            self.textproduct_price.delete(0, END)
            self.textproduct_expire.delete(0, END)
            self.textproduct_stock.delete(0, END)
            self.textproduct_dealer_details.delete(0, END)
            

        def insert():
            try:
                rec.sql_insert(product_tag.get(), product_name.get(), product_weight.get(), product_price.get(),
                               product_expire.get(), product_stock.get(), product_dealer_details.get())
                list_box.delete(0, END)
                list_box.insert(END, product_tag.get(), product_name.get(), product_weight.get(), product_price.get(),
                                product_expire.get(), product_stock.get(), product_dealer_details.get())
                messagebox.showinfo("Cash Flow",'Data Inserted')
            except Exception as e:
                messagebox.showerror("Cash Flow",e)

        def show_price():
            try:
                list_box.delete(0, END)
                for row in rec.sql_fetch_price():
                    list_box.insert(END, row, str(''))
            except Exception as e:
                messagebox.showerror("Cash Flow", e)
            
        #click on record to show its detail on left body
        def product_record(event):
            global pd
            searchPd = list_box.curselection() [0]
            pd = list_box.get(searchPd)

            try:
                self.textproduct_tag.delete(0, END)
                self.textproduct_tag.insert(END,pd[0])
            
                self.textproduct_name.delete(0, END)
                self.textproduct_name.insert(END,pd[1])
            
                self.textproduct_weight.delete(0, END)
                self.textproduct_weight.insert(END,pd[2])
            
                self.textproduct_price.delete(0, END)
                self.textproduct_price.insert(END,pd[3])
            
                self.textproduct_expire.delete(0, END)
                self.textproduct_expire.insert(END,pd[4])
            
                self.textproduct_stock.delete(0, END)
                self.textproduct_stock.insert(END,pd[5])
            
                self.textproduct_dealer_details.delete(0, END)
                self.textproduct_dealer_details.insert(END,pd[6])

            except Exception as e:
                messagebox.showerror('Cash Flow',e)


        def delete():
            try:
                rec.sql_delete(pd[0])
                clear()
                show_all()
                messagebox.showinfo('Cash Flow', 'Data Deleted')

            except Exception as e:
                messagebox.showerror('Cash Flow', e)


        def total():
            try:
                list_box.delete(0, END)
                for rows in rec.sql_sum():
                    list_box.insert(END,'Total Cash Flow(Rs)',rows, str(''))
            except Exception as e:
                messagebox.showerror('Cash Flow',e)

    
        ##Sroll Bar For ListBox
        scroll = Scrollbar(rightBody)
        scroll.grid(row=0, column=1, sticky="ns")

        # Create_ListBox
        # To show data saved in the database

        list_box = Listbox(rightBody, height=18, width=35, font = ('arial',15),yscrollcommand= scroll.set)
        #Called product_record function 
        list_box.bind("<<ListboxSelect>>", product_record)
        list_box.grid(row=0, column=0, padx=7)
        scroll.config(command=list_box.yview)

        # Create_Left_body Widgets
        # ========================
        # LABEL1
        self.labelproduct_tag = Label(leftBody, text='Product ID: ', font=('arial', 14), padx=2, pady=2, bg='white',
                                      fg='black')
        self.labelproduct_tag.grid(row=0, column=0)

        self.textproduct_tag = Entry(leftBody, textvariable=product_tag, font=('arial', 14), width=15)
        self.textproduct_tag.grid(row=0, column=1)

        # LABEL2
        self.labelproduct_name = Label(leftBody, text='Product Name: ', font=('arial', 14), padx=2, pady=2, bg='white',
                                       fg='black')
        self.labelproduct_name.grid(row=1, column=0)

        self.textproduct_name = Entry(leftBody, textvariable=product_name, font=('arial', 14), width=15)
        self.textproduct_name.grid(row=1, column=1)

        # LABEL3
        self.labelproduct_weight = Label(leftBody, text='Product Weight: ', font=('arial', 14), padx=2, pady=2,
                                         bg='white', fg='black')
        self.labelproduct_weight.grid(row=2, column=0)

        self.textproduct_weight = Entry(leftBody, textvariable=product_weight, font=('arial', 14), width=15)
        self.textproduct_weight.grid(row=2, column=1)

        # LABEL4
        self.labelproduct_price = Label(leftBody, text='Product Price(Rs): ', font=('arial', 14), padx=2, pady=2,
                                        bg='white', fg='black')
        self.labelproduct_price.grid(row=3, column=0)

        self.textproduct_price = Entry(leftBody, textvariable=product_price, font=('arial', 14), width=15)
        self.textproduct_price.grid(row=3, column=1)

        # LABEL5
        self.labelproduct_expire = Label(leftBody, text='Product Expire Date:', font=('arial', 14), padx=2, pady=2,
                                         bg='white', fg='black')
        self.labelproduct_expire.grid(row=4, column=0)

        self.textproduct_expire = Entry(leftBody, textvariable=product_expire, font=('arial', 14), width=15)
        self.textproduct_expire.grid(row=4, column=1)

        # LABEL6
        self.labelproduct_stock = Label(leftBody, text='Product Stock(Y/N): ', font=('arial', 14), padx=2, pady=2,
                                        bg='white', fg='black')
        self.labelproduct_stock.grid(row=5, column=0)

        self.textproduct_stock = Entry(leftBody, textvariable=product_stock, font=('arial', 14), width=15)
        self.textproduct_stock.grid(row=5, column=1)

        # LABEL6
        self.labelproduct_dealer_details = Label(leftBody, text='Company: ', font=('arial', 14), padx=2, pady=2,
                                                 bg='white', fg='black')
        self.labelproduct_dealer_details.grid(row=6, column=0)

        self.textproduct_dealer_details = Entry(leftBody, textvariable=product_dealer_details, font=('arial', 14),
                                                width=15)
        self.textproduct_dealer_details.grid(row=6, column=1)
        
        # Create_Buttons
        # Button1
        self.buttonInsert = Button(ButtonFrame, text='Add Stock', font=('arial', 15), width=12, command=insert)
        self.buttonInsert.grid(row=0, column=1)

        # Button2
        self.buttonShow = Button(ButtonFrame, text='Check Stock', font=('arial', 15), width=12, command=show_all)
        self.buttonShow.grid(row=0, column=2)

        # Button3
        self.buttonDelete = Button(ButtonFrame, text='Delete Stock', font=('arial', 15), width=12, command = delete)
        self.buttonDelete.grid(row=0, column=3)

        # Button5
        self.buttonClear = Button(ButtonFrame, text='Clear All', font=('arial', 15), width=12, command=clear)
        self.buttonClear.grid(row=0, column=5)

        # Button6
        self.buttonTotal = Button(ButtonFrame, text='Cash Column', font=('arial', 15), width=15, command=show_price)
        self.buttonTotal.grid(row=0, column=6)
        # Button7
        self.buttonSum = Button(ButtonFrame, text='Total Cash Flow', font=('arial', 15), width=15, command=total)
        self.buttonSum.grid(row=0, column=7)

#==============================================DATABASE CONNECTION==============================================    
class Record():
    def sql_connect(self):
        try:
            conn = sqlite3.connect('CashFlowDatabase.db')
            cursorObj = conn.cursor()
            cursorObj.execute(
                "CREATE TABLE if not exists product(productID INTEGER PRIMARY KEY,productName TEXT, productWeight INTEGER, productPrice REAL, expireDate REAL, productAvailable TEXT,productDealer TEXT)")
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Cash Flow", e)

    def sql_insert(self, product_tag, product_name, product_weight, product_price, product_expire, product_stock,
                   product_dealer_details):
        conn = sqlite3.connect('CashFlowDatabase.db')
        cursorObj = conn.cursor()
        query = "INSERT INTO product VALUES(?,?,?,?,?,?,?)"
        cursorObj.execute(query, (product_tag, product_name, product_weight, product_price, product_expire, product_stock,product_dealer_details))
        conn.commit()
        conn.close()
        
    def sql_fetchAll(self):
        conn = sqlite3.connect('CashFlowDatabase.db')
        cursorObj = conn.cursor()
        query = "SELECT * from product"
        cursorObj.execute(query)
        rows = cursorObj.fetchall()
        conn.close()
        return rows

    def sql_fetch_price(self):
        conn = sqlite3.connect('CashFlowDatabase.db')
        cursorObj = conn.cursor()
        cursorObj.execute('SELECT productID,productName,productPrice FROM product')
        rows = cursorObj.fetchall()
        conn.close()
        return rows

    def sql_delete(self,product_tag):
        conn = sqlite3.connect('CashFlowDatabase.db')
        cursorObj = conn.cursor()
        cursorObj.execute("DELETE FROM product WHERE productID = ?" ,(product_tag,))
        conn.commit()
        conn.close()

    def sql_search(self,product_tag ='', product_name='', product_weight='', product_price='', product_expire='', product_stock='',product_dealer_details=''):
        conn = sqlite3.connect('CashFlowDatabase.db')
        cursorObj = conn.cursor()
        cursorObj.execute("SELECT * FROM product WHERE productID=? or productName=? or productWeight=? or productPrice=? or expireDate=? or productAvailable=? or productDealer =? ")
        rows = cursorObj.fetchall()        
        conn.close()


    def sql_sum(self):
        conn = sqlite3.connect('CashFlowDatabase.db')
        cursorObj = conn.cursor()
        cursorObj.execute('SELECT sum(productPrice)FROM product')
        rows = cursorObj.fetchall()
        conn.close()
        return rows

        
        
  
if __name__ == "__main__":
    window = Tk()
    app = Product(window)
    window.mainloop()
