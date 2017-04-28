#python3
import urllib.request
url="http://www.webservicex.net/country.asmx/GetCountries"
data=urllib.request.urlopen(url).read()
z_data=data.decode('UTF-8')  
print(data)
