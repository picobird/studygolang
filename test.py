# -- coding: utf-8 --
import urllib.request
import csv
import re
from bs4 import BeautifulSoup

url = "http://idol001.com/xingcheng/list/star-exo-6730/"
data = urllib.request.urlopen(url).read()
data = data.decode('utf-8')
# data = data.decode('gbk', 'ignore').encode('utf-8')
print(data)
soup = BeautifulSoup(data, "lxml")
table = soup.find("table", {"class": "schedule-table"})
# print(table)

with open('output.csv', 'w') as f:
    csv_writer = csv.writer(f)

    td_th = re.compile('t[dh]')

    for row in table.findAll("tr"):
        cells = row.findAll(td_th)
        if len(cells) == 6:
            travel_date = cells[0].find(text=True)
            travel_time = cells[1].find(text=True)
            travel_content = cells[2].find(text=True)
            travel_type = cells[3].find(text=True)
            travel_address = cells[4].find(text=True)
            travel_res = cells[5].find(text=True)

            csv_writer.writerow([travel_date, travel_time,
                                 travel_content, travel_type,
                                 travel_address, travel_res])

    f.close()
