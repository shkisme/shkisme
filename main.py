import feedparser, time
from bs4 import BeautifulSoup

URL="https://rss.app/feeds/Pdrvizv67oA5fYy9.xml" 
RSS_FEED = feedparser.parse(URL)

markdown_text = """

## 🐈‍⬛ GitHub

<div align = "center">
  
[![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=shkisme&rank_icon=github&include_all_commits=true&count_private=true&show_icons=true&theme=shades-of-purple&show=reviews,discussions_started,discussions_answered,prs_merged,prs_merged_percentage)](https://github.com/anuraghazra/github-readme-stats) 
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=shkisme&layout=donut&theme=shades-of-purple&langs_count=6&private=true&exclude_repo=Embedded-term)](https://github.com/anuraghazra/github-readme-stats)
  
</div>

"""

markdown_text += """

## 📝 Latest Blog Post
<table><tbody><tr>
"""  # list of blog posts will be appended here

MAX_POST = 6

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

        # img 태그가 있는지 확인하고 img_url 설정
        img_tag = soup.find('img')
        image_url = img_tag['src']

        # div 태그 내부의 텍스트 추출하여 summary 설정
        div_tag = soup.find('div')
        text_content = div_tag.get_text(separator=' ', strip=True)
        summary = text_content[:50] + "..." if len(text_content) > 50 else text_content
      
        markdown_text += f"""
<td>
    <a href="{link}">
        <img width="100%" src="{image_url}"/><br/>
        <div>{title}</div>
    </a>
    <div>{feed['summary']}</div>
    <div>{feed_date}</div>
</td>
"""
        if (idx == 3):
          markdown_text += """
</tr>
<tr>
"""
        

markdown_text += "</tr></tbody></table>"
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
