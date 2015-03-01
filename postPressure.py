import requests
 
# fill in the appropriate values from your data.sparkfun.com data stream
publicKey = 'G2pKDamRDDUwKy7aMdy5'
privateKey = ''
dataLabel = 'pressure'
 
# Weather location, see openweathermap.org/current for more information
location = 'Edmonton,ca'
weatherUnits = 'metric'
 
# get weather data in JSON format
weatherUrl = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=' + location + '&units=' + weatherUnits + '&cnt=1'
weather = requests.get(weatherUrl).json()
pressure = str(weather['list'][0]['pressure'])
 
# log the data
pushUrl = 'https://data.sparkfun.com/input/' + publicKey + '?private_key=' + privateKey + '&' + dataLabel + '=' + pressure
push = requests.get(pushUrl)
