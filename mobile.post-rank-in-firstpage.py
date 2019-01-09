import requests
import sys
import selenium

from os import system 
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep 
from datetime import datetime

system('cls')

len = int(sys.argv[2]) if (len(sys.argv) > 2) else 10
driver = webdriver.Chrome()
driver.get('https://m.blog.naver.com/SectionPostSearch.nhn?searchValue=' + sys.argv[1])

def time_check():
    now = datetime.now()
    now_time = f"<{now.year}. {now.month}. {now.day} - {now.hour}:{now.minute} 기준 네이버 실시간 블로그 포스팅 순위 ({sys.argv[1]})>"

    return now_time


# html = requests.get('https://m.blog.naver.com/SectionPostSearch.nhn?searchValue=' + sys.argv[1]).text
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
rank_list = soup.select('.list_wrap .list_section .list')[ : len]
ids = ""

print(time_check() + "\n")
for rank, post in enumerate(rank_list, 1):
    head = post.select(".meta_head .dsc .td")
    writer = head[0].find("a")
    id = writer['href'].replace("/", "")
    ids += id + ';'
    print(rank, writer.find("span").text, '(' + id + ')', '\n')

print("아이디 집계 (순위 오름차순)\n", ids, '\n')
