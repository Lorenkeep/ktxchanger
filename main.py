from tkinter import *
from tkinter import ttk
#para ficheros de configuración importamos configparser
import configparser
import json
##para  html "requests"
import requests

config = configparser.ConfigParser()
config.read('config.ini')

inSymbol = input ("Qué moneda quieres convertir: ")
outSymbol = input ("En que otra moneda: ")


url = config['fixer.io']['RATE_LATEST_EP']
api_key = config['fixer.io']['API_KEY']

url = url.format(api_key, inSymbol, outSymbol)
response = requests.get(url)
if response.status_code == 200:
    print (response.text) 
else:
    print ("Se ha producion un error en la peticion: ", response.status_code)


a = 1