from distutils.cmd import Command
import tkinter
import requests
from tkinter import *
from customtkinter import *
import customtkinter
from bs4 import BeautifulSoup
def post_data():
    infopost.pack()
    try:
        
        dt=inp.get()
        url=f'http://ip-api.com/json/{dt}?fields=query'
        req=requests.get(url).json()
        d=req['query']
        url2=f'http://ip-api.com/json/{dt}?fields=country'
        country=requests.get(url2).json()['country']
        
        
        url3=f'http://ip-api.com/json/{dt}?fields=regionName'
        region=requests.get(url3).json()['regionName']
        url4=f'http://ip-api.com/json/{dt}?fields=zip'
        zip=requests.get(url4).json()['zip']
        text1=CTkLabel(infopost,text=f'query : {d} ')
        text3=CTkLabel(infopost,text=f'country: {country} ')
        text4=CTkLabel(infopost,text=f'region: {region} ')
        text5=CTkLabel(infopost,text=f'zip code: {zip} ')
        text1.pack()
        text3.pack()
        text4.pack()
        text5.pack()
    except:
        text2=CTkLabel(infopost,text='invalid ip')
        
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
root=CTk()
root.geometry('400x400')
root.iconbitmap('./icon.ico')

root.title('ip info Devloped by chiheb')
tit=CTkLabel(root,text='ip info' ,text_font='bold')
inp=CTkEntry(root,placeholder_text='please enter the ip')
btn=CTkButton(root,text='get info',command=post_data)
infopost=CTkFrame(root,bg_color='red')

tit.pack(padx=50,pady=15)
inp.pack(pady=15)
btn.pack(pady=25)


root.mainloop()