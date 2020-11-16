import requests
from lxml import etree

aja_sru_url = 'https://sru.aja.bs.no/mlnb'
vb_url = 'https://res.cloudinary.com/forlagshuset/image/upload/q_auto:best/{isbn}'
destination_path = '//Sindre/OmslagsbilderTilAja/{isbn}.jpg'

def get_isbns():
    # Retrieves up to `maximumRecords` isbns for records missing cover in Ája Catmandu
    query = 'bs.level = full AND dc.identifier=97882419* AND bs.has_cover=false'
    r = requests.get(aja_sru_url, params={
        'vesion': '1.1',
        'operation': 'searchRetrieve',
        'maximumRecords': '50',
        'recordSchema': 'marc21',
        'query': query,
    })
    tree =  etree.fromstring(r.text)

    # Dictionary for namespaces (prefix : URI)
    namespaces = {'marc21' : 'info:lc/xmlns/marcxchange-v1'}
    xpath = '//marc21:datafield[@tag = "020"]/marc21:subfield[@code ="a"]'
    return [node.text for node in tree.xpath(xpath, namespaces = namespaces)]

def get_image_from_vb(isbn):
    r = requests.get(vb_url.format(isbn=isbn), allow_redirects=True)
    # print("url: ", r.url)
    # print('Status r:', r.status_code)
    if r.ok:
        return r.content
    else:
        return None
        
def store_image(isbn, content):
    with open(destination_path.format(isbn=isbn), 'wb') as fp:
        fp.write(content)

for isbn in get_isbns():
    if image := get_image_from_vb(isbn):
        store_image(isbn, image)
