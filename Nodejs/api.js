
var Client = require('node-rest-client').Client;
var client = new Client();

let url      = 'https://api.bscscan.com/api?module='
let contract = '0xf0e5096edf070dc9b1bc8911d63c4e448a3e14c6' 
let wallet   = '0xBeBed1d2D5E08F9d03e329c52c70e1899B3fe0fC'
let api_key  = '2XGIAP1SMH769WPR2KR5NYE2ED6RXG156P'
let urlAll = `${url}account&action=tokenbalance&contractaddress=${contract}&address=${wallet}&tag=latest&apikey=${api_key}`

// registering remote methods
client.registerMethod("jsonMethod", urlAll, "POST");

client.methods.jsonMethod(function (data, response) {
    // parsed response body as js object
    console.log(data);
    // raw response
    //console.log(response);
});