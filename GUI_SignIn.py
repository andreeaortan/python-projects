
""" This is a program with a GUI made with the Tkinter module that allows the user to LogIn or create a new account.
All the information will pe stored in a MySQL databases and the user will also get a confirmation email
"""

from tkinter import *
import mysql.connector

window = Tk()

def click_up():
    # connect to mysql
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="0000",
    )
    cursor = db.cursor()


    #create database and table
    cursor.execute("CREATE DATABASE IF NOT EXISTS signin")
    cursor.execute("USE signin")
    cursor.execute("CREATE TABLE IF NOT EXISTS users(name VARCHAR(250), username VARCHAR(250), email VARCHAR(250), password VARCHAR(250))")

    #insert values
    cursor.execute("INSERT INTO users(name,username,email,password) VALUES(%s,%s,%s,%s)",(name.get(),username_signup.get(),email.get(),password_signup.get()))
    db.commit()


    #sending confrm email
    import smtplib

    reciver = email.get()
    usrn = #INSERT email address
    psw = #INSERT email password

    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

    smtpserver.starttls()
    smtpserver.login(usrn, psw)
    message = "Congrats! You created an account. "
    smtpserver.sendmail(usrn, reciver, message)

    name.delete(0,END)
    username_signup.delete(0, END)
    email.delete(0, END)
    password_signup.delete(0, END)
    window2 = Tk()
    congrats_label = Label(window2, text="Congratualations! You created an account. Verify your email for confirmation.")
    congrats_label.grid(row=5,column=5)
    window2.mainloop()

def click_in():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="0000",
    )
    cursor = db.cursor()
    cursor.execute("USE signin")
    cursor.execute("SELECT username FROM users")
    usernames = {u[0] for u in cursor.fetchall()}
    if username_signin.get() in usernames:
        cursor.execute("SELECT password FROM users")
        passwords = {p[0] for p in cursor.fetchall()}
        if password_signin.get() in passwords:
            loggedin = Tk()
            succes=Label(loggedin,text="You are logged in! ")
            succes.grid(row=4,column=4)

        else:
            fail = Tk()
            failed = Label(fail, text="Username or Password incorect! ")
            failed.grid(row=4, column=4)
    else:
        fail = Tk()
        failed = Label(fail, text="Username or Password incorect! ")
        failed.grid(row=4, column=4)

def sign_in():
    global username_signin, password_signin
    windowi= Tk()
    window.destroy()
    username_signin= Entry(windowi)
    username_signin.grid(row=0, column=2)
    password_signin= Entry(windowi)
    password_signin.grid(row=1, column=2)
    username_signin_l = Label(windowi, text="Username",width=30)
    username_signin_l.grid(row=0,column=1)
    password_signin_l = Label(windowi, text="Password",width=30)
    password_signin_l.grid(row=1,column=1)
    login_btn = Button(windowi, text="Log in", width=30,command=click_in)
    login_btn.grid(row=5,column=2)

def sign_up():
    global name, username_signup, email, password_signup
    windowu=Tk()
    windowu.geometry("450x450")
    window.destroy()
    name = Entry(windowu)
    name.grid(row=0, column=2)
    username_signup = Entry(windowu)
    username_signup.grid(row=1, column=2)
    email = Entry(windowu)
    email.grid(row=2, column=2)
    password_signup = Entry(windowu)
    password_signup.grid(row=3, column=2)

    name_label = Label(windowu, text="Name")
    name_label.grid(row=0, column=1)
    username_label = Label(windowu, text="Username")
    username_label.grid(row=1, column=1)
    email_label = Label(windowu, text="Email")
    email_label.grid(row=2, column=1)
    password_label = Label(windowu, text="Password")
    password_label.grid(row=3, column=1)

    submit_button = Button(windowu, text="Create account", command=click_up)
    submit_button.grid(row=4, column=2)


def main():

    window.geometry("450x150")
    hello_label = Label(window,text="Welcome to this amazing website! :)")
    hello_label.grid(row=2, column=2)
    singin_btn = Button(window, text="Log in", width=20, bg="#fadadd", command=sign_in)
    singin_btn.grid(row=4, column=3,padx=30, pady=50)
    signup_btn = Button(window, text="Create an account", width=20, bg="#fadadd", command=sign_up)
    signup_btn.grid(row=4, column=2, padx=30, pady=50)


    window.mainloop()

main()
