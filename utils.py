
import datetime

def today() : 
    today_str = "{0}-{1}-{2}"
    # get the date and format it accordingly to the url pattern
    now = datetime.datetime.now()
    day = now.strftime("%d").lstrip("0")
    month = now.strftime("%m").lstrip("0")
    year = now.strftime("%y")

    today_str = today_str.format(day,month,year)
    return today_str
def get_todays_pdfFileName() : 
    today_str = today()
    pdf_file = "corona_" + today_str + ".pdf"
    return pdf_file

def get_url() : 
    now = datetime.datetime.now()
    day = now.strftime("%d").lstrip("0")
    month = now.strftime("%m").lstrip("0")
    year = now.strftime("%y")
    base_url_november = "http://www.covidmaroc.ma/Documents/BULLETIN/BQ_COVID.{0}.{1}.{2}.pdf"
    final_url = base_url_november.format(day,month,year)
    return final_url