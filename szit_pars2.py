from LxmlSoup import LxmlSoup
from datetime import date
import requests
import os

url = "https://www.wolframalpha.com/"
file_name = "szit_pars2.txt"

r = requests.get(url).text
if r == 200:
    print('Error! Run to administrator!')
else:
    print('Parsing is starting...')

soup = LxmlSoup(r)
inf = soup.find_all('a')
print(inf)

file = open(file_name, "a")
if os.stat("szit_pars2.txt").st_size == 0:
    file.write(' ;\n')
file.close()
