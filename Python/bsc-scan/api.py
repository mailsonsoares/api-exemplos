import requests
import csv
##Get the balance of a Token from a wallet.
#
# url         = 'https://api.bscscan.com/api?module=account&action='
# action      = 'tokenbalance'
# token       = '0xe9e7cea3dedca5984780bafc599bd69add087d56'
# wallet      = '0x89e73303049ee32919903c09e8de5629b84f59eb'
# tag         = 'latest'
# key         = '8EHHHRD2RHBZPRT287SM4KTSKI9IPVCE4C'
# url_request = (f"{url}{action}&contractaddress={token}&address={wallet}&tag={tag}&apikey={key}")

##Get the total supply of a Token.
#
# url           = 'https://api.bscscan.com/api?module=stats&action='
# action        = 'tokenCsupply'
# token         = '0xf0e5096edf070dc9b1bc8911d63c4e448a3e14c6' #epw
# key           = '8EHHHRD2RHBZPRT287SM4KTSKI9IPVCE4C'
#url_request = (f"{url}{action}&contractaddress={token}&apikey={key}")

#Get a list of 'BEP-20 Token Transfer Events' by Address
url      = 'https://api.bscscan.com/api?module=account&action='
action   = 'tokentx'
token    = '0xe9e7cea3dedca5984780bafc599bd69add087d56' #busd
address  = '0x4E285a4f0A8eA28D6289FDBAE29e5aA5E63d4743'
pg       = '1'
offset   = '0'
block    = '0'
endblock = '9999999999'
sort     = 'asc'
key      = '8EHHHRD2RHBZPRT287SM4KTSKI9IPVCE4C'

url_request = (f"{url}{action}&contractaddress={token}&address={address}&page={pg}&offset={offset}&startblock={block}&endblock={endblock}&sort={sort}&apikey={key}")

response = requests.get(url_request)

# with open('report.csv', 'w') as f:
#     tab = csv.reader(f, delimiter=',')
#     tab.__next__()
#     for line in tab:
#         print(line)

print(response.text)