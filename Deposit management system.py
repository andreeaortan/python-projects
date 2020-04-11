"""Program that keeps track of everything that comes in or goes out of the deposit using OOP
   - it also sends warning emails when the stock is too low for a product
   - it sends an email with the product's file if you want to
"""
from datetime import datetime
from datetime import date


class Stoc():

    def __init__(self, denp, categ, pret, um='Buc',sold=0, limita=5):
        self.denp = denp
        self.categ = categ
        self.um = um
        self.sold = sold
        self.limita = limita
        self.pret=pret
        self.dd = {}
        self.di = {}
        self.do = {}

    def intrari(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        self.cant = cant
        self.data = data
        if self.dd.keys():
            cheie = max(self.dd.keys()) + 1
        else:
            cheie = 1
        self.dd[cheie] = self.data
        self.di[cheie] = self.cant
        self.sold += self.cant

    def iesiri(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        self.cant = cant
        self.data = data
        if self.dd.keys():
            cheie = max(self.dd.keys()) + 1
        else:
            cheie = 1
        self.dd[cheie] = self.data
        self.do[cheie] = self.cant
        self.sold -= self.cant

    def fisap(self):
        self.lista_afis = []
        print(36 * '-')
        print('Product {0}, um {1}'.format(self.denp, self.um))
        print(36 * '-')
        self.b = ' Nrc    Date    Entry   Exit'
        print(self.b)
        print(36 * '-')
        for elem in self.dd.keys():
            if elem in self.di.keys():
                self.a = "{} {} {} {}".format(str(elem).rjust(5), self.dd[elem], str(self.di[elem]).rjust(7),
                                              str(0).rjust(6))
                print(self.a)
                self.lista_afis.append(self.a)
            else:
                self.a = "{} {} {} {}".format(str(elem).rjust(5), self.dd[elem], str(0).rjust(7),
                                              str(self.do[elem]).rjust(6))
                print(self.a)
                self.lista_afis.append(self.a)

        print(36 * '-')
        print('Final sold:', self.sold)
    def profit(self):
        self.chel=0
        self.venit=0
        for i in self.di:
            self.chel=self.pret*self.di[i]
        print(self.chel)
        for i in self.do:
            self.castig=self.pret*self.do[i]
        print(self.castig)
        if self.castig < self.chel:
            self.pierdere=self.castig-self.chel
            print("You have a loss of ",self.pierdere)
        else:
            self.venit=self.castig-self.chel
            print("You have a profit of ",self.venit)



    def trimt_mail(self):
        f = open("fisaprod.txt", "w")
        for i in listap:
            f.write('\t' + i.denp)
            f.write('\n')
            f.write(i.b)
            f.write('\n')
            for j in i.lista_afis:
                line = j
                f.write(line)
                f.write('\n')
        f.close()
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders

        reciver = input("RECIVER EMAIL")
        username = input("YOUR EMAIL")
        password = input("YOUR PASSWORD ")

        msg = MIMEMultipart()
        msg['Subject'] = "Product's file"
        body = "In this email you have attached the product's file"

        msg.attach(MIMEText(body, 'plain'))
        filename = "fisaprod.txt"
        attachment = open("fisaprod.txt", "rb")

        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        text = msg.as_string()

        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.starttls()
        smtpserver.login(username, password)
        smtpserver.sendmail(username, reciver, text)


listap = []
listaden = []
rosie = Stoc("Tomato", "vegetable",3.5, "kg", limita=10)
listap.append(rosie)
listaden.append(rosie.denp)
rosie.intrari(20, "2019-04-23")
rosie.intrari(10, "2019-04-30")
rosie.intrari(5, "2019-05-01")

rosie.iesiri(5, "2019-05-10")
rosie.iesiri(28, "2019-06-01")
rosie.profit()

cartof = Stoc("Potato", "vegetable", "kg", limita=7)
listap.append(cartof)
listaden.append(cartof.denp)

cartof.intrari(100, "2019-04-23")
cartof.intrari(20, "2019-05-05")

cartof.iesiri(78, "2019-05-02")
banana = Stoc("Banana", "fruit", 'kg')
listap.append(banana)
listaden.append(banana.denp)

banana.intrari(50, "2019-04-23")
banana.intrari(10, "2019-04-30")

banana.iesiri(40, "2019-05-21")
banana.iesiri(16, "2019-06-10")

capsuna = Stoc("Starwberries", "fruit", "kg")
listap.append(capsuna)
listaden.append(capsuna.denp)

capsuna.intrari(20, "2018-06-05")
capsuna.intrari(20, "2019-06-30")

capsuna.iesiri(25, "2019-06-23")
capsuna.iesiri(2, "2019-07-01")
rosie.exp("2020-01-01")
rosie.fisap()
cartof.fisap()
banana.fisap()
capsuna.fisap()

optiune = input("Do you want to send an email with the product's file? [y/n]").lower()
if optiune == 'y':
    cartof.trimt_mail()


import smtplib

reciver = input("RECIVER EMAIL")
username = input("YOUR EMAIL")
password = input("YOUR PASSWORD ")

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.starttls()
smtpserver.login(username, password)

for i in listap:

    message = """
    WARNING!
    Bring more supplies of: {}.
    The stock touched the limit of {} {}
    """.format(i.denp, i.limita, i.um)
    if i.sold < 5:
        smtpserver.sendmail(username, reciver, message)
        print("The message was sent successfully!")

import re

optiune1 = input("Are you searching for a product? [y/n]").lower()
if optiune1 == 'y':
    a = input("Product's name: ").capitalize()

    for i in listaden:
        for j in listap:
            if i == j.denp:
                z = re.match(a, i)
                if z:
                    print(
                        " All the information about the product:\n Name: {}\n Measure unit: {}\n Stock available: {}{}".format(
                            i, j.um, j.sold, j.um))



