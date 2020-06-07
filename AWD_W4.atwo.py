import urllib
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#line 1-8 is copy paste from lecture vidoes ^^

url = input("Enter URL- ")
position = int(input("Enter position: "))
count = int(input("Enter count: "))

#promt user to enter url(link), the position where to extract the url and
#the number of times to repeat this cycle ("count").

for i in range(count): 
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[position-1].get("href")
    result = tags[position-1].string

print(result)

#Answer 'RICE'
