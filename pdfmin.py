"""
Extract PDF text using PDFMiner. Adapted from
http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
"""



from pdfminer.high_level import extract_text 
text = extract_text('D:\morocovid\pdfBulletins\corona1.pdf')

print(text)