from tkinter import *
import sqlite3,sys

def connection():

    try:
        conn=sqlite3.connect("restaurant.db")
    except:
        print("cannot connect to the database")
    return conn

def _verify_():

    a=b=c=d=0
    if not customer_name.get():
        t1.insert(END,"name is required\n")
        a=1

    if not phone_no.get():
        t1.insert(END,"phone number is required\n")
        b=1

    if not room_no.get():
        t1.insert(END,"room number is required\n")
        c=1

    if not address.get():
        t1.insert(END,"address is required")
        d=1

    if a==1 or b==1 or c==1 or d==1:
        return 1
    else:
        return 0

def _add_():

    ret = _verify_()
    if ret == 0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS CUSTOMERS(NAME TEXT,PHONE_NO INTEGER,ROOM_NO INTEGER,ADDRESS TEXT)")
        cur.execute("insert into CUSTOMERS values(?,?,?,?)",(customer_name.get(),int(phone_no.get()),int(room_no.get()),address.get()))
        conn.commit()
        conn.close()
        t1.insert(END,"\nADDED SUCCESSFULLY\n")

def _view_():

    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from CUSTOMERS")
    data=cur.fetchall()
    conn.close()

    for i in data:
        t1.insert(END,str(i)+"\n")

def _delete_():

    ret=_verify_()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM CUSTOMERS WHERE ROOM_NO=?",(int(room_no.get()),))
        conn.commit()
        conn.close()
        t1.insert(END,"\nUPDATED SUCCESSFULLY\n")

def close():
    sys.exit()

def clear():
    t1.delete('1.0',END)

if __name__=="__main__":
    root=Tk()
    root.title("Hotel Management System")

    customer_name=StringVar()
    room_no=StringVar()
    phone_no=StringVar()
    address=StringVar()

    l1=Label(root,text="Customer name")
    l1.place(x=0,y=0)

    l2=Label(root,text="Phone number")
    l2.place(x=0,y=30)

    l3=Label(root,text="Room number")
    l3.place(x=0,y=60)
    l4=Label(root,text="Address")
    l4.place(x=0,y=90)


    e1=Entry(root,textvariable=customer_name)
    e1.place(x=100,y=0)

    e2=Entry(root,textvariable=phone_no)
    e2.place(x=100,y=30)

    e3=Entry(root,textvariable=room_no)
    e3.place(x=100,y=60)

    e4=Entry(root,textvariable=address)
    e4.place(x=100,y=90)

    t1=Text(root,width=80,height=20)
    t1.grid(row=0,column=1)


    b1=Button(root,text="ADD CUSTOMER",command=_add_,width=40)
    b1.grid(row=11,column=0)

    b2=Button(root,text="VIEW ALL CUSTOMERS",command=_view_,width=40)
    b2.grid(row=12,column=0)

    b3=Button(root,text="DELETE CUSTOMER",command=_delete_,width=40)
    b3.grid(row=13,column=0)

    b4=Button(root,text="CLOSE",command=close,width=40)
    b4.grid(row=14,column=0)

    b5=Button(root,text="CLEAR",command=clear,width=40)
    b5.grid(row=15,column=0)

    root.mainloop()
