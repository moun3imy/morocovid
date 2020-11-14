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
import utils

""" 
cleans the data provided by tabula-py, in case there are errors or missing columns
"""
def clean_output(output) : 
    with open(output,mode = 'rt', encoding='UTF-8') as f : 
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

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
today = utils.today()

pdf_file = utils.get_todays_pdfFileName()

#construct the url for the bulletin of today
final_url = utils.get_url()

# if there is no such folder, the script will create one automatically
scraping_folder = path.join(path.dirname(__file__), 'pdfBulletins')
csv_folder  = path.join(path.dirname(__file__),"CSVs")
# make the folder 
if not os.path.exists(scraping_folder):
    os.mkdir(scraping_folder)
if not os.path.exists(csv_folder):
    os.mkdir(csv_folder)
filename = path.join(scraping_folder,pdf_file)

print(final_url)
print(filename)

#get the pdf
with open(filename, 'wb') as f:
    response = requests.get(final_url,headers = headers).content
    f.write(response)
# analyze the pdf
# this will generate the data in csv format in the file output.csv
output_file = "output_" + today + ".csv"
tabula.convert_into(filename, output_file, output_format="csv", pages=[2,3,4],java_options="-Dfile.encoding=UTF8")
# read output.csv to fix it (when the pdf reading file contains only 2 commas, add 0 and a second comma)
#TODO think when there are no cases nor deaths, or when there are no cases but there are deaths
clean_output(output_file)
# output1 is an itermediary file
df = pd.read_csv("output2.csv", header = None)
# rename columns
df.columns = [ "Régions","Nouveaux Cas","Décès","Régions Ar"]
# replace NaN with 0 (this is because the number of deaths is not entred when there are not any)
df = df.fillna(0)
#write data to corona_today.csv
final_corona_data = "corona_" + today + ".csv"
final_csv_path = path.join(csv_folder,final_corona_data)
df.to_csv(final_csv_path,index=True)
print(df)






# TODO analyse the page at "http://www.covidmaroc.ma/Pages/LESINFOAR.aspx"
# get all the pdf links and download them, without folowwing the pattern of the url using BeautifulSoup Library