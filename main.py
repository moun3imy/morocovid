"""
this script will : 
1. download the coronavirus data from moroccan ministry of health PDF files
2. extract the data in the PDF files using tabula-py library (a wrapper around tabula-java library)
3. will clean the data extracted from the PDF files using pandas library
4. export the final data to a CSV file in the same directory
5. TODO export the data in JSON format
6. TODO make a REST API out of this data

"""

import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from os import path
import datetime
import tabula
import pandas as pd

""" 
cleans the data provided by tabula-py, in case there are errors or missing columns
"""
def clean_output() : 
    with open('output.csv',mode = 'rt', encoding='UTF-8') as f : 
        with open('output2.csv',mode = 'w+', encoding='UTF-8') as out : 
            x = 1
            for line in f :
                # skip the first 4 lines, which are just titles
                if x < 5 : 
                    x+=1
                    continue
                    
                values = line.split(",")
                #print(values)
                if len(values) == 4 : 
                    if len(values[2].replace(" ","")) == 0 : 
                        values[2] = '0'
                    final_line = ",".join(values)
                elif len(values) == 3 : 
                    #values[1] is either a 2 consecutive digits like "Kénitra,352 5,القنيطرة"
                    # or just 1 digit, in which case, we must add a 0 after it for the number of deaths like "Benslimane,39,بن سليمان"
                    numbers = [int(s) for s in values[1].split() if s.isdigit()]
                    if len(numbers) == 1 : 
                        values = [values[0],str(numbers[0]),'0',values[2]]
                        final_line = ",".join(values)
                    elif len(numbers) == 2 : 
                        values = [values[0],str(numbers[0]),str(numbers[1]),values[2]]
                        final_line = ",".join(values)
                out.write(final_line)

url = "http://www.covidmaroc.ma/Pages/LESINFOAR.aspx"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
base_url_november = "http://www.covidmaroc.ma/Documents/BULLETIN/BQ_COVID.{0}.{1}.{2}.pdf"
 
# if there is no such folder, the script will create one automatically
scraping_folder = path.join(path.dirname(__file__), 'pdfBulletins')
# make the folder 
if not os.path.exists(scraping_folder):
    os.mkdir(scraping_folder)
filename = path.join(scraping_folder,"corona1.pdf")



# get the date and format it accordingly to the url pattern
now = datetime.datetime.now()
day = now.strftime("%d").lstrip("0")
month = now.strftime("%m").lstrip("0")
year = now.strftime("%y")

#construct the url for the bulletin of today
final_url = base_url_november.format(day,month,year)

print(final_url)

#get the pdf
with open(filename, 'wb') as f:
    response = requests.get(final_url,headers = headers).content
    print(response)
    f.write(response)
# analyze the pdf
# this will generate the data in csv format in the file output.csv
tabula.convert_into("pdfBulletins/corona1.pdf", "output.csv", output_format="csv", pages=[2,3,4],java_options="-Dfile.encoding=UTF8")
# read corona.csv to fix it (when the pdf reading file contains only 2 commas, add 0 and a second comma)
clean_output()
df = pd.read_csv("output2.csv", header = None)

# rename columns
df.columns = [ "Régions","Nouveaux Cas","Décès","Régions Ar"]
# replace NaN with 0
df = df.fillna(0)
#write data to corona.csv
df.to_csv("corona.csv",index=True)
print(df)






# TODO analyse the page at "http://www.covidmaroc.ma/Pages/LESINFOAR.aspx"
# get all the pdf links and download them, without folowwing the pattern of the url using BeautifulSoup Library