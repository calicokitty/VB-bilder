import requests
from lxml import etree

server = 'https://sru.aja.bs.no/mlnb'
version = '1.1'
maxrec = '100'
schema = 'marc21'
query = "dc.identifier=97882419*%20AND%20bs.has_cover=true"

url = server + '?version=' + version + '&operation=searchRetrieve' + '&maximumRecords=' + maxrec
url = url + '&recordSchema=' + schema + '&query=' + query

print(url)

parser = etree.XMLParser(encoding='utf-8')

r = requests.get(url)
tree = etree.fromstring(r.text)

# Dictionary for namespaces (prefix : URI)

namespaces = {'marc21' : 'info:lc/xmlns/marcxchange-v1'}

xpath = '//marc21:datafield[@tag = "020"]/marc21:subfield[@code ="a"]'

isbns = tree.xpath(xpath, namespaces = namespaces)

for isbn in isbns:
    print(isbn.text)