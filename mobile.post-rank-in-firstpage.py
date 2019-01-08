import requests
import sys
import selenium

from os import system 
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep 
from datetime import datetime

driver = webdriver.Chrome()
driver.get('https://m.blog.naver.com/SectionPostSearch.nhn?searchValue=' + sys.argv[1])

def time_check():
    now = datetime.now()
    now_time = f"<{now.year}. {now.month}. {now.day} - {now.hour}:{now.minute} 기준 네이버 실시간 블로그 포스팅 순위 ({sys.argv[1]})>"

    return now_time

while True:
    # html = requests.get('https://m.blog.naver.com/SectionPostSearch.nhn?searchValue=' + sys.argv[1]).text
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    rank_list = soup.select('.list_wrap .list_section .list')[ : 10]
    
    print(time_check() + "\n")
    for rank, post in enumerate(rank_list, 1):
        print(post.find('.meta_head .dsc .writer .ell'))
        # print(post.find('.td .writer .ell').text)
        # infos = post.select(".txt_block .inline a")
        # print(rank, infos[0].text, infos[0]['href'])
        
    sleep(10)
    system('cls')
    print("\n")