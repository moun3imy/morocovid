
from datetime import datetime,timedelta
import time 
import requests
import os
# 4/9 to 30/9
first_format = "http://www.covidmaroc.ma/Documents/BULLETIN/BQ_SARS-CoV-2.{0}.{1}.20.pdf" 
# 1/10 to 7/10
second_format = "http://www.covidmaroc.ma/Documents/BULLETIN/BQ_COVID.OCTOB.{0}.20.pdf" 
# 8/10 to 31/10
third_format = "http://www.covidmaroc.ma/Documents/BULLETIN/BQ_COVID.OCTOB_{0}-20.pdf" 
#1/11 to 15/11
fourth_format = "http://www.covidmaroc.ma/Documents/BULLETIN/BQ_COVID.{0}.{1}.20.pdf" 
#16/11 to
fifth_format = "http://www.covidmaroc.ma/Documents/BULLETIN/BQ_COVID_{0}-{1}-20.pdf"


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

start_date = "04-09-2020"
end_date = "10-09-2020"

start = datetime.strptime(start_date,"%d-%m-%Y")
end = datetime.strptime(end_date,"%d-%m-%Y")

date = start

#  iterate through all the dates since 4/9/2020
#  construct the proper URL

while date <= end : 
    if datetime(2020,9,4)<=date and date <= datetime(2020,9,30) : 
        url = first_format.format(str(date.day), str(date.month))
    elif datetime(2020,10,1)<=date and date <= datetime(2020,10,7) : 
        url = second_format.format(str(date.day))
    elif datetime(2020,10,8)<=date and date <= datetime(2020,10,31) : 
        url = third_format.format(str(date.day))
    elif datetime(2020,11,1)<=date and date <= datetime(2020,11,15) : 
        url = fourth_format.format(str(date.day), str(date.month))
    elif datetime(2020,11,16) <= date  : 
        url = fifth_format.format(str(date.day), str(date.month))
    filename = "corona_" + str(date.day) + "-" + str(date.month) + "-20.pdf"
    print(url)

    scraping_folder = os.path.join(os.path.dirname(__file__), 'pdfs')
    # make the folder 
    if not os.path.exists(scraping_folder):
        os.mkdir(scraping_folder)
    filename = os.path.join(scraping_folder,filename)

    # request the url and store the pdf file in pdfs/corona_{day}_{month}_{year}.pdf file
    with open(filename, 'wb') as f:
        response = requests.get(url,headers = headers)
        if response.status_code == 200 : 
            f.write(response.content)
        else : 
            print("Invalid URL or unresponsive server")    

    date = date + timedelta(days=1)
    time.sleep(5)











