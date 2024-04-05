import feedparser, time
from bs4 import BeautifulSoup

URL="https://shkisme.vercel.app/rss.xml"
RSS_FEED = feedparser.parse(URL)

markdown_text = """## 🐈‍⬛ GitHub

<div align = "center">
  
[![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=shkisme&rank_icon=github&include_all_commits=true&count_private=true&show_icons=true&theme=shades-of-purple&show=reviews,discussions_started,discussions_answered,prs_merged,prs_merged_percentage)](https://github.com/anuraghazra/github-readme-stats) 
[![GitHub Streak](https://streak-stats.demolab.com?user=shkisme&theme=shades-of-purple&card_width=350)](https://git.io/streak-stats)  
</div>

"""

markdown_text += """## 📝 Latest Blog Post

<table style="width: 100%; text-align: center;"><tbody><tr>
"""  # list of blog posts will be appended here

MAX_POST = 5

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = time.strftime('%Y/%m/%d', feed['published_parsed'])
        title = feed['title']
        link = feed['link']
        description = feed['description']
      
        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(description, 'html.parser')

        img_tag = soup.find('img')
        img_url = img_tag['src'] if img_tag['src'] != 'https://shkisme.vercel.app/undefined' else './myBlog.png'

        # div 태그 내부의 텍스트 추출하여 summary 설정
        desired_text = soup.find('div').find_next('div').text
        summary = desired_text[:50] + "..." if len(desired_text) > 50 else desired_text
      
        markdown_text += f"""<td style="width: 25%;">
    <a href="{link}">
        <img style="width: 100%; height: auto; aspect-ratio: 16 / 9;" src="{img_url}"/><br/>
        <div align="center" style="font-weight: bold;">{title} <br/> ({feed_date})</div>
    </a>
    {summary}
</td>
"""
        if idx == 2:
          markdown_text += """</tr>
<tr>
"""
        

markdown_text += "</tr></tbody></table>"
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
