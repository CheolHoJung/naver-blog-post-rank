import requests
import sys
from os import system 
from bs4 import BeautifulSoup
from time import sleep 
from datetime import datetime

def time_check():
    now = datetime.now()
    now_time = f"<{now.year}. {now.month}. {now.day} - {now.hour}:{now.minute} 기준 네이버 실시간 블로그 포스팅 순위 ({sys.argv[1]})>"

    return now_time

while True:
    html = requests.get('https://search.naver.com/search.naver?where=post&sm=tab_jum&query=' + sys.argv[1]).text
    soup = BeautifulSoup(html, 'lxml')
    rank_list = soup.select('.blog.section._blogBase._prs_blg #elThumbnailResultArea .sh_blog_top')

    print(time_check() + "\n")
    for rank, post in enumerate(rank_list, 1):
        infos = post.select(".txt_block .inline a")
        print(rank, infos[0].text, infos[0]['href'])
    sleep(10)
    system('cls')
    print("\n")