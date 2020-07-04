import csv
import wget

#open import file
with open("D:/PYTHON PROGRAMMING/data/Scrapping/Himawari_scraping5.csv", newline='', encoding='utf-8') as f:

#Assign the import file to the DictReader "reader"
    reader = csv.DictReader(f)

#loop through all rows and build out variables
    for row in reader:
        filename = row['Nama File'] + '.jpg'
        url = 'https://www.data.jma.go.jp/mscweb/data/himawari/img/r2w/'
        wget.download(url + filename, 'Himawari-8 ' + filename)
