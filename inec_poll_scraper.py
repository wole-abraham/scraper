#python script generates csv file from gathering data 
#of the polling units in lagos(not subject to this only) can be changed in script

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import csv 


driver = webdriver.Firefox()
driver.get("https://www.inecnigeria.org/?page_id=2526")
table_data = {'lagos': {}}
try:
    
    elem = driver.find_element(By.NAME, "states")
    elem.send_keys("Lagos")
    time.sleep(2)
    select = Select(driver.find_element(By.ID, 'lgaPoll'))
    time.sleep(2)
    for lga in select.options:
        select.select_by_visible_text(lga.get_attribute('text'))
        time.sleep(3)
        Select2 = Select(driver.find_element(By.ID, 'wardPoll'))
        for ward in Select2.options:
            if ward.get_attribute('text') == 'Choose Ward':
                continue
            Select2.select_by_visible_text(ward.get_attribute('text'))
            time.sleep(3)
            driver.find_element(By.ID, "SearchPoll").click()
            time.sleep(3)
            table = driver.find_element(By.TAG_NAME, "tbody")
            rows = table.find_elements(By.TAG_NAME, "tr")

            if lga.get_attribute('text') not in table_data['lagos']:
                table_data['lagos'][lga.get_attribute('text')] = []
            for row in rows:
                cols = row.find_elements(By.TAG_NAME, "td")
                row_data = [col.text for col in cols]
                row_data.append(ward.get_attribute('text'))
                row_data.append(lga.get_attribute('text'))
                table_data['lagos'][lga.get_attribute('text')].append(row_data)
except:
    pass
           

        
with open('polling_unit_data.csv', 'w', newline='') as csv_file:
     writer = csv.writer(csv_file)
     writer.writerow(['polling id', 'polling unit name', 'remark', 'ward', 'lga'])
     for keys, values in table_data['lagos'].items():
            writer.writerows(values)
