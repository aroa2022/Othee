from  datetime import datetime
from datetime import timedelta
from time import sleep
from traceback import print_tb
import requests

date_1 = datetime.strptime('22-09-05', "%y-%m-%d") + timedelta(days=10)




# get current datetime
dt = datetime.strptime('09/09/22','%m/%d/%y').strftime(' %A')



# get weekday name

def time():
    c= 0
    #requgests
    r = requests.get('https://b24-8w7tjp.bitrix24.com/rest/1/bgrb1zcnrq98r55u/lists.element.get.json?IBLOCK_TYPE_ID=bitrix_processes&IBLOCK_ID=35')
    #loop for all elelment
    for i in r.json()['result']:
        t10 = i['PROPERTY_161'] #first time
        t20 = i['PROPERTY_163'] #sec time
        Time = i['PROPERTY_173']  #time field
        id = i['ID'] #id
        t100 = ""
        t200 = ""
        Time100 = ""
        
        for a,b in Time.items():
            Time100 = b
        for a,b in i['PROPERTY_161'].items():
            t100 = b
        for a,b in i['PROPERTY_163'].items():
            t200 = b
        #print("time 100" , Time100)
        if Time100 == "000":

            t1 = ''
            t2 = ''

            for a,b in t10.items():
                t1 = b
            for a,b in t20.items():
                t2 = b
            t1 = t1.replace('2022','22')
            t1 = t1.replace(' am','')
            t1e = t1.replace(' pm','')

            t2 = t2.replace(' am','')
            t2 = t2.replace(' pm','')
            t2e = t2.replace('2022','22')
            print (t1e)



            t1 = datetime.strptime(t1e,'%m/%d/%y %H:%M:%S')
            t2 = datetime.strptime(t2e,'%m/%d/%y %H:%M:%S')
            t3 =str(t2-t1).rsplit(',')
            print('F time is ',t1)
            print('S time is ',t2)
            print('The different Time is ' , t3)
            if len(t3) == 1 :
                #print('noday')
                hour = t3[0].rsplit(':',2)
                hour = hour[0]
                #print('hour' + hour)

            else:
                #print('day')
                day = t3[0].rsplit(' day')
                day=int(day[0])
                hour = t3[1].rsplit(':',2)
                hour = hour[0]
                for i in range(day) :
                    holede= datetime.strptime(t1e,'%m/%d/%y %H:%M:%S') + timedelta(days=i) 
                    nd =  (holede.strftime('%A'))
                    if nd == "Saturday" or nd == "Sunday":
                        c = c
                    else:
                        c = c + 1 
            print('hour = ',hour)
            diff = f"{c}  Day/s   " + " And   " + f"{hour} Hour/s"
            print('diff == ' ,diff)
            r = requests.post(f'https://b24-8w7tjp.bitrix24.com/rest/1/bgrb1zcnrq98r55u/lists.element.update?IBLOCK_TYPE_ID=bitrix_processes&IBLOCK_ID=35&ELEMENT_ID={id}&FIELDS[NAME]=Project&FIELDS[PROPERTY_173]={diff}&FIELDS[PROPERTY_161]={t100}&FIELDS[PROPERTY_163]={t200}')
        else:
            print('mhsoob' ,id)
    sleep(1)


for i in range(100):
    time()