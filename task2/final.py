#   for login
# use user name :- subzz
# use password :- password123

from tkinter import *
from tkinter import messagebox
import sqlite3


def fun():
    uss=us.get()
    pss=pswd.get()
    if(uss==us1 and pss==pswd1) :
        def no1():
            def no2():
                mpps = m_pps.get()
                mbee = m_bee.get()
                mphy = m_phy.get()
                mmath = m_math.get()
                avg = (mpps + mbee + mphy + mmath) / 4
                cgp = 0.105 * avg
                def close():
                    gui.destroy()

                def cgpa():
                    #cgp = 0.105 * avg
                    label = Label(gui_3, text=cgp)
                    label.grid(row=1, column=2)

                def grade():
                    if cgp>=9:
                        grd='O'
                    elif cgp>=8:
                        grd='E'
                    elif cgp>=7:
                        grd='A'
                    elif cgp>=6:
                        grd='B'
                    elif cgp>=5:
                        grd='C'
                    elif cgp>=4:
                        grd='D'
                    else:
                        grd='F'
                    lbl=Label(gui_3,text=grd)
                    lbl.grid(row=2,column=2)

                def n_input():
                    no1()
                con = sqlite3.connect('database.db')
                c = con.cursor()
                c.execute("INSERT INTO student VALUES (:nm,:br,:ref,:m_pps,:m_bee,:m_phy,:m_math)",
                          {
                              'nm': nm.get(),
                              'br': br.get(),
                              'ref': ref.get(),
                              'm_pps': m_pps.get(),
                              'm_bee': m_bee.get(),
                              'm_phy': m_phy.get(),
                              'm_math': m_math.get()
                          })
                con.commit()
                con.close()
                gui_3=Toplevel()
                gui_3.geometry("400x250")
                gui_3.title("students result")
                b4 = Button(gui_3, text="CGPA", fg="green",command=cgpa).grid(row=1, column=1)
                b4 = Button(gui_3, text="GRADE", fg="green",command=grade).grid(row=2, column=1)
                b4 = Button(gui_3, text="NEW INPUT", fg="green",command=n_input).grid(row=4, column=1)
                b4 = Button(gui_3, text="CLOSE", fg="green", command=close).grid(row=4, column=6)




                gui_3.mainloop()

            gui_2=Toplevel()
            def ent0():
                e3 = Entry(gui_2, textvariable=m_pps).grid(row=0, column=1)
            def ent1():
                e3 = Entry(gui_2, textvariable=m_bee).grid(row=1, column=1)

            def ent2():
                e3 = Entry(gui_2, textvariable=m_phy).grid(row=2, column=1)

            def ent3():
                e3 = Entry(gui_2, textvariable=m_math).grid(row=3, column=1)

            gui_2.geometry("400x300")
            gui_2.title("students marks")

            b3 = Button(gui_2, text="PPS", fg='pink', command=ent0).grid(row=0, sticky=W)
            b3 = Button(gui_2, text="BEE", fg='pink', command=ent1).grid(row=1, sticky=W)
            b3 = Button(gui_2, text="PHYSICS", fg='pink', command=ent2).grid(row=2, sticky=W)
            b3 = Button(gui_2, text="MATHS", fg='pink', command=ent3).grid(row=3, sticky=W)

            b3 = Button(gui_2, text="SUBMIT", fg='blue', command=no2).grid(row=5, column=1)
            gui_2.mainloop()


        gui1=Toplevel()
        gui1.geometry("400x250")
        gui1.title("student details")

        Label(gui1, text="Name").grid(row=0, sticky=W)
        Label(gui1, text="Branch").grid(row=1, sticky=W)
        Label(gui1, text="Registration ID").grid(row=2, sticky=W)

        e2 = Entry(gui1, textvariable=nm)
        e2.grid(row=0, column=1)
        e3 = Entry(gui1, textvariable=br)
        e3.grid(row=1, column=1)
        e4 = Entry(gui1, textvariable=ref)
        e4.grid(row=2, column=1)
        b2 = Button(gui1, text="SUBMIT", fg='blue', command=no1).grid(row=4, column=1)


        gui1.mainloop()

    else:
        messagebox.showerror("error", "invalid username and password")


# login gui
gui = Tk()

gui.geometry("500x500")
gui.title("login page")

# variable declaration
us = StringVar()
pswd = StringVar()
us1 = 'subzz'
pswd1 = 'password123'
nm = StringVar()
br = StringVar()
ref = StringVar()
m_pps = DoubleVar()
m_phy = DoubleVar()
m_bee = DoubleVar()
m_math = DoubleVar()

Label(gui,text="user name:- subzz and password :- password123").grid(row=0,sticky=W)
Label(gui, text="User Name").grid(row=1, sticky=W)
Label(gui, text="Password").grid(row=2, sticky=W)

e1 = Entry(gui, textvariable=us).grid(row=1, column=1)
e1 = Entry(gui, textvariable=pswd).grid(row=2, column=1)

b1 = Button(gui, text="SUBMIT", fg='blue', command=fun).grid(row=5, column=1)



gui.mainloop()
