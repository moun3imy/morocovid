# Using PyMuPDF 
# https://github.com/pymupdf/PyMuPDF
# for Code Snippets : https://pymupdf.readthedocs.io/en/latest/tutorial.html
import fitz


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
def process_percentage(string_with_percentage) : 
    #TODO
    pass


    

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


total_excluded_cases = process_number()
new_excluded_cases = process_number()
total_deaths = process_number()
new_deaths = process_number()
total_recovered = process_number()
new_recovered = process_number()
total_active_cases = process_number()
total_cumul_incidence_rate = process_number()
last_24h_incidence_rate = process_number()
case_fatality_rate = process_number()
recovery_rate = process_number()
total_severe_cases = process_number()
last_24h_severe_cases = process_number()
total_under_intubation = process_number()
total_non_invasive_ventilation = process_number()
covid_beds_occupation = process_number()



last_24h_tests = 0
total_24_total_tests = 0


print(text)

print(process_number("some texxxttt here 2 356 861"))
