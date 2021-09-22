import requests
from bs4 import BeautifulSoup
import smtplib

req="http://gvpce.ac.in/result.html"

r=requests.get(req)

soup=BeautifulSoup(r.content,'html5lib')

s=soup.find(id='table4').a

txt=s.get_text()

if "R-2015" in txt or "BTech III Sem" in txt :
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("Code2hunt4@gmail.com","luv2code@4")
    s.sendmail("Code2hunt4@gmail.com","vasireddi.ganesh.8@gmail.com","Hey There !!! Results Released")
    s.quit()



    
