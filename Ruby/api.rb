require 'rest-client'

#'https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=0xf0e5096edf070dc9b1bc8911d63c4e448a3e14c6&address=0xBeBed1d2D5E08F9d03e329c52c70e1899B3fe0fC&tag=latest&apikey=2XGIAP1SMH769WPR2KR5NYE2ED6RXG156P'

url      = 'https://api.bscscan.com/api?module='
contract = '0xf0e5096edf070dc9b1bc8911d63c4e448a3e14c6' 
wallet   = '0xBeBed1d2D5E08F9d03e329c52c70e1899B3fe0fC'
api_key  = '2XGIAP1SMH769WPR2KR5NYE2ED6RXG156P'
urlAll = "#{url}account&action=tokenbalance&contractaddress=#{contract}&address=#{wallet}&tag=latest&apikey=#{api_key}"

resp = RestClient.get urlAll

puts resp 