# Using PyMuPDF 
# https://github.com/pymupdf/PyMuPDF
# for Code Snippets : https://pymupdf.readthedocs.io/en/latest/tutorial.html
import fitz
import re


#TODO generate all today's data (including cases for each city) in json format 
#TODO generate it for every day since september
""" 
takes a string containing a number (whose digits may be separated by spaces, like "some texxt here 2 356 861")
and returns the number within it (in previous example returns 2356861)

"""
def process_number(string_with_number) : 
    list_strings = string_with_number.split()
    final_string =  ""
    for s in list_strings : 
        if s.isdigit() : 
            final_string += s

    return int(final_string)


""" 
takes a string containing a percentage (like "some texxt here 1,7%", "some random txt here 37%")
and returns the percentage within it (in previous examples returns "1,7%", "37%")

"""
#\d+(?:(\.|,)\d+)?%
#\d+(\.|.)*\d*
def process_percentage(string_with_percentage) : 
    list_percentages = re.findall(r"\d+(?:,*\d+)?%",string_with_percentage)
    if len(list_percentages) == 1 : 
        return list_percentages[0]


    
""" print(process_percentage("kjdshjfdhfkdfs 1%"))
print(process_percentage("kjdshjfdhfkdfs 37,0%"))
print(process_percentage("jhfdjksfhkjhdfh 36,35% jhfgkjhfdjgdf"))
print(process_percentage("kdfjkdsjfkdsf 36,35% jhhfsdfkh")) """


""" 
takes a string containing an incidence factor (like "some texxt here 150/100000 ", "some random txt here 110,15/100000 ")
and returns the incidence factor within it (in previous examples returns "150/100000", "110,15/100000")

"""
def process_incidence(string_with_incidence) : 
    list_incidences = re.findall(r"\d+(?:,*\d+)?/100\.000",string_with_incidence)
    if len(list_incidences) == 1 : 
        return list_incidences[0]

    
""" 
print(process_incidence("kjdshjfdhfkdfs 12,12/100.000%"))
print(process_incidence("kjdshjfdhfkdfs 15/100.000"))
print(process_incidence("jhfdjksfhkjhdfh 10/100000 jhfgkjhfdjgdf"))
print(process_incidence("kdfjkdsjfkdsf 17.0/100.000 jhhfsdfkh")) """

    
total_cases = 0
new_cases = 0
total_excluded_cases = 0
new_excluded_cases = 0
total_deaths = 0
new_deaths = 0
total_recovered = 0 
new_recovered = 0
total_active_cases = 0
total_cumul_incidence_rate = 0
last_24h_incidence_rate = 0
case_fatality_rate = 0
recovery_rate = 0
total_severe_cases = 0
last_24h_severe_cases = 0
total_under_intubation = 0
total_non_invasive_ventilation = 0
covid_beds_occupation = 0
last_24h_tests = 0
total_24_total_tests = 0

doc = fitz.open("D:\morocovid\pdfBulletins\corona_11-11-20")


for page in doc :
    text = page.getText()
    break
text = text.split("\n")
for i in range(len(text)) : 
    if 'Cas conf' in text[i] : 
        total_cases_str = text[i+1]
        new_cases_str = text[i+2]
        
    elif 'Cas exclus' in text[i] :
        total_excluded_cases_str = text[i+1]
        new_excluded_cases_str = text[i+2]
         
    elif 'Décès' in text[i] : 
        total_deaths_str = text[i+1]
        new_deaths_str = text[i+2]
        
    elif 'Guéris' in text[i] : 
        total_recovered_str = text[i+1]
        new_recovered_str = text[i+2]
        
    elif 'Cas actifs' in text[i] : 
        total_active_cases_str = text[i+1]
        
    elif  'Incidence cumul' in text[i] : 
        total_cumul_incidence_rate_str = text[i+1] 
        
    elif  'Incidence de 24H' in text[i] : 
        last_24h_incidence_rate_str = text[i+1] 
        
    elif  'Taux de létalité' in text[i] : 
        case_fatality_rate_str = text[i+1]
        
    elif  'Taux de guérison' in text[i] : 
        recovery_rate_str = text[i+1]
        
    elif  'Nombre total' in text[i] : 
        total_severe_cases_str = text[i+1]
        
    elif  'Les nouveaux cas de 24 heures' in text[i] : 
        last_24h_severe_cases_str = text[i+1]
        
    elif 'intubation' in text[i] : 
        total_under_intubation_str = text[i+1]
    
    elif 'invasive' in text[i] : 
        total_non_invasive_ventilation_str = text[i+1]

    elif 'réanimation dédiés' in text[i] : 
        covid_beds_occupation_str = text[i+1]
    

total_cases = process_number(total_cases_str)
new_cases = process_number(new_cases_str)
total_excluded_cases = process_number(total_excluded_cases_str)
new_excluded_cases = process_number(new_excluded_cases_str)

last_24h_tests = new_excluded_cases + new_cases
total_tests = total_excluded_cases + total_cases


total_deaths = process_number(total_deaths_str)
new_deaths = process_number(new_deaths_str)
total_recovered = process_number(total_recovered_str)
new_recovered = process_number(new_recovered_str)
total_active_cases = process_number(total_active_cases_str)
total_cumul_incidence_rate = process_incidence(total_cumul_incidence_rate_str)
last_24h_incidence_rate = process_incidence(last_24h_incidence_rate_str)
case_fatality_rate = process_percentage(case_fatality_rate_str)
recovery_rate = process_percentage(recovery_rate_str)
total_severe_cases = process_number(total_severe_cases_str)
last_24h_severe_cases = process_number(last_24h_severe_cases_str)
total_under_intubation = process_number(total_under_intubation_str)
total_non_invasive_ventilation = process_number(total_non_invasive_ventilation_str)
covid_beds_occupation = process_percentage(covid_beds_occupation_str)





print(" total_cases: ",total_cases)
print(" new_cases: ",new_cases)
print("total_excluded_cases:  ",total_excluded_cases)
print(" new_excluded_cases:  ",new_excluded_cases)
print("total_deaths:  ",total_deaths)
print("new_deaths:  ",new_deaths)
print("total_recovered:  ",total_recovered)
print("new_recovered:  ",new_recovered)
print("total_active_cases:  ",total_active_cases)
print("total_cumul_incidence_rate:  ",total_cumul_incidence_rate)
print("last_24h_incidence_rate:  ",last_24h_incidence_rate)
print("case_fatality_rate:  ",case_fatality_rate)
print("recovery_rate:  ",recovery_rate)
print("total_severe_cases:  ",total_severe_cases)
print("last_24h_severe_cases:  ",last_24h_severe_cases)
print("total_under_intubation:  ",total_under_intubation)
print("total_non_invasive_ventilation:  ",total_non_invasive_ventilation)
print("covid_beds_occupation:  ",covid_beds_occupation)
print("last_24h_tests:  ",last_24h_tests)
print("total_tests:  ",total_tests)





