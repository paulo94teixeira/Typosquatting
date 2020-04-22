import socket
import sys
import requests

print('Argument List:', str(sys.argv[1]))

host = sys.argv[1]

addr1 = socket.gethostbyname(host)

print('Ip --> ' + str(addr1))
print('##################')

URL = 'https://ipinfo.io/'+ addr1 +'/geo'

r = requests.get(url = URL)

res = r.json()

print("Country Code --> " + res['country'])
print("Lat/Long --> " + res['loc'])

URL = 'https://rdap.arin.net/registry/ip/'+ addr1

r = requests.get(url = URL)

res = r.json()

print("Start Address --> " + res['startAddress'])
print("End Address --> " + res['endAddress'])
print("Name --> " + res['name'])
print('##########' + 'Last events' + '##########')

for i in range(len(res['events'])):
	evento = res['events'][i]
	print("------------------" + "event number " + str(i + 1) + "------------------")
	print("Event action --> " + evento['eventAction'])
	print("Event date --> " + evento['eventDate'])


#ir buscar a handle e o vcardarray(address)


