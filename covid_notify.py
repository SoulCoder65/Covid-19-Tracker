import time
import notify2
import requests
from bs4 import BeautifulSoup

ICON_PATH = "/home/akshay/Downloads/PYTHON/images/covid.png"
notify2.init("News Notifier")
n = notify2.Notification(None, icon=ICON_PATH)
n.set_urgency(notify2.URGENCY_NORMAL)

def notifyMe(title,message):
    title=title
    message=message
    n.update(title,message)
    n.show()
    time.sleep(5)

def getData(url):
    r=requests.get(url)
    return r.text

if __name__ == '__main__':
    site_data=getData("https://www.mohfw.gov.in/")

    soup=BeautifulSoup(site_data,'html.parser')

    mydata=""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        mydata+=tr.get_text()
    mydata=mydata[1::]
    item_list=mydata.split("\n\n")

    states=['Madhya Pradesh','Maharashtra','Delhi']
    for item in item_list[0:22]:
        datalist=item.split("\n")
        if datalist[1] in states:
            print(datalist)
            Title="Covid Update"
            Message=f"State: {datalist[1]}\n Cases: {datalist[2]}\n Cured: {datalist[3]}\n Death: {datalist[4]}"
            notifyMe(Title,Message)