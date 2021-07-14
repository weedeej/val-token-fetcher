import requests
import json
import os
import urllib3
import tkinter
import base64
from tkinter import messagebox
import pyperclip

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

r = tkinter.Tk()
r.withdraw()
try:
    lockfile = open(os.getenv('localappdata')+'/Riot Games/Riot Client/Config/lockfile', 'r')
    credentials = lockfile.readline().split(':')
    processId = [1]
    port = credentials[2]
    token = credentials[3]
    protocol = credentials[4]
    basic = base64.b64encode((f"riot:{token}").encode()).decode()
    headers = {}
    headers["Authorization"] = f"Basic {basic}"
    resp = requests.get(f"{protocol}://127.0.0.1:{port}/entitlements/v1/token",headers=headers,verify=False)
    pyperclip.copy(json.loads(resp.text)["accessToken"])
    messagebox.showinfo('Access Token',"Token has been copied!\n")
except (FileNotFoundError,KeyError):
    messagebox.showwarning('Error',"Please login to VALORANT before using this file.\nPlease follow the instruction carefully\nto avoid further error.")