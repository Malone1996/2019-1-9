# 1. 分析网址  岗位名称 页码
# https://search.51job.com/list/000000,000000,0000,00,9,99,岗位名称,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
# https://search.51job.com/list/000000,000000,0000,00,9,99,岗位名称,2,2.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
# 2. 获取所有页页码（字符串替换、正则）   字符串 -> 数字
# 共732页，到第
# str(数字)   int(字符串)
# 3. 采集数据
# 薪资：有可能不存在，则默认为"面议"
# 统一单位   8000-10000元/月   300元/天    300元/时
# 4. 数据存储   csv
# 5. 发邮件（选做）
# 6. 统计每天的工作数量  参考"统计单词数量"逻辑
# 7. 图表展示  pyecharts
import requests
from lxml import etree
import re

url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,3.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
content = requests.get(url)
content.encoding = content.apparent_encoding
content = content.text

root = etree.HTML(content)
jobs = root.xpath("//p/span/a/@title")
companies = root.xpath("//span[@class='t2']/a/@title")
locations = root.xpath("//div[@class='el']/span[@class='t3']/text()")

salaries = root.xpath("//div[@class='el']/span[@class='t4']/text()")
print(salaries[0])
content = f"{salaries[0]}"
print(type(content))
pattern = re.compile(r'(\d+\.?\d*)-(\d+\.?\d*)[万千]')
s = pattern.findall(content)
print(len(s))
print(s)
a = s[0][0]
print(a)
a = int(a)
print(s[0][1])



# if '千' in content:
#     print('true')
#     s1 = int(s[0][0]) * 1000
#     s2 = int(s[0][1]) * 1000


# datas = root.xpath("//div[@class='el']/span[@class='t5']/text()")
#
# for job, company, location, salary, data in zip(jobs, companies, locations, salaries, datas):
#     print(job, company, location, salary, data)
#     f = open("test.csv", "a+", encoding="utf-8")
#     f.write(f"{job},{company},{location},{salary},{data}\n")
#     f.close()


# p_salary_1 = re.compile(r'(\d+\.?\d*)-(\d+\.?\d*)[万千]')
#         str_salary = soup_cn.find('strong').get_text(strip=True)
#         # print(str_salary)
#         r = re.match(p_salary_1, str_salary)
#         # print(r.groups())
#         if r:
#             if '万' in str_salary:
#                 lst_r = [float(i) * 10000 for i in r.groups()]
#
#             else:
#                 lst_r = [float(i) * 1000 for i in r.groups()]
#             offer['salary_from'], offer['salary_to'] = lst_r
#
#         else:
#             offer['is_negotiable'] = True
