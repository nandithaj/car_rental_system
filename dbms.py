from tkinter import messagebox, simpledialog
from tkinter import ttk
from tkinter import *
from datetime import datetime
import pymysql
from PIL import Image, ImageTk

class CarRentalApp:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("600x600")
        self.root.title("DBMS PROJECT")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()
        self.frame1 = Frame(self.notebook, width=500, height=500, bg="lightblue")
        self.frame2 = Frame(self.notebook, width=500, height=500, bg="lightgreen")  
        self.frame3 = Frame(self.notebook, width=500, height=500, bg="orange")
        self.frame1.pack(fill="both", expand=1)
        self.frame2.pack(fill="both", expand=1)
        self.frame3.pack(fill="both", expand=1)
        self.notebook.add(self.frame1, text="admin")
        self.notebook.add(self.frame2, text="book")
        self.notebook.add(self.frame3, text="return")
        self.load_frame2()
        self.load_frame3()

con=pymysql.connect(host="localhost",user="root",password="1234",database="college")
check=0


def refresh():
    global app_instance
    if app_instance:
        app_instance.root.destroy()
    app_instance = CarRentalApp()

def enter():

    def addcar():

        e1=ent1.get()
        e2=ent2.get()
        e3=ent3.get()
        cur=con.cursor()
        x='y'
        cur.execute("insert into cars(car_id,brand,rent,available) values(%s,%s,%s,%s)",(e1,e2,e3,x))
        con.commit()
        carid.delete(0,END)
        brand.delete(0,END)
        price.delete(0,END)
        messagebox.showinfo('success',"car inserted!")
    #frame2add()

#function for deleting a car
    def delcar():
        e1=ent1.get()
        e2=ent2.get()
        e3=ent3.get()
        cur=con.cursor()
        x='y'
        cur.execute("delete from cars where car_id=%s and available=%s",(e1,x))
        con.commit()
        carid.delete(0,END)
        brand.delete(0,END)
        price.delete(0,END)
        messagebox.showinfo('success','car deleted!!')

#creating the main window
    root=Toplevel()
    root.geometry("600x600")
    root.title("DBMS PROJECT")

    #creating a notebook for tabs(admin,book,return)
    notebook=ttk.Notebook(root)
    notebook.pack()

    #creating 3 frames 
    frame1=Frame(notebook,width=500,height=500,bg="lightblue")
    frame2=Frame(notebook,width=500,height=500,bg="lightgreen")  
    frame3=Frame(notebook,width=500,height=500,bg="orange")

    frame1.pack(fill="both",expand=1)
    frame2.pack(fill="both",expand=1)
    frame3.pack(fill="both",expand=1)

    notebook.add(frame1,text="admin")
    notebook.add(frame2,text="book")
    notebook.add(frame3,text="return")

    #notebook.hide(1)

    # def show():
    # notebook.add(frame2,text="book")


    ent1=IntVar()
    ent2=StringVar()
    ent3=IntVar()

    #adding and droping car window
    lab=Label(frame1,text="WELCOME TO CAR RENTAL SYSTEM").pack()

    lab1=Label(frame1,text="CARID").place(x=150,y=50)
    carid=Entry(frame1,textvariable=ent1)
    carid.place(x=200,y=50)

    lab2=Label(frame1,text="BRAND").place(x=150,y=80)
    brand=Entry(frame1,textvariable=ent2)
    brand.place(x=200,y=80)

    lab3=Label(frame1,text="RENT").place(x=150,y=110)
    price=Entry(frame1,textvariable=ent3)
    price.place(x=200,y=110)

    but1=Button(frame1,text="ADD CAR",command=addcar).place(x=200,y=200)
    but2=Button(frame1,text="DROP CAR",command=delcar).place(x=300,y=200)

    #butshow=Button(frame1,text="GO TO BOOK",command=show).place(x=250,y=400)
    # def frame2add():
    #displaying available cars
    labf=Label(frame2,text="AVAILABLE CARS").pack()

    treescroll=Frame(frame2)
    treescroll.pack()

    scroll=Scrollbar(frame2)
    scroll.pack(side=RIGHT,fill=Y)
    tree=ttk.Treeview(frame2,yscrollcommand=scroll.set) #yscrollcommand=scroll.set)
    scroll.config(command=tree.yview)
    
    #vsb=Scrollbar(root,orient="vertical")
    #vsb.configure(command=tree.yview)
    #tree.configure(yscrollcommand=vsb.set)
    #vsb.pack(fill=Y,side=RIGHT)

    tree['show']='headings'
    s=ttk.Style(root)
    s.theme_use("clam")
    tree.pack()

    tree['columns']=("car_id","brand","rent")
    cur=con.cursor()
    y='y'
    cur.execute("select car_id,brand,rent from cars where available='y'")
        #con.commit()
        #cur.close()
    tree.column("car_id",width=50,minwidth=50,anchor=CENTER)
    tree.column("brand",width=100,minwidth=100,anchor=CENTER)
    tree.column("rent",width=150,minwidth=150,anchor=CENTER)

        #headings
    tree.heading("car_id",text="carid",anchor=CENTER)
    tree.heading("brand",text="brand",anchor=CENTER)
    tree.heading("rent",text="rent",anchor=CENTER)

    i=0
    for row in cur:
        tree.insert('',i,text='',values=(row[0],row[1],row[2]))
        i+=1

    con.commit()

    #vsb=Scrollbar(root,orient="vertical")
    #vsb.configure(command=tree.yview)
    #tree.configure(yscrollcommand=vsb.set)
    #vsb.pack(fill=Y,side=RIGHT)

    ent4=IntVar()
    ent5=StringVar()
    ent6=StringVar()
    ent7=StringVar()
    ent8=StringVar()
    ent9=StringVar()
    #function to book a car
    def bookcar():
        a = ent4.get() # Car ID
        b = ent5.get() # Name
        c = ent6.get() # Email
        d = ent7.get() # Start Date
        e = ent8.get() # Location
        end_date = ent9.get() # End Date

        # Check if all required fields are filled
        if not (a and b and c and d and e and end_date):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # Calculate the number of days between start_date and end_date
        start_date = datetime.strptime(d, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        delta = end_date - start_date
        number_of_days = delta.days

        # Retrieve the rent for the selected car
        cur = con.cursor()
        cur.execute("SELECT rent FROM cars WHERE car_id=%s", (a,))
        rent = 0
        for row in cur:
            rent = row[0]

        # Calculate the total price
        total_price = number_of_days * rent

        # Insert data into the database
        cur = con.cursor()
        cur.execute("INSERT INTO users(name, email, startdate, loc, enddate, total_price) VALUES(%s, %s, %s, %s, %s, %s)",
                    (b, c, d, e, end_date, total_price))
        con.commit()

        cur = con.cursor()
        cur.execute("SELECT user_id FROM users WHERE name=%s AND email=%s", (b, c))
        user_id = 0
        for row in cur:
            user_id = row[0]

        cur = con.cursor()
        cur.execute("INSERT INTO manages(user_id, car_id) VALUES(%s, %s)", (user_id, a))
        x = 'n'
        cur.execute("UPDATE cars SET available=%s WHERE car_id=%s", (x, a))
        con.commit()

        # Clean up
        cur.execute("DELETE FROM manages WHERE car_id NOT IN (SELECT car_id FROM cars)")
        con.commit()
        cur.execute("DELETE FROM users WHERE user_id NOT IN (SELECT user_id FROM manages)")
        con.commit()

        messagebox.showinfo("Success", f"Car booked successfully!\nTotal Price: {total_price}")
        carbook.delete(0, END)
        carname.delete(0, END)
        carsdate.delete(0, END)
        carmail.delete(0, END)
        caredate.delete(0, END)
        carloc.delete(0, END)
        caredate.delete(0, END) # Clear the end date field

    #under development!!!
    def returncar():
        root1 = Toplevel()
        root1.geometry("600x600")
        root1.title("RETURN CAR")
        lab = Label(root1, text="CARS TO BE RETURNED").pack()
        tree1 = ttk.Treeview(root1)
        tree1["show"] = "headings"
        s = ttk.Style(root1)
        s.theme_use("clam")
        tree1["columns"] = ("carid", "userid", "name", "email", "startdate")
        tree1.column("carid", width=70, minwidth=70, anchor=CENTER)
        tree1.column("userid", width=70, minwidth=70, anchor=CENTER)
        tree1.column("name", width=150, minwidth=150, anchor=CENTER)
        tree1.column("email", width=150, minwidth=150, anchor=CENTER)
        tree1.column("startdate", width=150, minwidth=150, anchor=CENTER)
        tree1.heading("carid", text="carid", anchor=CENTER)
        tree1.heading("userid", text="userid", anchor=CENTER)
        tree1.heading("name", text="name", anchor=CENTER)
        tree1.heading("email", text="email", anchor=CENTER)
        tree1.heading("startdate", text="startdate", anchor=CENTER)

        cur = con.cursor()
        cur.execute("SELECT car_id, user_id, name, email, startdate FROM manages NATURAL JOIN users NATURAL JOIN cars WHERE available='n'")
        i = 0
        for row in cur:
            tree1.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4]))
            i += 1
        con.commit()

        def rccar():
            s1 = bt1.get()
            s2 = bt2.get()
            s3 = bt3.get()

            # Ask for the return date from the user
            # Ask for the return date from the user
            # Ask for the return date from the user
            # Ask for the return date from the user
            return_date = simpledialog.askstring("Return Date", "Enter the return date (YYYY-MM-DD):")

            # Get the end date from the database
            cur = con.cursor()
            cur.execute("SELECT enddate FROM users WHERE user_id=%s", (s2,))
            end_date_str = cur.fetchone()[0]

            # Check if it's already a string or a datetime object
            if isinstance(end_date_str, datetime):
                end_date_db = end_date_str.date()
            else:
                end_date_db = datetime.strptime(end_date_str, '%Y-%m-%d %H:%M:%S').date()

            # Calculate the number of days overdue
            return_date = datetime.strptime(return_date, '%Y-%m-%d').date()
            overdue_days = max((return_date - end_date_db).days, 0)

            # Apply a fine of 20 rupees per day overdue
            fine_amount = 20 * overdue_days

            # Display the fine in the messagebox
            messagebox.showinfo("Fine Calculation", f"Fine for {overdue_days} days overdue: {fine_amount} rupees")


            # Update the database and inform the user
            cur = con.cursor()
            y = 'y'
            cur.execute("UPDATE cars SET available=%s WHERE car_id=%s", (y, s1))
            con.commit()
            cur.execute("DELETE FROM manages WHERE car_id=%s AND user_id=%s", (s1, s2))
            con.commit()
            messagebox.showinfo("Car Returned", "Thank you, come again!")
            b1.delete(0, END)
            b2.delete(0, END)
            b3.delete(0, END)


        bt1 = IntVar()
        bt2 = IntVar()
        bt3 = StringVar()

        l1 = Label(root1, text="CARID").place(x=210, y=270)
        b1 = Entry(root1, textvariable=bt1)
        b1.place(x=260, y=270)

        l2 = Label(root1, text="USERID").place(x=210, y=300)
        b2 = Entry(root1, textvariable=bt2)
        b2.place(x=260, y=300)

        l3 = Label(root1, text="NAME").place(x=210, y=330)
        b3 = Entry(root1, textvariable=bt3)
        b3.place(x=260, y=330)

        b4 = Button(root1, text="RETURN CAR", command=rccar).place(x=250, y=370)

        vsb = ttk.Scrollbar(root1, orient="vertical")
        vsb.configure(command=tree1.yview)
        tree1.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y, side=RIGHT)

        tree1.pack()
        root1.mainloop()



    lab4=Label(frame2,text="CARID").place(x=150,y=270)
    carbook=Entry(frame2,textvariable=ent4)
    carbook.place(x=200,y=270)

    lab5=Label(frame2,text="NAME").place(x=150,y=300)
    carname=Entry(frame2,textvariable=ent5)
    carname.place(x=200,y=300)

    lab6=Label(frame2,text="EMAIL").place(x=150,y=330)
    carmail=Entry(frame2,textvariable=ent6)
    carmail.place(x=200,y=330)

    lab7=Label(frame2,text="START DATE").place(x=150,y=360)
    carsdate=Entry(frame2,textvariable=ent7)
    carsdate.place(x=220,y=360)

    lab8=Label(frame2,text="LOCATION").place(x=150,y=390)
    carloc=Entry(frame2,textvariable=ent8)
    carloc.place(x=220,y=390)

    lab8=Label(frame2,text="END DATE").place(x=150,y=420)
    caredate=Entry(frame2,textvariable=ent9)
    caredate.place(x=220,y=420)

    but3=Button(frame2,text="BOOK CAR",command=bookcar).place(x=200,y=450)
    b10=Button(frame2,text="REFRESH",command=enter).place(x=200,y=480)

    la=Label(frame3,text="RETURN CAR PORTAL").place(x=190,y=10)
    but4=Button(frame3,text="GO TO RETURN CAR",command=returncar).place(x=200,y=100)


    #tree.pack()
    frame2.mainloop()
    root.mainloop()



def submit():
    c=0
    username=a.get()
    password=b.get()
    cur.execute("select *from admin")
    for i in cur:
        if i[0]==username and i[1]==password:
            global check
            c=1
            check=1
    if c==1:
        messagebox.showinfo("valid!","welcome!")
        enter()
    else:
        messagebox.showwarning("not valid!!","try again!")
def set_background(root, image_path):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo)
    label.image = photo
    label.place(x=0, y=0, relwidth=1, relheight=1)
    
r=Tk()
r.title("LOGIN CAR RENTAL SYSTEM")
r.geometry("500x500")


set_background(r, "C:\\Users\\lenovo\\OneDrive\\Desktop\\carpic.jpeg")

r.configure(bg="black")
s=ttk.Style(r)
s.theme_use("clam")
cur=con.cursor()
a=StringVar()
b=StringVar()
t=Label(r,text="CAR RENTAL ADMIN LOGIN").pack()
user=Label(r,text="USERNAME").place(x=150,y=150)
g=Entry(r,textvariable=a)
g.place(x=220,y=150)
passw=Label(r,text="PASSWORD").place(x=150,y=180)
h=Entry(r,textvariable=b)
h.place(x=220,y=180)
bo=Button(r,text="SUBMIT",command=submit)
bo.place(x=250,y=220)
#b5=Button(r,text="REFRESH",command=enter)
#b5.place(x=250,y=250)
con.commit()
r.mainloop()