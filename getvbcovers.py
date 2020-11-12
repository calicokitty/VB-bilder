import requests
from lxml import etree

vburl = 'https://res.cloudinary.com/forlagshuset/image/upload/q_auto:best/'
path = '//Sindre/OmslagsbilderTilAja/'
jpg = '.jpg'

# Creates a url to get SRU
def get_isbns():
    server = 'https://sru.aja.bs.no/mlnb'
    version = '1.1'
    maxrec = '10'
    schema = 'marc21'
    query = "bs.level=full%20AND%20dc.identifier=97882419*%20AND%20bs.has_cover=false"
    url = server + '?version=' + version + '&operation=searchRetrieve' + '&maximumRecords=' + maxrec
    url = url + '&recordSchema=' + schema + '&query=' + query
    r = requests.get(url)
    tree =  etree.fromstring(r.text)

    # Dictionary for namespaces (prefix : URI)
    namespaces = {'marc21' : 'info:lc/xmlns/marcxchange-v1'}
    xpath = '//marc21:datafield[@tag = "020"]/marc21:subfield[@code ="a"]'
    return tree.xpath(xpath, namespaces = namespaces)

def get_images_from_vb(_isbns):
    for isbn in _isbns:
        r = requests.get(vburl+str(isbn.text), allow_redirects=True)
        # print("url: ", r.url)
        # print('Status r:', r.status_code)
        if r:
            upload_images_to_aja(isbn.text, r.content)
        
def upload_images_to_aja(_isbn, _content):
    open(path + str(_isbn)+jpg, 'wb').write(_content)

get_images_from_vb(get_isbns())
