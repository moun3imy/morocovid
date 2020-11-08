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
""" with open(filename, 'wb') as f:
    response = requests.get(final_url,headers = headers).content
    print(response)
    f.write(response) """
# analyze the pdf
# this will generate the data in csv format in the file output.csv
tabula.convert_into("pdfBulletins/corona1.pdf", "output.csv", output_format="csv", pages=[2,3,4],java_options="-Dfile.encoding=UTF8")
# get general statistics from the pdf file
tabula.convert_into("pdfBulletins/corona1.pdf", "stats-corona.csv", output_format="csv", pages=[1],java_options="-Dfile.encoding=UTF8")
# send it by mail to me
df = pd.read_csv("output.csv")
# delete header rows
updated_df = df.drop([df.index[0],df.index[1],df.index[2]])
# rename columns
updated_df.columns = [ "Régions","Nouveaux Cas","Décès","Régions Ar"]
# replace NaN with 0
updated_df = updated_df.fillna(0)
#write data to corona.csv
updated_df.to_csv("corona.csv",index=True)
print(updated_df)






# TODO analyse the page at "http://www.covidmaroc.ma/Pages/LESINFOAR.aspx"
# get all the pdf links and download them, without folowwing the pattern of the url using BeautifulSoup Library