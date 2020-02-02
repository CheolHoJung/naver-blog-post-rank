import sys

from os import system 
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep 
from datetime import datetime

system('cls')

argSize = len(sys.argv)
lastArg = sys.argv[argSize - 1]

if lastArg.isdigit():
    len = int(lastArg)
    keywords = sys.argv[1 : argSize - 1]
else:
    len = 10
    keywords = sys.argv[1 : ]

def getTime() :
    now = datetime.now()
    now_time = f"{now.year}. {now.month}. {now.day}"
    return now_time

def getBlogIdInQueryString(queryString) :
	return next(
		map(lambda qs: qs.split("=")[1],
		filter(lambda qs: qs.split("=")[0] == "blogId", queryString)))

searchTime = getTime()

result = "%-20s%-10s%-20s\n" % ("날짜", "키워드", "아이디")
driver = webdriver.Chrome()

for keyword in keywords:
	driver.get('https://m.blog.naver.com/SectionPostSearch.nhn?searchValue=' + keyword)
	driver.implicitly_wait(3)
	sleep(3)
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	posts = soup.select('.list_wrap .item .postlist')[ : len]

	for post in posts:
		href = post.find("a")["href"]
		queryString = href.split("?")[1].split("&")
		id = getBlogIdInQueryString(queryString)
		result += "%-20s%-10s%-20s\n" % (searchTime, keyword, id)

driver.quit()
print(result)


