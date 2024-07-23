from tkinter import*
from tkinter import messagebox
import tempfile
import os 
root=Tk()
root.title('Bakery Billing System-GST')
root.geometry('1280x780')
bg_color='#2D9290'

#===================Variable============================
Bread=IntVar()
Pastry=IntVar()
Cake=IntVar()
Icecream=IntVar()
Waffles=IntVar()
total=IntVar()

cb=StringVar()
cp=StringVar()
cc=StringVar()
ci=StringVar()
cw=StringVar()
total_cost=StringVar() 

#======================Functions=========================
def itemsordered():
    temp=[]
    quant=[]
    if Bread.get():
        temp.append("Bread")
        quant.append(Bread.get())
    if Icecream.get():
        temp.append("Icecream")
        quant.append(Icecream.get())
    if Pastry.get():
        temp.append("Pastry")
        quant.append(Pastry.get())
    if Cake.get():
        temp.append("Cake")
        quant.append(Cake.get())
    if Waffles.get():
        temp.append("Waffle")
        quant.append(Waffles.get())
    return temp,quant
    
def Total():
    if Bread.get()==0 and Icecream.get()==0 and Pastry.get()==0 and Cake.get()==0 and Waffles.get()==0 :
        messagebox.showerror('Error','Please select number of quantity')
    else:
        b=Bread.get()
        i=Icecream.get()
        p=Pastry.get()
        c=Cake.get()
        w=Waffles.get()

        t=float(b*20.0+p*40.0+c*350.0+i*40.0+w*10.0)
        total.set(b+p+c+i+w)
        total_cost.set('₹'+str(round(t,2)))

        cb.set(str(round(b*20.0,2)))
        ci.set(str(round(i*40.0,2)))
        cp.set(str(round(p*40.0,2)))
        cc.set(str(round(c*350.0,2)))
        cw.set(str(round(w*10.5,2)))

def reciptcost():
    totalcst=[cb.get(),ci.get(),cp.get(),cc.get(),cw.get()]
    finalcost=[]
    for j in totalcst:
        if float(j)>0:
            finalcost.append(j)
    return finalcost

    
def receipt():
    textarea.delete(1.0,END)
    textarea.insert(END,'Items\tNumber of Items\tCost of Items')
    items,quantity=itemsordered()
    cost=reciptcost()
    for i in range(len(items)):
        textarea.insert(END,f'\n\n{items[i]}\t\t{quantity[i]}\t{cost[i]}')
    textarea.insert(END,'\n\n================================')
    textarea.insert(END,f'\nTotal price\t\t{total.get()}\t{total_cost.get()}')
    textarea.insert(END,'\n================================')

def print():
    q=textarea.get('1.0','end-1c')
    filename=tempfile.mktemp('.txt')
    open(filename,'w',encoding="utf8").write(q)
    os.startfile(filename,'Print')

def reset():
    textarea.delete(1.0,END)
    Bread.set(0)
    Pastry.set(0)
    Cake.set(0)
    Icecream.set(0)
    Waffles.set(0)
    total.set(0)

    cb.set('')
    cp.set('')
    cc.set('')
    ci.set('')
    cw.set('')
    total_cost.set('')

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()

title=Label(root, text='Bakery Billing System-GST', bg=bg_color, fg='white', font=('times new romman', 35, 'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)

#===================Products details=====================
F1=LabelFrame(root, text='Product Details', font=('times new romman', 18, 'bold'),fg='gold', bg=bg_color,relief=RIDGE,bd=15)
F1.place(x=5,y=90,width=800,height=550)

#===================Heading==============================
itm=Label(F1,text='Items',font=('Helvetic',25,'bold'), fg='black')
itm.grid(row=0,column=0,padx=20,pady=15)

n=Label(F1,text='Number of Items',font=('Helvetic',25,'bold'), fg='black')
n.grid(row=0,column=1,padx=10,pady=10)

cost=Label(F1,text='Cost of Items',font=('Helvetic',25,'bold',), fg='black')
cost.grid(row=0,column=2,padx=20,pady=15)

#==================Product===============================
bread=Label(F1,text='Bread', font=('times new rommon',20,'bold'),fg='gold',bg=bg_color)
bread.grid(row=1,column=0,padx=20,pady=15)
b_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Bread)
b_txt.grid(row=1,column=1,padx=20,pady=15)
cb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cb)
cb_txt.grid(row=1,column=2,padx=20,pady=15)

pastry=Label(F1,text='Pastry', font=('times new rommon',20,'bold'),fg='gold',bg=bg_color)
pastry.grid(row=2,column=0,padx=20,pady=15)
p_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Pastry)
p_txt.grid(row=2,column=1,padx=20,pady=15)
cp_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cp)
cp_txt.grid(row=2,column=2,padx=20,pady=15)

cake=Label(F1,text='cake', font=('times new rommon',20,'bold'),fg='gold',bg=bg_color)
cake.grid(row=3,column=0,padx=20,pady=15)
c_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Cake)
c_txt.grid(row=3,column=1,padx=20,pady=15)
cc_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cc)
cc_txt.grid(row=3,column=2,padx=20,pady=15)

icecream=Label(F1,text='Icecream', font=('times new rommon',20,'bold'),fg='gold',bg=bg_color)
icecream.grid(row=4,column=0,padx=20,pady=15)
i_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Icecream)
i_txt.grid(row=4,column=1,padx=20,pady=15)
ci_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=ci)
ci_txt.grid(row=4,column=2,padx=20,pady=15)

waffles=Label(F1,text='Waffles', font=('times new rommon',20,'bold'),fg='gold',bg=bg_color)
waffles.grid(row=5,column=0,padx=20,pady=15)
w_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Waffles)
w_txt.grid(row=5,column=1,padx=20,pady=15)
cw_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cw)
cw_txt.grid(row=5,column=2,padx=20,pady=15)

t=Label(F1,text='Total Price', font=('times new rommon',20,'bold'),fg='gold',bg=bg_color)
t.grid(row=6,column=0,padx=20,pady=15)
t_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=total)
t_txt.grid(row=6,column=1,padx=20,pady=15)
ct_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=total_cost)
ct_txt.grid(row=6,column=2,padx=20,pady=15)

#===================== billing area============================
F2=Frame(root,relief=GROOVE,bd=10)
F2.place(x=820,y=90,width=430,height=550)
bill_title=Label(F2,text='Receipt',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol=Scrollbar(F2,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15',yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)

#==================== button======================================
F3=Frame(root,relief=GROOVE,bd=10,bg=bg_color)
F3.place(x=5,y=650,width=1270,height=120)
btn1=Button(F3,text='Total',font='arial 25 bold',bg='white',fg='crimson',padx=5,pady=5,width=10,command=Total)
btn1.grid(row=0,column=0,padx=15,pady=10)

btn2=Button(F3,text='Receipt',font='arial 25 bold',bg='white',fg='crimson',padx=5,pady=5,width=10,command=receipt)
btn2.grid(row=0,column=1,padx=15,pady=10)

btn3=Button(F3,text='Print',font='arial 25 bold',bg='white',fg='crimson',padx=5,pady=5,width=10,command=print)
btn3.grid(row=0,column=2,padx=15,pady=10)

btn4=Button(F3,text='Reset',font='arial 25 bold',bg='white',fg='crimson',padx=5,pady=5,width=10,command=reset)
btn4.grid(row=0,column=3,padx=15,pady=10)

btn5=Button(F3,text='Exit',font='arial 25 bold',bg='white',fg='crimson',padx=5,pady=5,width=10,command=exit)
btn5.grid(row=0,column=4,padx=15,pady=10)
root.mainloop()
