from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
web = webdriver.Firefox()
from time import sleep
web.get ('https://www.bitrix24.net/')
from openpyxl import Workbook
workbook = Workbook()
sheet = workbook.active

def tt():
    web.find_element(By.CLASS_NAME,'modern-page-next').click()
    sleep(3)
    for c in range (2,100):
        tr = web.find_element(By.XPATH,f'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td/div/div[2]/div/div/div/form/div[2]/div[1]/div[6]/table/tbody/tr[{c}]')
        event_type= tr.find_elements(By.CLASS_NAME,'main-grid-cell-content')
        if 'Responsible Person' in event_type[6].text:
            sort = sheet.max_row+1
            #print('------------------------')
            #print(event_type[2].text,event_type[4].text,event_type[5].text ,event_type[6].text,event_type[7].text)
            old= event_type[7].text.split('→')[0]
            new = event_type[7].text.split('→')[1]
            a= event_type[4].find_element(By.TAG_NAME,'a')
            id = a.get_attribute('href').split('/details/')
            print(id[1])
            sheet[f'A{sort}'] = event_type[2].text
            sheet[f'B{sort}'] = id[1]
            sheet[f'C{sort}'] = event_type[4].text
            sheet[f'D{sort}'] = event_type[5].text
            sheet[f'E{sort}'] = event_type[6].text
            sheet[f'F{sort}'] = old
            sheet[f'G{sort}'] = new
            sort = sort+1
            k=sort/10
            kk=str(k).split('.')[1]
            if kk =='0':
                workbook.save(filename="julay.xlsx")

for i in range(137,896):
    try:
        tt()
        print(i)
    except:
        input('error')