
from pdfminer.high_level import extract_text

text = extract_text('pdfBulletins/corona1.pdf')

print(text)

""" if sys.version_info > (3, 0):  
    from io import StringIO
else:
    from io import BytesIO as StringIO
output_string = StringIO()
with open('pdfBulletins/corona1.pdf', 'rb') as fin:
     high_level.extract_text_to_fp(fin, output_string)
print(output_string.getvalue().strip()) """


""" 
scraping_folder = path.join(path.dirname(__file__), 'pdfBulletins')
output_file = path.join(path.dirname(__file__),'out_text.txt')
#return the text in the first page of the pdf
text = extract_text(files = [scraping_folder],page_numbers = [1],out_file=output_file) """