# 老师给的代码
import requests
from lxml import etree
import re

url = "https://www.dy2018.com/html/gndy/dyzz/index.html"
content = requests.get(url).text
root = etree.HTML(content)
pages = root.xpath("//select/option/@value")
f = open("movie.csv", "w")
num = 1
for page in pages:
    url = "https://www.dy2018.com" + page
    content = requests.get(url)
    content.encoding = content.apparent_encoding
    content = content.text
    root = etree.HTML(content)
    movie_titles = root.xpath("//b/a/@title")
    movie_hrefs = root.xpath("//b/a/@href")
    for movie_title, movie_href in zip(movie_titles, movie_hrefs):
        pattern = re.compile(r"《(.*?)》")
        if "《" in movie_title and "》" in movie_title:
            movie_title = pattern.findall(movie_title)[0]

        movie_href = "https://www.dy2018.com" + movie_href
        content = requests.get(movie_href)
        content.encoding = content.apparent_encoding
        content = content.text
        if content:
            root = etree.HTML(content)
            download_url = root.xpath("//td[@bgcolor='#fdfddf']/a/text()")
            if download_url:
                download_url = download_url[0]
                print(movie_title, download_url)
                f.write(str(num) + ',' + movie_title + ',' + download_url + '\n')
                f.flush()  # 将缓冲区的内容立即写入文件并清空缓冲区
                num += 1
f.close()
