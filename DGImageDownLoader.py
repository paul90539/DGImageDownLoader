import requests
from bs4 import BeautifulSoup
import shutil
import os
import sys
import queue
a = queue.Queue(0)

def saveImage(link, filePath):
    f = open(filePath, 'wb')
    resImage = requests.get(link, stream=True)
    shutil.copyfileobj(resImage.raw, f)
    f.close()
    del resImage

def getCount(infoStr):
    getNumFlag = False
    while( not getNumFlag ):      
        number = input(infoStr)
        if number.isdigit():
            number = int(number, 10)
            getNumFlag = True
        else:
            print("Input error, please enter digit.")

    return number

dir_name = 'dg_img'
if not os.path.exists(dir_name): 
    os.makedirs(dir_name)
dir_name2 = 'dg_icon'
if not os.path.exists(dir_name2): 
    os.makedirs(dir_name2)

startNum = getCount(">>> Input startNum: ")
endNum = getCount(">>> Input endNum: ")
endNum += 1

for i in range(startNum, endNum, 1):
    link = 'http://divine-gate.net/Units/lists/' + str(i)
    resHtml = requests.get(link)
    soup = BeautifulSoup(resHtml.text, "lxml")
    
    adds = ''
    if i < 10:
        adds = adds + '0'
    if i < 100:
        adds = adds + '0'
    if i < 1000:
        adds = adds + '0'
    
    for img in soup.select('.h2_panel'):
        picLink = 'http://divine-gate.net/' + img['src']
        fName = 'icon_' + adds + str(i) + '.png'
        fPath = os.path.join(dir_name2, fName)

        saveImage(picLink, fPath)

    for img in soup.select('.unit_img'):
        picLink = 'http://divine-gate.net/' + img['src']        
        fName = 'unit_' + adds + str(i) + '.png'
        fPath = os.path.join(dir_name, fName)

        saveImage(picLink, fPath)

    print ("case:" + str(i))
    del resHtml