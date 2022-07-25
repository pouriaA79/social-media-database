import tkinter as tk
from tkinter import *
from tkinter import ttk

import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="qanari")

cursor = conn.cursor()

def login():
    def logintodb(user, passw):
        Username.delete(0, END)
        password.delete(0, END)
        info = []
        info.append(user)
        info.append(passw)
        info.append("")
        arg = cursor.callproc("login", info)
        conn.commit()

        if arg[2] is None:
            root = tk.Tk()
            root.geometry("300x130")
            root.title("warning!!")

            root.eval('tk::PlaceWindow . center')
            label_frame = LabelFrame(root)
            label_frame.config(bg="cadet blue")
            label_frame.pack(expand='yes', fill='both')
            lblfrstrow = tk.Label(label_frame, text="password or username is wrong")
            lblfrstrow.place(x=60, y=50)
            lblfrstrow.config(bg='cadet blue')

            root.mainloop()
        else:
            root = tk.Tk()
            root.geometry("300x130")
            root.title("Welcome")

            root.eval('tk::PlaceWindow . center')
            label_frame = LabelFrame(root)
            label_frame.config(bg="cadet blue")
            label_frame.pack(expand='yes', fill='both')
            txt = "hello  " + arg[0]
            global login_id
            login_id = arg[2]
            lblfrstrow = tk.Label(label_frame, text=txt)
            lblfrstrow.place(x=100, y=50)
            lblfrstrow.config(bg='cadet blue')

            root.mainloop()

    def submitact():
        user = Username.get()
        passw = password.get()
        logintodb(user, passw)

    root = tk.Tk()
    root.geometry("300x130")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari Login Page")
    label_frame = LabelFrame(root, text="login page")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text="Username", )
    lblfrstrow.config(bg="cadet blue")

    lblfrstrow.place(x=50, y=20)

    Username = tk.Entry(label_frame, width=35)
    Username.place(x=130, y=20, width=80)

    lblsecrow = tk.Label(label_frame, text="Password")
    lblsecrow.config(bg="cadet blue")

    lblsecrow.place(x=50, y=50)

    password = tk.Entry(label_frame, width=35, show="*")
    password.place(x=130, y=50, width=80)

    submitbtn = tk.Button(label_frame, text="Login",
                          bg='pale green', command=submitact)
    submitbtn.place(x=130, y=80, width=55)

    root.mainloop()
def logincheck():
    def checkdb(user):
        Username.delete(0, END)
        info = []
        info.append(user)
        cursor.callproc("logincheck", info)

        for res in cursor.stored_results():
            data = res.fetchall()
        conn.commit()

        if len(data) == 0:
            root = tk.Tk()
            root.geometry("300x130")
            root.title("warning!!")

            root.eval('tk::PlaceWindow . center')
            label_frame = LabelFrame(root)
            label_frame.config(bg="cadet blue")
            label_frame.pack(expand='yes', fill='both')
            lblfrstrow = tk.Label(label_frame, text="password or username is wrong")
            lblfrstrow.place(x=60, y=50)
            lblfrstrow.config(bg='cadet blue')

            root.mainloop()
        else:
            root = tk.Tk()
            root.geometry("500x450")
            root.title("login records")
            root.eval('tk::PlaceWindow . center')
            label_frame = LabelFrame(root)
            label_frame.config(bg="khaki")
            label_frame.pack(expand='yes', fill='both')
            e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                      font=('Arial', 16, 'bold'))
            e.grid(row=0, column=0)
            e.insert(END, "username")
            e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                      font=('Arial', 16, 'bold'))
            e.grid(row=0, column=1)

            e.insert(END, "date")
            for i in range(len(data)):
                for j in range(2):
                    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                              font=('Arial', 16, 'bold'))
                    e.grid(row=i + 1, column=j)
                    e.insert(END, data[i][j])
            root.mainloop()

    def check_log():
        user = Username.get()
        checkdb(user)

    root = tk.Tk()
    root.geometry("300x130")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari Login Page")
    label_frame = LabelFrame(root, text="login check")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text="Username", )
    lblfrstrow.config(bg="cadet blue")

    lblfrstrow.place(x=50, y=20)

    Username = tk.Entry(label_frame, width=35)
    Username.place(x=130, y=20, width=80)

    submitbtn = tk.Button(label_frame, text="check",
                          bg='pale green', command=check_log)
    submitbtn.place(x=130, y=80, width=55)

    root.mainloop()
def avahaye_shakhsi():
    info = []
    info.append(login_id)
    cursor.callproc("daryaft_avaye_shakhsi", info)
    for res in cursor.stored_results():
        data = res.fetchall()
    root = tk.Tk()
    root.geometry("1200x600")
    root.title("avahaye shakhsi")
    # root.eval('tk::PlaceWindow . center')
    label_frame = LabelFrame(root)
    label_frame.config(bg="khaki")
    label_frame.pack(expand='yes', fill='both')
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=0)
    e.insert(END, "id ava")
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=1)
    e.insert(END, "mohtava")
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=2)
    e.insert(END, "date")
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=3)

    e.insert(END, "user id")
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=4)

    e.insert(END, "comment on ava")
    for i in range(len(data)):
        for j in range(5):
            e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                      font=('Arial', 16, 'bold'))
            e.grid(row=i + 1, column=j)
            if data[i][j] is None:
                e.insert(END, "")
            else:
                e.insert(END, data[i][j])
    root.mainloop()
def donbal_kardan():
    def follow(user_id):
        idd.delete(0, END)
        info = []
        info.append(login_id)
        info.append(user_id)
        cursor.callproc("donbal_kardan", info)
        print("follower_id  followed_id")
        conn.commit()

    def submitact():
        iddd = idd.get()
        follow(iddd)

    root = tk.Tk()
    root.geometry("300x130")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari UI")
    label_frame = LabelFrame(root, text="follow page")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text="user id", )
    lblfrstrow.config(bg="cadet blue")
    idd = tk.Entry(label_frame, width=35)
    idd.place(x=130, y=20, width=80)

    lblfrstrow.place(x=50, y=20)
    submitbtn = tk.Button(label_frame, text="submit",
                          bg='pale green', command=submitact)
    submitbtn.place(x=130, y=80, width=55)

    root.mainloop()
def tavaqof_donbal_kardan():
    def unfollow(user_id):
        idd.delete(0, END)
        info = []
        info.append(login_id)
        info.append(user_id)
        cursor.callproc("tavaqof_donbal_kardan", info)
        conn.commit()

    def submitact():
        iddd = idd.get()
        unfollow(iddd)

    root = tk.Tk()
    root.geometry("300x130")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari UI")
    label_frame = LabelFrame(root, text="unfollow page")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text="user id", )
    lblfrstrow.config(bg="cadet blue")
    idd = tk.Entry(label_frame, width=35)
    idd.place(x=130, y=20, width=80)

    lblfrstrow.place(x=50, y=20)
    submitbtn = tk.Button(label_frame, text="submit",
                          bg='pale green', command=submitact)
    submitbtn.place(x=130, y=80, width=55)

    root.mainloop()
def block():
    def unfollow(user_id):
        idd.delete(0, END)
        info = []
        info.append(login_id)
        info.append(user_id)
        cursor.callproc("block", info)
        conn.commit()

    def submitact():
        iddd = idd.get()
        unfollow(iddd)

    root = tk.Tk()
    root.geometry("300x130")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari UI")
    label_frame = LabelFrame(root, text="block page")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text="user id", )
    lblfrstrow.config(bg="cadet blue")
    idd = tk.Entry(label_frame, width=35)
    idd.place(x=130, y=20, width=80)

    lblfrstrow.place(x=50, y=20)
    submitbtn = tk.Button(label_frame, text="submit",
                          bg='pale green', command=submitact)
    submitbtn.place(x=130, y=80, width=55)

    root.mainloop()
def unblock():
    def unfollow(user_id):
        idd.delete(0, END)
        info = []
        info.append(login_id)
        info.append(user_id)
        cursor.callproc("unblock", info)
        conn.commit()

    def submitact():
        iddd = idd.get()
        unfollow(iddd)

    root = tk.Tk()
    root.geometry("300x130")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari UI")
    label_frame = LabelFrame(root, text="unblock page")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text="user id", )
    lblfrstrow.config(bg="cadet blue")
    idd = tk.Entry(label_frame, width=35)
    idd.place(x=130, y=20, width=80)

    lblfrstrow.place(x=50, y=20)
    submitbtn = tk.Button(label_frame, text="submit",
                          bg='pale green', command=submitact)
    submitbtn.place(x=130, y=80, width=55)

    root.mainloop()
def faaliat_donbal_shavandegan():
    info = []
    info.append(login_id)
    cursor.callproc("daryaft_faaliat_donbal_shavandegan", info)
    for res in cursor.stored_results():
        data = res.fetchall()
    root = tk.Tk()
    root.geometry("1200x600")
    root.title("faaliat donbal shavandegan")
    # root.eval('tk::PlaceWindow . center')
    label_frame = LabelFrame(root)
    label_frame.config(bg="khaki")
    label_frame.pack(expand='yes', fill='both')
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=0)
    e.insert(END, "id ava")
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=1)
    e.insert(END, "mohtava")
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=2)
    e.insert(END, "date")
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=3)

    e.insert(END, "user id")
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=4)

    e.insert(END, "comment on ava")
    for i in range(len(data)):
        for j in range(5):
            e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                      font=('Arial', 16, 'bold'))
            e.grid(row=i + 1, column=j)
            if data[i][j] is None:
                e.insert(END, "")
            else:
                e.insert(END, data[i][j])
    root.mainloop()
def faaliat_karbaran():
    def checkdb(user):
        Username.delete(0, END)
        info = []
        info.append(login_id)
        info.append(user)

        cursor.callproc("faaliat_karbaran", info)

        for res in cursor.stored_results():
            data = res.fetchall()
        conn.commit()

        root = tk.Tk()
        root.geometry("1200x600")
        root.title("faaliat karbaran")
        label_frame = LabelFrame(root)
        label_frame.config(bg="khaki")
        label_frame.pack(expand='yes', fill='both')
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=0)
        e.insert(END, "id ava")
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=1)
        e.insert(END, "mohtava")
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=2)
        e.insert(END, "date")
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=3)

        e.insert(END, "user id")
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=4)

        e.insert(END, "comment on ava")
        for i in range(len(data)):
            for j in range(5):
                e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                          font=('Arial', 16, 'bold'))
                e.grid(row=i + 1, column=j)
                if data[i][j] is None:
                    e.insert(END, "")
                else:
                    e.insert(END, data[i][j])
        root.mainloop()

    def check_log():
        user = Username.get()
        checkdb(user)

    root = tk.Tk()
    root.geometry("300x130")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari UI")
    label_frame = LabelFrame(root, text="falliat karbaran ")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text="user id", )
    lblfrstrow.config(bg="cadet blue")

    lblfrstrow.place(x=50, y=20)

    Username = tk.Entry(label_frame, width=35)
    Username.place(x=130, y=20, width=80)

    submitbtn = tk.Button(label_frame, text="check",
                          bg='pale green', command=check_log)
    submitbtn.place(x=130, y=80, width=55)

    root.mainloop()
def nazar_dadan():
    def unfollow(user_id, passw):
        user_id.delete(0, END)
        passw.delete(0, END)
        info = []
        info.append(login_id)
        info.append(user_id)
        info.append(passw)
        cursor.callproc("nazar_dadan", info)
        conn.commit()

    def submitact():
        user = Username.get()
        passw = password.get()
        unfollow(user, passw)

    root = tk.Tk()
    root.geometry("300x130")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari UI")
    label_frame = LabelFrame(root, text="comment page")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text="user id", )
    lblfrstrow.config(bg="cadet blue")
    lblfrstrow.place(x=50, y=20)
    Username = tk.Entry(label_frame, width=35)
    Username.place(x=130, y=20, width=80)

    lblsecrow = tk.Label(label_frame, text="comment")
    lblsecrow.config(bg="cadet blue")

    lblsecrow.place(x=50, y=50)

    password = tk.Entry(label_frame, width=35)
    password.place(x=130, y=50, width=80)

    submitbtn = tk.Button(label_frame, text="submit",
                          bg='pale green', command=submitact)
    submitbtn.place(x=130, y=80, width=55)

    root.mainloop()
def daryaft_comment():
    def checkdb(user):
        Username.delete(0, END)
        info = []
        info.append(login_id)
        info.append(user)

        cursor.callproc("daryaft_comment", info)

        for res in cursor.stored_results():
            data = res.fetchall()
        conn.commit()

        root = tk.Tk()
        root.geometry("1200x600")
        root.title("nazarat ava")
        label_frame = LabelFrame(root)
        label_frame.config(bg="khaki")
        label_frame.pack(expand='yes', fill='both')
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=0)
        e.insert(END, "id ava")
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=1)
        e.insert(END, "mohtava")
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=2)
        e.insert(END, "date")
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=3)

        e.insert(END, "user id")
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=4)

        e.insert(END, "comment on ava")
        for i in range(len(data)):
            for j in range(5):
                e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                          font=('Arial', 16, 'bold'))
                e.grid(row=i + 1, column=j)
                e.insert(END, data[i][j])
        root.mainloop()

    def check_log():
        user = Username.get()
        checkdb(user)

    root = tk.Tk()
    root.geometry("300x130")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari UI")
    label_frame = LabelFrame(root, text="nazarat ava ")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text="ava id", )
    lblfrstrow.config(bg="cadet blue")

    lblfrstrow.place(x=50, y=20)

    Username = tk.Entry(label_frame, width=35)
    Username.place(x=130, y=20, width=80)

    submitbtn = tk.Button(label_frame, text="check",
                          bg='pale green', command=check_log)
    submitbtn.place(x=130, y=80, width=55)

    root.mainloop()
def like_ava():
    def unfollow(user_id):
        idd.delete(0, END)
        info = []
        info.append(login_id)
        info.append(user_id)
        cursor.callproc("like_ava", info)
        conn.commit()

    def submitact():
        iddd = idd.get()
        unfollow(iddd)

    root = tk.Tk()
    root.geometry("300x130")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari UI")
    label_frame = LabelFrame(root, text="like page")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text="ava id", )
    lblfrstrow.config(bg="cadet blue")
    idd = tk.Entry(label_frame, width=35)
    idd.place(x=130, y=20, width=80)

    lblfrstrow.place(x=50, y=20)
    submitbtn = tk.Button(label_frame, text="submit",
                          bg='pale green', command=submitact)
    submitbtn.place(x=130, y=80, width=55)

    root.mainloop()
def num_like():
    def checkdb(user):
        Username.delete(0, END)
        info = []
        info.append(login_id)
        info.append(user)

        cursor.callproc("num_like", info)

        for res in cursor.stored_results():
            data = res.fetchall()
        conn.commit()

        root = tk.Tk()
        root.geometry("600x300")
        root.title("number like")
        label_frame = LabelFrame(root)
        label_frame.config(bg="khaki")
        label_frame.pack(expand='yes', fill='both')
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=0)
        e.insert(END, "count")

        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                          font=('Arial', 16, 'bold'))
        e.grid(row=11, column=0)
        e.insert(END, data[0][0])
        root.mainloop()

    def check_log():
        user = Username.get()
        checkdb(user)

    root = tk.Tk()
    root.geometry("300x130")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari UI")
    label_frame = LabelFrame(root, text="like number ")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text="ava id", )
    lblfrstrow.config(bg="cadet blue")

    lblfrstrow.place(x=50, y=20)

    Username = tk.Entry(label_frame, width=35)
    Username.place(x=130, y=20, width=80)

    submitbtn = tk.Button(label_frame, text="check",
                          bg='pale green', command=check_log)
    submitbtn.place(x=130, y=80, width=55)

    root.mainloop()
def avahaye_portarafdar():
    info = []
    info.append(login_id)
    cursor.callproc("avahaye_portarafdar", info)
    for res in cursor.stored_results():
        data = res.fetchall()
    root = tk.Tk()
    root.geometry("600x600")
    root.title("avahaye portarafdar")
    # root.eval('tk::PlaceWindow . center')
    label_frame = LabelFrame(root)
    label_frame.config(bg="khaki")
    label_frame.pack(expand='yes', fill='both')
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=0)
    e.insert(END, "id ava")
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=1)
    e.insert(END, "count")
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))

    for i in range(len(data)):
        for j in range(2):
            e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                      font=('Arial', 16, 'bold'))
            e.grid(row=i + 1, column=j)

            e.insert(END, data[i][j])
    root.mainloop()
def message_inbox_from_userx():
    def checkdb(user):
        Username.delete(0, END)
        info = []
        info.append(login_id)
        info.append(user)

        cursor.callproc("payamhaye_daryafti_karbar", info)

        for res in cursor.stored_results():
            data = res.fetchall()
        conn.commit()

        root = tk.Tk()
        root.geometry("1200x600")
        root.title("inbox")
        label_frame = LabelFrame(root)
        label_frame.config(bg="khaki")
        label_frame.pack(expand='yes', fill='both')
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=0)
        e.insert(END, "id ava")
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=1)
        e.insert(END, "mohtava")
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=2)
        e.insert(END, "sender id")
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=3)

        e.insert(END, "date")

        for i in range(len(data)):
            for j in range(4):
                e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                          font=('Arial', 16, 'bold'))
                e.grid(row=i + 1, column=j)
                if data[i][j] is None:
                    e.insert(END, "")
                else:
                    e.insert(END, data[i][j])
        root.mainloop()

    def check_log():
        user = Username.get()
        checkdb(user)

    root = tk.Tk()
    root.geometry("300x130")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari UI")
    label_frame = LabelFrame(root, text="message inbox ")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text="user id", )
    lblfrstrow.config(bg="cadet blue")

    lblfrstrow.place(x=50, y=20)

    Username = tk.Entry(label_frame, width=35)
    Username.place(x=130, y=20, width=80)

    submitbtn = tk.Button(label_frame, text="check",
                          bg='pale green', command=check_log)
    submitbtn.place(x=130, y=80, width=55)

    root.mainloop()
def ersal_konandegan_payam():
    info = []
    info.append(login_id)
    cursor.callproc("list_ersal_konandegan_payam", info)
    for res in cursor.stored_results():
        data = res.fetchall()
    root = tk.Tk()
    root.geometry("1200x600")
    root.title("message records")
    # root.eval('tk::PlaceWindow . center')
    label_frame = LabelFrame(root)
    label_frame.config(bg="khaki")
    label_frame.pack(expand='yes', fill='both')
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=0)
    e.insert(END, "sender id")
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=1)
    e.insert(END, "mohtava")
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=2)
    e.insert(END, "ava id")
    e = Entry(label_frame, width=20, fg='blue', bg="khaki",
              font=('Arial', 16, 'bold'))
    e.grid(row=0, column=3)

    e.insert(END, "date")

    for i in range(len(data)):
        for j in range(4):
            e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                      font=('Arial', 16, 'bold'))
            e.grid(row=i + 1, column=j)
            if data[i][j] is None:
                e.insert(END, "")
            else:
                e.insert(END, data[i][j])
    root.mainloop()
def list_pasankonandegan():
    def checkdb(user):
        Username.delete(0, END)
        info = []
        info.append(login_id)
        info.append(user)

        cursor.callproc("list_pasankonandegan", info)

        for res in cursor.stored_results():
            data = res.fetchall()
        conn.commit()

        root = tk.Tk()
        root.geometry("600x300")
        root.title("inbox")
        label_frame = LabelFrame(root)
        label_frame.config(bg="khaki")
        label_frame.pack(expand='yes', fill='both')
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=0)
        e.insert(END, "usernames")

        for i in range(len(data)):
            for j in range(1):
                e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                          font=('Arial', 16, 'bold'))
                e.grid(row=i + 1, column=j)
                if data[i][j] is None:
                    e.insert(END, "")
                else:
                    e.insert(END, data[i][j])
        root.mainloop()

    def check_log():
        user = Username.get()
        checkdb(user)

    root = tk.Tk()
    root.geometry("300x130")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari UI")
    label_frame = LabelFrame(root, text="pasand konandegan ")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text='ava id', )
    lblfrstrow.config(bg="cadet blue")

    lblfrstrow.place(x=50, y=20)

    Username = tk.Entry(label_frame, width=35)
    Username.place(x=130, y=20, width=80)

    submitbtn = tk.Button(label_frame, text="check",
                          bg='pale green', command=check_log)
    submitbtn.place(x=130, y=80, width=55)

    root.mainloop()
def avahaye_hashtag():
    def checkdb(user):
        Username.delete(0, END)
        info = []
        info.append(login_id)
        info.append(user)

        cursor.callproc("avahaye_hashtag", info)

        for res in cursor.stored_results():
            data = res.fetchall()
        conn.commit()

        root = tk.Tk()
        root.geometry("1200x600")
        root.title("list avaha")
        label_frame = LabelFrame(root)
        label_frame.config(bg="khaki")
        label_frame.pack(expand='yes', fill='both')
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=0)
        e.insert(END, "ava id")
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=1)
        e.insert(END, "mohtava")
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=2)
        e.insert(END, "post date")
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=3)
        e.insert(END, "user id")
        e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                  font=('Arial', 16, 'bold'))
        e.grid(row=0, column=4)
        e.insert(END, "comment on ava")

        for i in range(len(data)):
            for j in range(5):
                e = Entry(label_frame, width=20, fg='blue', bg="khaki",
                          font=('Arial', 16, 'bold'))
                e.grid(row=i + 1, column=j)
                if data[i][j] is None:
                    e.insert(END, "")
                else:
                    e.insert(END, data[i][j])
        root.mainloop()

    def check_log():
        user = Username.get()
        checkdb(user)

    root = tk.Tk()
    root.geometry("300x130")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari UI")
    label_frame = LabelFrame(root, text="hashtags ")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text='hashtag id', )
    lblfrstrow.config(bg="cadet blue")

    lblfrstrow.place(x=50, y=20)

    Username = tk.Entry(label_frame, width=35)
    Username.place(x=130, y=20, width=80)

    submitbtn = tk.Button(label_frame, text="check",
                          bg='pale green', command=check_log)
    submitbtn.place(x=130, y=80, width=55)

    root.mainloop()
def add_user():
    def logintodb(f,l,user, passw,bir,bio):
        Username.delete(0, END)
        password.delete(0, END)
        birthday.delete(0, END)
        biography.delete(0, END)
        fName.delete(0, END)
        lName.delete(0, END)
        info = []
        info.append(f)
        info.append(l)
        info.append(user)
        info.append(passw)
        info.append(bir)
        info.append(bio)
        cursor.callproc("add_user", info)
        conn.commit()


        root.mainloop()

    def submitact():
        f = fName.get()
        l = lName.get()
        bi = biography.get()
        bir = birthday.get()
        user = Username.get()
        passw = password.get()
        logintodb(f,l,user, passw,bir,bi)

    root = tk.Tk()
    root.geometry("300x300")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari add User Page")
    label_frame = LabelFrame(root, text="Register")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow1 = tk.Label(label_frame, text="First name", )
    lblfrstrow1.config(bg="cadet blue")

    lblfrstrow1.place(x=50, y=20)

    fName = tk.Entry(label_frame, width=35)
    fName.place(x=130, y=20, width=80)

    lblsecrow1 = tk.Label(label_frame, text="Last name")
    lblsecrow1.config(bg="cadet blue")

    lblsecrow1.place(x=50, y=50)

    lName = tk.Entry(label_frame, width=35)
    lName.place(x=130, y=50, width=80)
    lblfrstrow2 = tk.Label(label_frame, text="Username", )
    lblfrstrow2.config(bg="cadet blue")

    lblfrstrow2.place(x=50, y=80)

    Username = tk.Entry(label_frame, width=35)
    Username.place(x=130, y=80, width=80)

    lblsecrow2 = tk.Label(label_frame, text="Password")
    lblsecrow2.config(bg="cadet blue")

    lblsecrow2.place(x=50, y=110)

    password = tk.Entry(label_frame, width=35)
    password.place(x=130, y=110, width=80)
    lblfrstrow3 = tk.Label(label_frame, text="birthday", )
    lblfrstrow3.config(bg="cadet blue")

    lblfrstrow3.place(x=50, y=140)

    birthday = tk.Entry(label_frame, width=35)
    birthday.place(x=130, y=140, width=80)

    lblsecrow3 = tk.Label(label_frame, text="biography")
    lblsecrow3.config(bg="cadet blue")

    lblsecrow3.place(x=50, y=170)

    biography = tk.Entry(label_frame, width=35)
    biography.place(x=130, y=170, width=80)


    submitbtn = tk.Button(label_frame, text="Register",
                          bg='pale green', command=submitact)
    submitbtn.place(x=130, y=200, width=55)

    root.mainloop()
def add_ava():
    def checkdb(user):
        Username.delete(0, END)
        info = []
        info.append(login_id)
        info.append(user)

        cursor.callproc("add_ava", info)

        conn.commit()


        root.mainloop()

    def check_log():
        user = Username.get()
        checkdb(user)

    root = tk.Tk()
    root.geometry("300x130")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari add ava UI")
    label_frame = LabelFrame(root, text="add ava")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text="mohtava", )
    lblfrstrow.config(bg="cadet blue")

    lblfrstrow.place(x=50, y=20)

    Username = tk.Entry(label_frame, width=35)
    Username.place(x=130, y=20, width=150)

    submitbtn = tk.Button(label_frame, text="add",
                          bg='pale green', command=check_log)
    submitbtn.place(x=130, y=80, width=55)

    root.mainloop()
def add_hashtag():
    def logintodb(user, user1, passw):
        Username.delete(0, END)
        Username1.delete(0, END)
        password.delete(0, END)
        info = []
        info.append(login_id)
        info.append(user)
        info.append(user1)
        info.append(passw)

        cursor.callproc("aadd_hashtag", info)
        conn.commit()

    def submitact():
        user = Username.get()
        user1 = Username1.get()
        passw = password.get()
        logintodb(user,user1, passw)

    root = tk.Tk()
    root.geometry("300x180")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari add # Page")
    label_frame = LabelFrame(root, text="add #")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow = tk.Label(label_frame, text="mohtava", )
    lblfrstrow.config(bg="cadet blue")

    lblfrstrow.place(x=50, y=20)

    Username = tk.Entry(label_frame, width=35)
    Username.place(x=160, y=20, width=100)

    lblfrstrow1 = tk.Label(label_frame, text="comment on ava", )
    lblfrstrow1.config(bg="cadet blue")

    lblfrstrow1.place(x=50, y=50)

    Username1 = tk.Entry(label_frame, width=35)
    Username1.place(x=160, y=50, width=100)

    lblsecrow = tk.Label(label_frame, text="hashtag")
    lblsecrow.config(bg="cadet blue")

    lblsecrow.place(x=50, y=80)

    password = tk.Entry(label_frame, width=35)
    password.place(x=160, y=80, width=100)

    submitbtn = tk.Button(label_frame, text="add",
                          bg='pale green', command=submitact)
    submitbtn.place(x=160, y=110, width=55)

    root.mainloop()
def send_message():
    def logintodb(r, d, av,mo):
        rec.delete(0, END)
        dat.delete(0, END)
        ava.delete(0, END)
        moh.delete(0, END)

        info = []
        info.append(login_id)
        info.append(d)
        info.append(r)
        info.append(av)
        if av=="":
            info.append(2)
        elif mo=="":
            info.append(1)
        info.append(mo)
        cursor.callproc("send_message", info)
        conn.commit()
        root.mainloop()
    def submitact():
        recc = rec.get()
        datt = dat.get()
        avaa = ava.get()
        mohh = moh.get()
        logintodb(recc, datt, avaa, mohh)

    root = tk.Tk()
    root.geometry("300x300")
    root.eval('tk::PlaceWindow . center')
    root.title("qanari send Message Page")
    label_frame = LabelFrame(root, text="send Messge")
    label_frame.config(bg="cadet blue")
    label_frame.pack(expand='yes', fill='both')

    # Definging the first row
    lblfrstrow1 = tk.Label(label_frame, text="date", )
    lblfrstrow1.config(bg="cadet blue")

    lblfrstrow1.place(x=50, y=20)

    dat = tk.Entry(label_frame, width=35)
    dat.place(x=180, y=20, width=80)

    lblsecrow1 = tk.Label(label_frame, text="ava id")
    lblsecrow1.config(bg="cadet blue")

    lblsecrow1.place(x=50, y=50)

    ava = tk.Entry(label_frame, width=35)
    ava.place(x=180, y=50, width=80)
    lblfrstrow2 = tk.Label(label_frame, text="receiver id", )
    lblfrstrow2.config(bg="cadet blue")

    lblfrstrow2.place(x=50, y=80)

    rec = tk.Entry(label_frame, width=35)
    rec.place(x=180, y=80, width=80)

    lblsecrow2 = tk.Label(label_frame, text="mohtavaye matni")
    lblsecrow2.config(bg="cadet blue")

    lblsecrow2.place(x=50, y=110)

    moh = tk.Entry(label_frame, width=35)
    moh.place(x=180, y=110, width=80)

    submitbtn = tk.Button(label_frame, text="send",
                          bg='pale green', command=submitact)
    submitbtn.place(x=180, y=200, width=55)

    root.mainloop()


def choice(event):

    decide = event.widget.get()
    if decide == str(1):
        login()
    elif decide == str(2):
        logincheck()
    elif decide == str(3):
        avahaye_shakhsi()
    elif decide == str(4):
        donbal_kardan()
    elif decide == str(5):
        tavaqof_donbal_kardan()
    elif decide == str(6):
        block()
    elif decide == str(7):
        unblock()
    elif decide == str(8):
        faaliat_donbal_shavandegan()
    elif decide == str(9):
        faaliat_karbaran()
    elif decide == str(10):
        nazar_dadan()
    elif decide == str(11):
        daryaft_comment()
    elif decide == str(12):
        like_ava()
    elif decide == str(13):
        num_like()
    elif decide == str(14):
        avahaye_portarafdar()
    elif decide == str(15):
        message_inbox_from_userx()
    elif decide == str(16):
        ersal_konandegan_payam()
    elif decide == str(18):
        list_pasankonandegan()
    elif decide == str(19):
        avahaye_hashtag()
    elif decide ==str(20):
        add_user()
    elif decide == str(21):
        add_ava()
    elif decide == str(22):
        add_hashtag()
    elif decide ==str(17):
        send_message()







def main():
    root = tk.Tk()
    root.geometry("500x750")
    root.title("qanari")

    label_frame = LabelFrame(root, text='what do you want ')
    label_frame.config(bg="alice blue")
    label_frame.pack(expand='yes', fill='both')

    label1 = Label(label_frame, text='1. login.')
    label1.config(bg="alice blue")
    label1.place(x=0, y=5)

    label2 = Label(label_frame, text='2. logincheck.')
    label2.config(bg="alice blue")
    label2.place(x=0, y=35)

    label3 = Label(label_frame, text='3. daryaft avaye shakhsi.')
    label3.config(bg="alice blue")
    label3.place(x=0, y=65)

    label4 = Label(label_frame, text='4. donbal kardan.')
    label4.config(bg="alice blue")
    label4.place(x=0, y=95)

    label5 = Label(label_frame, text='5. tavaqof donbal kardan.')
    label5.config(bg="alice blue")
    label5.place(x=0, y=125)

    label6 = Label(label_frame, text='6. block.')
    label6.config(bg="alice blue")
    label6.place(x=0, y=155)

    label7 = Label(label_frame, text='7. unblock.')
    label7.config(bg="alice blue")
    label7.place(x=0, y=185)

    label8 = Label(label_frame, text='8. daryaft faaliat donbal shavandegan.')
    label8.config(bg="alice blue")
    label8.place(x=0, y=215)

    label9 = Label(label_frame, text='9. daryaft faaliat karbaran (motefavet ba sql)!!!!!!!!!!!.')
    label9.config(bg="alice blue")
    label9.place(x=0, y=245)

    label10 = Label(label_frame, text='10. comment.')
    label10.config(bg="alice blue")
    label10.place(x=0, y=275)

    label11 = Label(label_frame, text='11. daryaft comment.')
    label11.config(bg="alice blue")
    label11.place(x=0, y=305)

    label12 = Label(label_frame, text='12. like ava .')
    label12.config(bg="alice blue")
    label12.place(x=0, y=335)

    label13 = Label(label_frame, text='13. number of like .')
    label13.config(bg="alice blue")
    label13.place(x=0, y=365)

    label14 = Label(label_frame, text='14. avahaye portarafdar.')
    label14.config(bg="alice blue")
    label14.place(x=0, y=395)

    label15 = Label(label_frame, text='15. payamhaye daryafti karbar.')
    label15.config(bg="alice blue")
    label15.place(x=0, y=425)

    label16 = Label(label_frame, text='16. list ersal konandegan payam.')
    label16.config(bg="alice blue")
    label16.place(x=0, y=455)

    label17 = Label(label_frame, text='17. send message.')
    label17.config(bg="alice blue")
    label17.place(x=0, y=485)

    label18 = Label(label_frame, text='18. list pasan konandegan.')
    label18.config(bg="alice blue")
    label18.place(x=0, y=515)

    label19 = Label(label_frame, text='19. avahaye hashtag.')
    label19.config(bg="alice blue")
    label19.place(x=0, y=545)

    label20 = Label(label_frame, text='20. add new user.')
    label20.config(bg="alice blue")
    label20.place(x=0, y=575)

    label21 = Label(label_frame, text='21. add ava.')
    label21.config(bg="alice blue")
    label21.place(x=0, y=605)

    label22 = Label(label_frame, text='22. add hashtag   (different).')
    label22.config(bg="alice blue")
    label22.place(x=0, y=635)

    vlist = []
    for i in range(1, 23):
        vlist.append(str(i))

    Combo = ttk.Combobox(label_frame, values=vlist, state="readonly")
    Combo.set("choose an option")
    # Combo.current("choose option")
    Combo.place(x=201, y=5)
    Combo.bind("<<ComboboxSelected>>", choice)
    root.mainloop()


if __name__ == "__main__":
    main()
