import requests
from bs4 import BeautifulSoup
import smtplib
import time

while(True):
    req="http://gvpce.ac.in/result.html"

    r=requests.get(req)

    soup=BeautifulSoup(r.content,'html.parser')

    s=soup.find(id='table4').a

    txt=s.get_text()

    if "R-2019" in txt or "BTech III Sem" in txt :
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login("Code2hunt4@gmail.com","luv2code@4")
        s.sendmail("Code2hunt4@gmail.com","vasireddi.ganesh.8@gmail.com","Hey There !!! 3rd Sem Results Released")
        s.quit()
    time.sleep(1000)



    
