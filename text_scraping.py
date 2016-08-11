# sample_text_scraping
# This piece of code is written to help you to extract the text from a htmp page which is stored in your hard disk.
# Please remember that depending on the strucure of the html page the elemet that you should specify for the text sraping is different.
# Authour: Mahboobeh "Mabi" Harandi

from bs4 import BeautifulSoup
import re
import fileinput


def TextScrape():
    textfile = open('Test_Scraping.txt', 'w')
    page = open('My Web Sites/www.test.com/test.html', 'r')
    docs = page.read()
    soup = BeautifulSoup(docs, 'html.parser')
    texts = soup.findAll("div", { "class": "issue-list-issue__img-wrap" })
    text_file = []
    for text in texts:
        text_file.append(''.join(text.findAll(text=True)))
    for item in text_file:
        textfile.write(item)
    
TextScrape()        
