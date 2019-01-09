import requests
from lxml import etree
import re

url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
content = requests.get(url)
content.encoding = content.apparent_encoding
content = content.text
root = etree.HTML(content)
# yema = root.xpath("//div[@class='p_in']/span[@class='td']/text()")
yema = root.xpath("//span[@class='td']/text()")
print(type(yema))
# print(yema)
context = f"{yema}"
print(type(content))
# print(content)

# yema = int(yema)
pattern = re.compile(r"\d{1,}")
result = pattern.findall(context)
print(result[0])
result = int(result[0])
print(type(result))
