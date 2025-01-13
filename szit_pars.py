from LxmlSoup import LxmlSoup
from datetime import date

import time
import requests
import os
import certifi

url = "https://192.168.1.17/stat/consumables.php"
url2 = "https://192.168.1.17/counters/usage.php"
file_name = "szit_pars.csv"

temp = 0
while temp == 0:
    r2 = requests.get(url2).text
    if r2 == 200:
        print('Error! Run to administrator!')
    else:
        print('First parsing is starting...')
        soup = LxmlSoup(r2)
        inf = soup.find_all('td')
        a = ' '
        count = 0
        for i in inf:
            if count == 1:
                a = a + i.text() + '; '
                print(i.text())
                count = 0
            if i.text() == 'Total Impressions':
                count = count + 1
    r = requests.get(url).text
    if r == 200:
        print('Error! Run to administrator!')
    else:
        print('Second parsing is starting...')
        soup = LxmlSoup(r)
        inf = soup.find_all('td')
        for i in inf:
            if i.text() == 'Black Toner':
                count = 5
            if count > 0 and i.text() != '':
                count = count - 1
                if count != 1 and count != 3 and count != 4:
                    a = a + i.text() + '; '
        count = 0
        a = a + ' '
        for i in inf:
            if i.text() == 'Cyan Toner':
                count = 5
            if count > 0 and i.text() != '':
                count = count - 1
                if count != 1 and count != 3 and count != 4:
                    a = a + i.text() + '; '
        count = 0
        a = a + ' '
        for i in inf:
            if i.text() == 'Magenta Toner':
                count = 5
            if count > 0 and i.text() != '':
                count = count - 1
                if count != 1 and count != 3 and count != 4:
                    a = a + i.text() + '; '
        count = 0
        a = a + ' '
        for i in inf:
            if i.text() == 'Yellow Toner':
                count = 5
            if count > 0 and i.text() != '':
                count = count - 1
                if count != 1 and count != 3 and count != 4:
                    a = a + i.text() + '; '
        count = 0
        a = a + ' '
        for i in inf:
            if i.text() == 'Drum Cartridge (R1)':
                count = 5
            if count > 0 and i.text() != '':
                count = count - 1
                if count != 1 and count != 3 and count != 4:
                    a = a + i.text() + '; '
        count = 0
        a = a + ' '
        for i in inf:
            if i.text() == 'Drum Cartridge (R2)':
                count = 5
            if count > 0 and i.text() != '':
                count = count - 1
                if count != 1 and count != 3 and count != 4:
                    a = a + i.text() + '; '
        count = 0
        a = a + ' '
        for i in inf:
            if i.text() == 'Drum Cartridge (R3)':
                count = 5
            if count > 0 and i.text() != '':
                count = count - 1
                if count != 1 and count != 3 and count != 4:
                    a = a + i.text() + '; '
        count = 0
        a = a + ' '
        for i in inf:
            if i.text() == 'Drum Cartridge (R4)':
                count = 5
            if count > 0 and i.text() != '':
                count = count - 1
                if count != 1 and count != 3 and count != 4:
                    a = a + i.text() + '; '

        file = open(file_name, "a")
        if os.stat("szit_pars.csv").st_size == 0:
            file.write(' ; Total Impressions; Black Toner; Black Toner; Cyan Toner; Cyan Toner; Magenta Toner; Magenta Toner; Yellow Toner; Yellow Toner; Drum Cartridge (R1); Drum Cartridge (R1); Drum Cartridge (R2); Drum Cartridge (R2); Drum Cartridge (R3); Drum Cartridge (R3); Drum Cartridge (R4); Drum Cartridge (R4)\n')
        current_datetime = date.today()
        file.write(str(current_datetime))
        file.write(';')
        file.write(a)
        file.write('\n')
        file.close()
        print('Parsing is over.')
        sec = 86400 #time u need
        time.sleep(sec)
