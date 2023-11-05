from datetime import time
from random import random
from tkinter import *
from tkinter import messagebox, filedialog
import random
import datetime
import datetime

from django.contrib.sites import requests


def send():
    if textR.get(1.0, END) == '\n':
        pass
    else:
        def send_msg():
            message = textarea.get(1.0, END)
            number = numberfield.get()
            auth = ''
            url = ''

            params = {
                'authorization': auth,
                'message': message,
                'numbers': number,
                'sender-id': '',
                'route': 'p',
                'language': 'english'
            }
            response = requests.get(url, params=params)
            dic = response.json()
            result = dic.get('return')
            if result == True:
                messagebox.showinfo('Send Successfully', 'Message sent succesfully')

            else:
                messagebox.showerror('Error', 'Something went wrong')

        root2 = Toplevel()

        root2.title("Send Bill")
        root2.config(bg='orange')
        root2.geometry('485x620+50+50')

        logoImage = PhotoImage(file='Img.jpg')
        label = Label(root2, image=logoImage, bg='red4')
        label.pack(pady=5)

        numberLabel = Label(root2, text='Mobile Number', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
        numberLabel.pack(pady=5)

        numberfield = Entry(root2, font=('helvetica', 22, 'bold'), bd=3, width=24)
        numberfield.pack(pady=5)

        billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
        billLabel.pack(pady=5)

        textarea = Text(root2, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
        textarea.pack(pady=5)
        textarea.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n\n')

        if costofVeg.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Veg\t\t\t{priceofVeg}Rs\n')
        if costofNonveg.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Non\t\t\t{priceofNonVeg}Rs\n')
        if costofDrinks.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n')

        textarea.insert(END, f'Sub Total\t\t\t{subtotals}Rs\n')
        textarea.insert(END, f'Service Tax\t\t\t{256}Rs\n')
        textarea.insert(END, f'Total Cost\t\t\t{subtotals + 256}Rs\n')

        sendButton = Button(root2, text='SEND', font=('arial', 19, 'bold'), bg='white', fg='red4', bd=7, relief=GROOVE
                            , command=send_msg)
        sendButton.pack(pady=5)

        root2.mainloop()


def receipt():
    global billnumber, date
    if costofNonveg.get() != '' or costofVeg.get() != '' or costofDrinks.get() != '':
        textR.delete(1.0, END)
        x = random.randint(100, 10000)
        billnumber = 'BILL' + str(x)
        current_datetime = datetime.datetime.now()
        date = current_datetime.strftime('%d/%m/%Y')
        textR.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n')
        textR.insert(END, '***************************************************************\n')
        textR.insert(END, 'Items:\t\t Cost Of Items(Rs)\n')
        textR.insert(END, '***************************************************************\n')
        if e_Aloo.get() != '0':
            # Continue with the rest of your code for generating the receipt
            textR.insert(END,f'Aloo Paratha\t\t\t{int(e_Aloo.get())*10}\n\n')

        if e_tikka.get()!='0':
            textR.insert(END,f'Paneer Tikka\t\t\t{int(e_tikka.get())*60}\n\n')

        if e_pulao.get()!='0':
            textR.insert(END,f'Pulao\t\t\t{int(e_pulao.get())*100}\n\n')

        if e_Bhature.get() != '0':
            textR.insert(END, f'Chole Bhature:\t\t\t{int(e_Bhature.get()) * 30}\n\n')

        if e_Biryani.get() != '0':
            textR.insert(END, f'Vegetable Biryani:\t\t\t{int(e_Biryani.get()) * 50}\n\n')

        if e_Thepla.get() != '0':
            textR.insert(END, f'Thepla:\t\t\t{int(e_Thepla.get()) * 100}\n\n')

        if e_Dosa.get() != '0':
            textR.insert(END, f'Dosa:\t\t\t{int(e_Dosa.get()) * 40}\n\n')

        if e_Paneer.get() != '0':
            textR.insert(END, f'Paneer:\t\t\t{int(e_Paneer.get()) * 120}\n\n')

        if e_Upma.get() != '0':
            textR.insert(END, f'Upma:\t\t\t{int(e_Upma.get()) * 120}\n\n')

        if e_Whisky.get() != '0':
            textR.insert(END, f'Whisky:\t\t\t{int(e_Whisky.get()) * 50}\n\n')

        if e_Rum.get() != '0':
            textR.insert(END, f'Rum:\t\t\t{int(e_Rum.get()) * 40}\n\n')

        if e_Beer.get() != '0':
            textR.insert(END, f'Beer:\t\t\t{int(e_Beer.get()) * 80}\n\n')

        if e_Vodka.get() != '0':
            textR.insert(END, f'Vodka:\t\t\t{int(e_Vodka.get()) * 30}\n\n')

        if e_Brandy.get() != '0':
            textR.insert(END, f'Brandy:\t\t\t{int(e_Brandy.get()) * 40}\n\n')

        if e_Gin.get() != '0':
            textR.insert(END, f'Gin:\t\t\t{int(e_Gin.get()) * 60}\n\n')

        if e_Tequila.get() != '0':
            textR.insert(END, f'Tequila:\t\t\t{int(e_Tequila.get()) * 20}\n\n')

        if e_Cocktails.get() != '0':
            textR.insert(END, f'Cocktails:\t\t\t{int(e_Cocktails.get()) * 50}\n\n')

        if e_Sake.get() != '0':
            textR.insert(END, f'Sake:\t\t\t{int(e_Sake.get()) * 80}\n\n')

        if e_ChickenCurry.get() != '0':
            textR.insert(END, f'Curry:\t\t\t{int(e_ChickenCurry.get()) * 400}\n\n')

        if e_MuttonBiryani.get() != '0':
            textR.insert(END, f'Mutton:\t\t\t{int(e_MuttonBiryani.get()) * 300}\n\n')

        if e_ButterChicken1.get() != '0':
            textR.insert(END, f'ButterChicken:\t\t\t{int(e_ButterChicken1.get()) * 500}\n\n')

        if e_FishTandoori.get() != '0':
            textR.insert(END, f'Fish:\t\t\t{int(e_FishTandoori.get()) * 450}\n\n')

        if e_MuttonRoganJosh.get() != '0':
            textR.insert(END, f'JOSH:\t\t\t{int(e_MuttonRoganJosh.get()) * 800}\n\n')

        if e_LambKebabs.get() != '0':
            textR.insert(END, f'Kebabs:\t\t\t{int(e_LambKebabs.get()) * 620}\n\n')

        if e_ShrimpScampi.get() != '0':
            textR.insert(END, f'ShrimpScampi:\t\t\t{int(e_ShrimpScampi.get()) * 700}\n\n')

        if e_PorkVindaloo.get() != '0':
            textR.insert(END, f'Pork:\t\t\t{int(e_PorkVindaloo.get()) * 550}\n\n')

        if e_ChickenSarwama.get() != '0':
            textR.insert(END, f'Sarwama:\t\t\t{int(e_ChickenSarwama.get()) * 550}\n\n')

        textR.insert(END,'***************************************************************\n')
        if costofVeg.get()!='0 Rs':
            textR.insert(END,f'Cost Of VEG\t\t\t{priceofVeg}Rs\n\n')
        if costofNonveg.get() != '0 Rs':
            textR.insert(END,f'Cost Of NONVEG\t\t\t{priceofNonVeg}Rs\n\n')
        if costofDrinks.get() != '0 Rs':
            textR.insert(END,f'Cost Of DRINKS\t\t\t{priceofDrinks}Rs\n\n')

        textR.insert(END, f'Sub Total\t\t\t{subtotals}Rs\n\n')
        textR.insert(END, f'Service Tax\t\t\t{260}Rs\n\n')
        textR.insert(END, f'Total Cost\t\t\t{totalprice}Rs\n\n')
        textR.insert(END,'***************************************************************\n')

    else:
        messagebox.showerror('Error','No Item Is selected')




def save():
    if textR.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:

            bill_data=textR.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('GRATEFUL','THANKS FOR COMING')









def reset():
    textR.delete(1.0,END)
    e_Aloo.set('0')
    e_tikka.set('0')
    e_pulao.set('0')
    e_Bhature.set('0')
    e_Biryani.set('0')
    e_Thepla.set('0')
    e_Dosa.set('0')
    e_Paneer.set('0')
    e_Upma.set('0')

    e_Whisky.set('0')
    e_Rum.set('0')
    e_Beer.set('0')
    e_Vodka.set('0')
    e_Brandy.set('0')
    e_Gin.set('0')
    e_Tequila.set('0')
    e_Cocktails.set('0')
    e_Sake.set('0')

    e_ChickenCurry.set('0')
    e_MuttonBiryani.set('0')
    e_ButterChicken1.set('0')
    e_FishTandoori.set('0')
    e_MuttonRoganJosh.set('0')
    e_LambKebabs.set('0')
    e_ShrimpScampi.set('0')
    e_PorkVindaloo.set('0')
    e_ChickenSarwama.set('0')

    textAloo.config(state=DISABLED)
    textTikka.config(state=DISABLED)
    textPulao.config(state=DISABLED)
    textBhature.config(state=DISABLED)
    textBiryani.config(state=DISABLED)
    textThepla.config(state=DISABLED)
    textDosa.config(state=DISABLED)
    textPaneer.config(state=DISABLED)
    textUpma.config(state=DISABLED)

    text_Whiskey.config(state=DISABLED)
    text_Rum.config(state=DISABLED)
    text_Beer.config(state=DISABLED)
    text_Vodka.config(state=DISABLED)
    text_Brandy.config(state=DISABLED)
    text_Gin.config(state=DISABLED)
    text_Tequila.config(state=DISABLED)
    text_Cocktails.config(state=DISABLED)
    text_Sake.config(state=DISABLED)

    text_ChickenCurry.config(state=DISABLED)
    text_MuttonBiryani.config(state=DISABLED)
    text_ButterChicken1.config(state=DISABLED)
    text_FishTandoori.config(state=DISABLED)
    text_RoganJosh.config(state=DISABLED)
    text_LambKebabs.config(state=DISABLED)
    text_ShrimpScampi.config(state=DISABLED)
    text_PorkVindaloo.config(state=DISABLED)
    text_ChickenShawarma.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofNonveg.set('')
    costofVeg.set('')
    costofDrinks.set('')
    Subtotals.set('')
    ServiceTax.set('')
    Totalcost.set('')



def totalcost():
    global priceofVeg,priceofNonVeg,priceofDrinks,subtotals,totalprice
    item1 =int(e_Aloo.get())
    item2 =int(e_tikka.get())
    item3 = int(e_pulao.get())
    item4 = int(e_Bhature.get())
    item5 = int(e_Biryani.get())
    item6 = int(e_Thepla.get())
    item7 = int(e_Dosa.get())
    item8 = int(e_Paneer.get())
    item9 = int(e_Upma.get())

    item19 = int(e_ChickenCurry.get())
    item20 = int(e_Biryani.get())
    item21 = int(e_ButterChicken1.get())
    item22 = int(e_FishTandoori.get())
    item23 = int(e_MuttonRoganJosh.get())
    item24 = int(e_LambKebabs.get())
    item25 = int(e_ShrimpScampi.get())
    item26 = int(e_PorkVindaloo.get())
    item27 = int(e_ChickenSarwama.get())

    item10 = int(e_Whisky.get())
    item11 = int(e_Rum.get())
    item12 = int(e_Beer.get())
    item13 = int(e_Vodka.get())
    item14 = int(e_Brandy.get())
    item15 = int(e_Gin.get())
    item16 = int(e_Tequila.get())
    item17 = int(e_Cocktails.get())
    item18 = int(e_Sake.get())

    priceofVeg = (item1 * 100) + (item2 * 160) + (item3 * 110) + (item4 * 160) + (item5 * 101) + (item6 * 160) + (
                item7 * 110) + (item8 * 160) + (item9 * 110)
    priceofNonVeg = (item10 * 120) + (item11 * 260) + (item12 * 210) + (item13 * 260)\
                                    + (item14 * 170) + (item15 * 460) + (item16 * 310) + (item17 * 650) + (item18 * 210)
    priceofDrinks = (item10 * 1110) + (item11 * 1160) + (item12 * 2210) + (item13 * 2260) + (item14 * 3310) \
                                    + (item15 * 2260) + (item16 * 3310) + (item17 * 8860) + (item18 * 7710)

    costofVeg.set(str(priceofVeg)+'RS')
    costofNonveg.set(str(priceofNonVeg)+'RS')
    costofDrinks.set(str(priceofDrinks)+'RS')

    subtotals=priceofDrinks+priceofVeg+priceofNonVeg
    Subtotals.set(str(subtotals)+"RS")
    ServiceTax.set("256 RS")

    totalprice=subtotals+256
    Totalcost.set(str(totalprice)+"RS")





def Aloo():
    if var1.get()==1:
        textAloo.config(state=NORMAL)
        textAloo.delete(0,END)
        textAloo.focus()

    else:
        textAloo.config(state=DISABLED)
        e_Aloo.set('0')


def Tikka():
    if var2.get() == 1:
        textTikka.config(state=NORMAL)
        textTikka.delete(0, END)
        textTikka.focus()

    else:
        textTikka.config(state=DISABLED)
        e_tikka.set('0')

def Pulao():
    if var3.get() == 1:
        textPulao.config(state=NORMAL)
        textPulao.delete(0, END)
        textPulao.focus()

    else:
        textPulao.config(state=DISABLED)
        e_pulao.set('0')

def Bhature():
    if var4.get() == 1:
        textBhature.config(state=NORMAL)
        textBhature.delete(0, END)
        textBhature.focus()

    else:
        textBhature.config(state=DISABLED)
        e_Bhature.set('0')

def Tikka():
    if var5.get() == 1:
        textTikka.config(state=NORMAL)
        textTikka.delete(0, END)
        textTikka.focus()

    else:
        textTikka.config(state=DISABLED)
        e_tikka.set('0')

def BiryaniV():
    if var6.get() == 1:
        textBiryani.config(state=NORMAL)
        textBiryani.delete(0, END)
        textBiryani.focus()

    else:
        textBiryani.config(state=DISABLED)
        e_Biryani.set('0')

def Thepla():
    if var7.get() == 1:
        textThepla.config(state=NORMAL)
        textThepla.delete(0, END)
        textThepla.focus()

    else:
        textThepla.config(state=DISABLED)
        e_Thepla.set('0')

def Dosa():
    if var7.get() == 1:
        textDosa.config(state=NORMAL)
        textDosa.delete(0, END)
        textDosa.focus()
    else:
        textDosa.config(state=DISABLED)
        e_Dosa.set('0')

def Paneer():
    if var8.get() == 1:
        textPaneer.config(state=NORMAL)
        textPaneer.delete(0, END)
        textPaneer.focus()
    else:
        textPaneer.config(state=DISABLED)
        e_Paneer.set('0')

def Upma():
    if var9.get() == 1:
        textUpma.config(state=NORMAL)
        textUpma.delete(0, END)
        textUpma.focus()
    else:
        textUpma.config(state=DISABLED)
        e_Upma.set('0')

def Whiskey():
    if var10.get() == 1:
        text_Whiskey.config(state=NORMAL)
        text_Whiskey.delete(0, END)
        text_Whiskey.focus()
    else:
        text_Whiskey.config(state=DISABLED)
        e_Whisky.set('0')

def Rum():
    if var11.get() == 1:
        text_Rum.config(state=NORMAL)
        text_Rum.delete(0, END)
        text_Rum.focus()
    else:
        text_Rum.config(state=DISABLED)
        e_Rum.set('0')

def Beer():
    if var12.get() == 1:
        text_Beer.config(state=NORMAL)
        text_Beer.delete(0, END)
        text_Beer.focus()
    else:
        text_Beer.config(state=DISABLED)
        e_Beer.set('0')

def Vodka():
    if var13.get() == 1:
        text_Vodka.config(state=NORMAL)
        text_Vodka.delete(0, END)
        text_Vodka.focus()
    else:
        text_Vodka.config(state=DISABLED)
        e_Vodka.set('0')

def Brandy():
    if var14.get() == 1:
        text_Brandy.config(state=NORMAL)
        text_Brandy.delete(0, END)
        text_Brandy.focus()
    else:
        text_Brandy.config(state=DISABLED)
        e_Brandy.set('0')

def Gin():
    if var15.get() == 1:
        text_Gin.config(state=NORMAL)
        text_Gin.delete(0, END)
        text_Gin.focus()
    else:
        text_Gin.config(state=DISABLED)
        e_Gin.set('0')

def Tequila():
    if var16.get() == 1:
        text_Tequila.config(state=NORMAL)
        text_Tequila.delete(0, END)
        text_Tequila.focus()
    else:
        text_Tequila.config(state=DISABLED)
        e_Tequila.set('0')

def Cocktails():
    if var17.get() == 1:
        text_Cocktails.config(state=NORMAL)
        text_Cocktails.delete(0, END)
        text_Cocktails.focus()
    else:
        text_Cocktails.config(state=DISABLED)
        e_Cocktails.set('0')

def Sake():
    if var18.get() == 1:
        text_Sake.config(state=NORMAL)
        text_Sake.delete(0, END)
        text_Sake.focus()
    else:
        text_Sake.config(state=DISABLED)
        e_Sake.set('0')

def ChickenCurry():
    if var19.get() == 1:
        text_ChickenCurry.config(state=NORMAL)
        text_ChickenCurry.delete(0, END)
        text_ChickenCurry.focus()
    else:
        text_ChickenCurry.config(state=DISABLED)
        e_ChickenCurry.set('0')

def MuttonBiryani():
    if var20.get() == 1:
        text_MuttonBiryani.config(state=NORMAL)
        text_MuttonBiryani.delete(0, END)
        text_MuttonBiryani.focus()
    else:
        text_MuttonBiryani.config(state=DISABLED)
        e_MuttonBiryani.set('0')

def ButterChicken():
    if var21.get() == 1:
        text_ButterChicken1.config(state=NORMAL)
        text_ButterChicken1.delete(0, END)
        text_ButterChicken1.focus()
    else:
        text_ButterChicken1.config(state=DISABLED)
        e_ButterChicken1.set('0')

def FishTandoori():
    if var22.get() == 1:
        text_FishTandoori.config(state=NORMAL)
        text_FishTandoori.delete(0, END)
        text_FishTandoori.focus()
    else:
        text_FishTandoori.config(state=DISABLED)
        e_FishTandoori.set('0')

def MuttonRoganJosh():
    if var23.get() == 1:
        text_RoganJosh.config(state=NORMAL)
        text_RoganJosh.delete(0, END)
        text_RoganJosh.focus()
    else:
        text_RoganJosh.config(state=DISABLED)
        e_MuttonRoganJosh.set('0')

def LambKebabs():
    if var24.get() == 1:
        text_LambKebabs.config(state=NORMAL)
        text_LambKebabs.delete(0, END)
        text_LambKebabs.focus()
    else:
        text_LambKebabs.config(state=DISABLED)
        e_LambKebabs.set('0')


def ShrimpScampi():
    if var25.get() == 1:
        text_ShrimpScampi.config(state=NORMAL)
        text_ShrimpScampi.delete(0, END)
        text_ShrimpScampi.focus()
    else:
        text_ShrimpScampi.config(state=DISABLED)
        e_ShrimpScampi.set('0')

def PorkVindaloo():
    if var26.get() == 1:
        text_PorkVindaloo.config(state=NORMAL)
        text_PorkVindaloo.delete(0, END)
        text_PorkVindaloo.focus()
    else:
        text_PorkVindaloo.config(state=DISABLED)
        e_PorkVindaloo.set('0')

def ChickenSarwana():
    if var27.get() == 1:
        text_ChickenShawarma.config(state=NORMAL)
        text_ChickenShawarma.delete(0, END)
        text_ChickenShawarma.focus()
    else:
        text_ChickenShawarma.config(state=DISABLED)
        e_ChickenSarwama.set('0')



root = Tk()

root.geometry('1270x690+0+0')
root.resizable(0, 0)
root.title("Paro Da Dabba")
root.config(bg='pink')

topLabel = Frame(root, bd=10, relief=RIDGE,bg='pink')
topLabel.pack(side=TOP)

custom_font = ('Helvetica', 24, 'bold')

labelTitle = Label(topLabel, text='Paro Da Dabba - Punjabi Dishes', font=custom_font,
                   fg='red4',bg='orange',width=64)
labelTitle.grid(row=0, column=0)

#Frames will be Created!!!

menuF=Frame(root,bd=10,relief=RIDGE,bg='pink')
menuF.pack(side=LEFT)

costF=Frame(menuF,bd=4,relief=RIDGE,bg='orange')
costF.pack(side=BOTTOM)

NonFoodF=LabelFrame(menuF,text='NonVeg Food',font=('arial',16,'bold'),bd=10,relief=RIDGE,bg='orange',fg='red')
NonFoodF.pack(side=LEFT)

VegFoodF=LabelFrame(menuF,text='Veg Food',font=('arial',16,'bold'),bd=10,relief=RIDGE,bg='orange',fg='red')
VegFoodF.pack(side=LEFT)

DrinksF=LabelFrame(menuF,text='Food',font=('arial',16,'bold'),bd=10,relief=RIDGE,bg='orange',fg='red')
DrinksF.pack(side=LEFT)

RightFrame=Frame(root,bd=15,relief=RIDGE)
RightFrame.pack(side=RIGHT)

Calci=Frame(RightFrame,bd=1,relief=RIDGE)
Calci.pack()

reciept=Frame(RightFrame,bd=4,relief=RIDGE)
reciept.pack()

buttonFrame=Frame(RightFrame,bd=3,relief=RIDGE)
buttonFrame.pack()



#vars
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

#VEG
e_Aloo=StringVar()
e_tikka=StringVar()
e_pulao=StringVar()
e_Bhature=StringVar()
e_Biryani=StringVar()
e_Thepla=StringVar()
e_Dosa=StringVar()
e_Paneer=StringVar()
e_Upma=StringVar()

#Drinks
e_Whisky =StringVar()
e_Rum = StringVar()
e_Beer = StringVar()
e_Vodka = StringVar()
e_Brandy = StringVar()
e_Gin = StringVar()
e_Tequila = StringVar()
e_Cocktails = StringVar()
e_Sake = StringVar()

# Non-Veg Food
e_ChickenCurry = StringVar()
e_MuttonBiryani = StringVar()
e_ButterChicken1 = StringVar()
e_FishTandoori = StringVar()
e_MuttonRoganJosh = StringVar()
e_LambKebabs = StringVar()
e_ShrimpScampi = StringVar()
e_PorkVindaloo=StringVar()
e_ChickenSarwama = StringVar()

costofNonveg=StringVar()
costofVeg=StringVar()
costofDrinks=StringVar()
Subtotals=StringVar()
ServiceTax=StringVar()
Totalcost=StringVar()




#For VEG FOODS
e_Aloo.set('0')
e_tikka.set('0')
e_pulao.set('0')
e_Bhature.set('0')
e_Biryani.set('0')
e_Thepla.set('0')
e_Dosa.set('0')
e_Paneer.set('0')
e_Upma.set('0')

#For NON VEG
e_ChickenCurry.set('0')
e_MuttonBiryani.set('0')
e_ButterChicken1.set('0')
e_FishTandoori.set('0')
e_MuttonRoganJosh.set('0')
e_LambKebabs.set('0')
e_ShrimpScampi.set('0')
e_PorkVindaloo.set('0')
e_ChickenSarwama.set('0')


#For Drinks
e_Whisky.set('0')
e_Rum.set('0')
e_Beer.set('0')
e_Vodka.set('0')
e_Brandy.set('0')
e_Gin.set('0')
e_Tequila.set('0')
e_Cocktails.set('0')
e_Sake.set('0')




#Khana
AlooParatha = Checkbutton(VegFoodF, text="Aloo Paratha", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var1, command=Aloo)
AlooParatha.grid(row=0, column=0, sticky=W)

PaneerTikka = Checkbutton(VegFoodF, text="Paneer Tikka", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var2, command=Tikka)
PaneerTikka.grid(row=1, column=0, sticky=W)

Pulao = Checkbutton(VegFoodF, text="Pulao", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var3, command=Pulao)
Pulao.grid(row=2, column=0, sticky=W)

CholeBhature = Checkbutton(VegFoodF, text="Chole Bhature", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var4, command=Bhature)
CholeBhature.grid(row=3, column=0, sticky=W)

VegetableBiryani = Checkbutton(VegFoodF, text="Vegetable Biryani", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var5, command=BiryaniV)
VegetableBiryani.grid(row=4, column=0, sticky=W)

MethiThepla = Checkbutton(VegFoodF, text="Methi Thepla", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var6, command=Thepla)
MethiThepla.grid(row=5, column=0, sticky=W)

MasalaDosa = Checkbutton(VegFoodF, text="Masala Dosa", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var7, command=Dosa)
MasalaDosa.grid(row=6, column=0, sticky=W)

PalakPaneer = Checkbutton(VegFoodF, text="Palak Paneer", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var8, command=Paneer)
PalakPaneer.grid(row=7, column=0, sticky=W)

VegetableUpma = Checkbutton(VegFoodF, text="Vegetable Upma", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var9, command=Upma)
VegetableUpma.grid(row=8, column=0, sticky=W)


#CheckButtonForDrinks

Whiskey =Checkbutton(DrinksF,text="Whiskey",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=Whiskey)
Whiskey.grid(row=0,column=0,sticky=W)

Rum =Checkbutton(DrinksF,text="Rum",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=Rum)
Rum.grid(row=1,column=0,sticky=W)

Beer =Checkbutton(DrinksF,text="Beer",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=Rum)
Beer.grid(row=2,column=0,sticky=W)

Vodka=Checkbutton(DrinksF,text="Vodka",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=Vodka)
Vodka.grid(row=3,column=0,sticky=W)

Brandy=Checkbutton(DrinksF,text="Brandy",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=Brandy)
Brandy.grid(row=4,column=0,sticky=W)

Gin=Checkbutton(DrinksF,text="Gin",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=Gin)
Gin.grid(row=5,column=0,sticky=W)

Tequila=Checkbutton(DrinksF,text="Tequila",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=Tequila)
Tequila.grid(row=6,column=0,sticky=W)

Cocktails=Checkbutton(DrinksF,text="Cocktails",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=Cocktails)
Cocktails.grid(row=7,column=0,sticky=W)

Sake=Checkbutton(DrinksF,text="Sake",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=Sake)
Sake.grid(row=8,column=0,sticky=W)

#NONVEG FOODS
# Non-Veg Foods
ChickenCurry = Checkbutton(NonFoodF, text="Chicken Curry", font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                           variable=var19,command=ChickenCurry)
ChickenCurry.grid(row=0, column=0, sticky=W)

Biryani = Checkbutton(NonFoodF, text="Biryani", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var20,command=MuttonBiryani)
Biryani.grid(row=1, column=0, sticky=W)

ButterChicken1 = Checkbutton(NonFoodF, text="Butter Chicken", font=('arial', 18, 'bold'),
                            onvalue=1, offvalue=0, variable=var21)
ButterChicken1.grid(row=2, column=0, sticky=W)

FishTandoori = Checkbutton(NonFoodF, text="Fish Tandoori", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var22,command=FishTandoori)
FishTandoori.grid(row=3, column=0, sticky=W)

MuttonRoganJosh = Checkbutton(NonFoodF, text="Mutton Rogan Josh", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var23,command=MuttonRoganJosh)
MuttonRoganJosh.grid(row=4, column=0, sticky=W)

LambKebabs = Checkbutton(NonFoodF, text="Lamb Kebabs", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var24,command=LambKebabs)
LambKebabs.grid(row=5, column=0, sticky=W)

ShrimpScampi = Checkbutton(NonFoodF, text="Shrimp Scampi", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var25,command=ShrimpScampi)
ShrimpScampi.grid(row=6, column=0, sticky=W)

PorkVindaloo = Checkbutton(NonFoodF, text="Pork Vindaloo", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var26,command=PorkVindaloo)
PorkVindaloo.grid(row=7, column=0, sticky=W)

ChickenShawarma = Checkbutton(NonFoodF, text="Chicken Shawarma", font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var27,command=ChickenSarwana)
ChickenShawarma.grid(row=8, column=0, sticky=W)







#EnterFields
textAloo=Entry(VegFoodF,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Aloo)
textAloo.grid(row=0,column=1)

textTikka=Entry(VegFoodF,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_tikka)
textTikka.grid(row=1,column=1)

textPulao=Entry(VegFoodF,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pulao)
textPulao.grid(row=2,column=1)

textBhature=Entry(VegFoodF,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Bhature)
textBhature.grid(row=3,column=1)

textBiryani=Entry(VegFoodF,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Biryani)
textBiryani.grid(row=4,column=1)

textThepla=Entry(VegFoodF,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Thepla)
textThepla.grid(row=5,column=1)

textDosa=Entry(VegFoodF,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Dosa)
textDosa.grid(row=6,column=1)

textPaneer=Entry(VegFoodF,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Paneer)
textPaneer.grid(row=7,column=1)

textUpma=Entry(VegFoodF,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Upma)
textUpma.grid(row=8,column=1)


# EnterFields for a drink (e.g., Whiskey)
text_Whiskey = Entry(DrinksF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Whisky)
text_Whiskey.grid(row=0, column=1)

# EnterFields for the drinks in DrinksF frame
text_Rum = Entry(DrinksF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Rum)
text_Rum.grid(row=1, column=1)

text_Beer = Entry(DrinksF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Beer)
text_Beer.grid(row=2, column=1)

text_Vodka = Entry(DrinksF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Vodka)
text_Vodka.grid(row=3, column=1)

text_Brandy = Entry(DrinksF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Brandy)
text_Brandy.grid(row=4, column=1)

text_Gin = Entry(DrinksF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Gin)
text_Gin.grid(row=5, column=1)

text_Tequila = Entry(DrinksF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Tequila)
text_Tequila.grid(row=6, column=1)

text_Cocktails = Entry(DrinksF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Cocktails)
text_Cocktails.grid(row=7, column=1)


text_Sake = Entry(DrinksF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Sake)
text_Sake.grid(row=8, column=1)


# EntryFields for the top 9 non-veg foods in NonFoodF frame
text_ChickenCurry = Entry(NonFoodF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_ChickenCurry)
text_ChickenCurry.grid(row=0, column=1)

text_MuttonBiryani = Entry(NonFoodF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_MuttonBiryani)
text_MuttonBiryani.grid(row=1, column=1)

text_ButterChicken1 = Entry(NonFoodF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_ButterChicken1)
text_ButterChicken1.grid(row=2, column=1)

text_FishTandoori = Entry(NonFoodF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_FishTandoori)
text_FishTandoori.grid(row=3, column=1)

text_RoganJosh = Entry(NonFoodF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_MuttonRoganJosh)
text_RoganJosh.grid(row=4, column=1)

text_LambKebabs = Entry(NonFoodF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_LambKebabs)
text_LambKebabs.grid(row=5, column=1)

text_ShrimpScampi = Entry(NonFoodF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_ShrimpScampi)
text_ShrimpScampi.grid(row=6, column=1)

text_PorkVindaloo = Entry(NonFoodF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_PorkVindaloo)
text_PorkVindaloo.grid(row=7, column=1)

text_ChickenShawarma = Entry(NonFoodF, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_ChickenSarwama)
text_ChickenShawarma.grid(row=8, column=1)

#COST Labels
labelOFCostN = Label(costF, text='COST OF NONVEG', font=('arial', 16, 'bold'), fg='red', bg='orange')
labelOFCostN.grid(row=0, column=0)

textCostofFoodN = Entry(costF, font=('arial', 16, 'bold'), bd=6,state='readonly',textvariable=costofNonveg)
textCostofFoodN.grid(row=0, column=1)

labelOFCostV = Label(costF, text='COST OF VEG', font=('arial', 16, 'bold'), fg='red', bg='orange')
labelOFCostV.grid(row=1, column=0)

textCostofFoodV = Entry(costF, font=('arial', 16, 'bold'), bd=6,state='readonly',textvariable=costofVeg)
textCostofFoodV.grid(row=1, column=1)
labelOFCostD = Label(costF, text='COST OF DRINKS', font=('arial', 16, 'bold'), fg='red', bg='orange')
labelOFCostD.grid(row=2, column=0)

textCostofFoodD = Entry(costF, font=('arial', 16, 'bold'), bd=6,state='readonly',textvariable=costofDrinks)
textCostofFoodD.grid(row=2, column=1)

labelOFSUBCost = Label(costF, text=' SUB TOTAL ', font=('arial', 16, 'bold'), fg='red', bg='orange')
labelOFSUBCost.grid(row=0, column=2)

textSUB = Entry(costF, font=('arial', 16, 'bold'), bd=6,state='readonly',textvariable=Subtotals)
textSUB.grid(row=0, column=3)

labelOFTAXES = Label(costF, text=' SERVICE TAXES', font=('arial', 16, 'bold'), fg='red', bg='orange')
labelOFTAXES.grid(row=1, column=2)

textTAXES = Entry(costF, font=('arial', 16, 'bold'), bd=6,state='readonly',textvariable=ServiceTax)
textTAXES.grid(row=1, column=3)

labelOFTOTAL = Label(costF, text=' TOTAL COST', font=('arial', 16, 'bold'), fg='red', bg='orange')
labelOFTOTAL.grid(row=2, column=2)

textTOTAL = Entry(costF, font=('arial', 16, 'bold'), bd=6,state='readonly',textvariable=Totalcost)
textTOTAL.grid(row=2, column=3)

# Buttons

# Buttons
# ... Your previous code ...

# Buttons


buttonTotal = Button(buttonFrame, text='TL', font=('arial', 8, 'bold'), fg='white', bg='red4', bd=3,padx=5,command=totalcost)
buttonTotal.grid(row=0, column=0)

buttonReceipt = Button(buttonFrame, text='RE', font=('arial', 8, 'bold'), fg='white', bg='red4', bd=3,padx=5,command=receipt)
buttonReceipt.grid(row=0, column=1)

buttonSave = Button(buttonFrame, text='SE', font=('arial', 8, 'bold'), fg='white', bg='red4', bd=3,padx=5,command=save)
buttonSave.grid(row=0, column=2)

buttonSend = Button(buttonFrame, text='SD', font=('arial', 8, 'bold'), fg='white', bg='red4', bd=3,padx=5,command=send)
buttonSend.grid(row=0, column=3)

buttonReset = Button(buttonFrame, text='RT', font=('arial', 8, 'bold'), fg='white', bg='red4', bd=3,padx=5,command=reset)
buttonReset.grid(row=0, column=4)

#textarea
textR = Text(reciept,font=('arial',12,'bold'),bd=3,bg='orange',width=42,height=14)
textR.grid(row=0,column=0)


#functions

#Calculator
operator='' #7+9
def buttonClick(numbers): #9
    global operator
    operator=operator+numbers
    calcifield.delete(0,END)
    calcifield.insert(END,operator)

def clear():
    global operator
    operator=''
    calcifield.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calcifield.delete(0,END)
    calcifield.insert(0,result)
    operator=''


calcifield = Entry(Calci,font=('arial',10,'bold'),width=32,bd=4)
calcifield.grid(row=0,column=0,columnspan=4)



button7=Button(Calci,text='7',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)
button8=Button(Calci,text='8',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)
button9=Button(Calci,text='9',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)
buttonplus=Button(Calci,text='+',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=lambda:buttonClick('+'))
buttonplus.grid(row=1,column=3)
button4=Button(Calci,text='4',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)
button5=Button(Calci,text='5',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)
button6=Button(Calci,text='6',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)
buttonminus=Button(Calci,text='-',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=lambda:buttonClick('-'))
buttonminus.grid(row=2,column=3)
button1=Button(Calci,text='1',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)
button2=Button(Calci,text='2',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)
button3=Button(Calci,text='3',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)
buttonmul=Button(Calci,text='*',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=lambda:buttonClick('*'))
buttonmul.grid(row=3,column=3)
buttonANS=Button(Calci,text='ANS',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=answer)
buttonANS.grid(row=4,column=0)
buttonCAN=Button(Calci,text='CAL',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=clear)
buttonCAN.grid(row=4,column=1)
button0=Button(Calci,text='0',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)
buttonDiv=Button(Calci,text='/',font=('arial',9,'bold'),fg='red',bg='orange',bd=6,width=6,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

root.iconbitmap("C:\\Users\\santo\\OneDrive\\Desktop\\ABOUT\\python\\Management System\\icon.ico")

root.mainloop()











