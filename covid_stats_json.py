import utils
import read_stats 
from os import path
import csv

# taken from https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-in-python-taking-union-o
# I prefered this over final_data = {**national_data,**cities_data} because this is supported from Python >= 3.5
# while this function is backward compatible
def merge_two_dicts(x, y):
    """Given two dictionaries, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

"""
generates all coronavirus-2 data for some date
date is provided in "dd-MM-yy" format with non padding zero when day or month are <10
"""
def get_coronavirus_json(date) : 
    csv_filename = "corona_{}.csv".format(date)
    pdf_filename = "corona_{}.pdf".format(date)
    #construct the file name 
    scraping_folder = path.join(path.dirname(__file__), 'CSVs')
    print ("scraping folder : ", scraping_folder)
    filename_path = path.join(scraping_folder,csv_filename)
    print("complete csv file path is : ", filename_path)

    if not path.isfile(filename_path) : 
        print("error : the file for this date does not exist, please check the date format is correct")
        return None

    # read csv file and convert it to json
    with open(filename_path,mode = 'r',encoding = 'utf-8') as file :
        cities_data = {}
        reader = csv.reader(file)
        iteration = 0
        for row in reader : 
            #skip the header row
            if iteration == 0 :
                iteration+=1 
                continue
            #print(row)
            cities_data [row[1]] = {'new_cases' : int(row[2]),'deaths' : int(row[3])}

    # read national covid-19 data from read_stats.read_stats()
    national_data = read_stats.read_stats(pdf_filename)

    # merge the two into one single json
    final_data = merge_two_dicts(national_data,cities_data)
    return final_data
if __name__ == "__main__":
    #print(get_coronavirus_json(utils.today()))
    print(get_coronavirus_json(utils.today()))