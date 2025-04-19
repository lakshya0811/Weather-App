from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=cfc18c552dbbe5544b915cb91b683439").json()
    
    climate_label.config(text=data["weather"][0]["main"])  # updated
    desc_label.config(text=data["weather"][0]["description"])  # updated
    temp_label1.config(text=str(int(data["main"]["temp"] -273.15)))
    per_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("DLN")
win.config(bg= 'blue')
win.geometry("500x570")

name_label = Label(win,text="DLN Weather App",
                   font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="DLN Weather App" ,values=list_name,
            font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

# Weather Climate Label
win_label = Label(win,text="Weather Climate",
                   font=("Time New Roman",20))
win_label.place(x=25,y=260,height=50,width=210)

climate_label = Label(win,text="",  # updated
                   font=("Time New Roman",20))  # updated
climate_label.place(x=250,y=260,height=50,width=210)  # updated

# Weather Description Label
win_label = Label(win,text="Weather Description",
                   font=("Time New Roman",17))
win_label.place(x=25,y=330,height=50,width=210)

desc_label = Label(win,text="",  # updated
                   font=("Time New Roman",17))  # updated
desc_label.place(x=250,y=330,height=50,width=210)  # updated

temp_label = Label(win,text="Temperature",
                   font=("Time New Roman",20))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1 = Label(win,text="",
                   font=("Time New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=210)

per_label = Label(win,text="Pressure",
                   font=("Time New Roman",20))
per_label.place(x=25,y=470,height=50,width=210)
per_label1 = Label(win,text="",
                   font=("Time New Roman",20))
per_label1.place(x=250,y=470,height=50,width=210)

done_button= Button(win,text="Done",
            font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=60,width=100,x=200)

win.mainloop()