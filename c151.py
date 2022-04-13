from tkinter import *

root=Tk()
root.title("sales application")
root.geometry("600x400")
root.configure(background="pink") 
label_months=Label(root)
label_sales=Label(root)
label_months.place(relx=0.5,rely=0.1,anchor=CENTER)
label_sales.place(relx=0.5,rely=0.2,anchor=CENTER)
month_tuple=("january","febuary","march","april","may","june","july","august","september","october","november","december")
sales_tuple=(2500,2000,23000,7000,1000,9700,6000,82000,2600,3000,1900,9000)
label_months["text"]="month :"+str(month_tuple)
label_sales["text"]="sales :"+str(sales_tuple)
label_maximumprofit=Label(root)
label_minimumprofit=Label(root)
label_maximumprofit.place(relx=0.5,rely=0.4,anchor=CENTER)
label_minimumprofit.place(relx=0.5,rely=0.7,anchor=CENTER)
def maxprofit():
    maxpro=max(sales_tuple)
    maxproindex=sales_tuple.index(maxpro)
    maximumpromonth=month_tuple[maxproindex]
    label_maximumprofit["text"]="maximum profit of:"+str(maxpro)+"in the month of"+str(maximumpromonth)
    
def minprofit():
    minpro=min(sales_tuple)
    minproindex=sales_tuple.index(minpro)
    minimumpromonth=month_tuple[minproindex]
    label_minimumprofit["text"]="minimum profit of:"+str(minpro)+"in the month of"+str(minimumpromonth)
button_maximum=Button(root,text="maximum profit month", command=maxprofit)
button_maximum.place(relx=0.5,rely=0.3,anchor=CENTER)
button_minimum=Button(root,text="minimum profit month", command=minprofit)
button_minimum.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()
