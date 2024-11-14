import feedparser, time
from bs4 import BeautifulSoup

URL="https://shkisme.vercel.app/rss.xml"
RSS_FEED = feedparser.parse(URL)

markdown_text = """
## [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fshkisme&count_bg=%23DAB628&title_bg=%232D2B55&icon=github.svg&icon_color=%23E7E7E7&title=GitHub&edge_flat=false)](https://hits.seeyoufarm.com)

<div align = "center">
[![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=shkisme&rank_icon=github&include_all_commits=true&count_private=true&show_icons=true&theme=shades-of-purple&show=reviews,discussions_started,discussions_answered,prs_merged,prs_merged_percentage)](https://github.com/anuraghazra/github-readme-stats) 
[![GitHub Streak](https://streak-stats.demolab.com?user=shkisme&theme=shades-of-purple&card_width=350)](https://git.io/streak-stats)  
</div>

"""

markdown_text += """
## 📝 Latest [Blog](https://shkisme.vercel.app/) Posts

<div align = "center">
  <table style="width: 100%; text-align: center;"><thead>
  <tr>
      <th>Title</th>
      <th>Date</th>
      <th>Description</th>
  </tr>
  </thead><tbody>
"""  # list of blog posts will be appended here

MAX_POST = 5

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break

    feed_date = time.strftime('%Y/%m/%d', feed['published_parsed'])
    title = feed['title']
    link = feed['link']
    description = feed['description']
  
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(description, 'html.parser')

    # div 태그 내부의 텍스트 추출하여 summary 설정
    summary = soup.find('div').find_next('div').text
  
    markdown_text += f"""<tr>
        <td style="width: 33%; padding: 10px;">
            <a href="{link}">{title}</a>
        </td>
        <td style="width: 33%; padding: 10px;">{feed_date}</td>
        <td style="width: 33%; padding: 10px; text-align: left;">{summary}</td>
    </tr>
    """

markdown_text += "</tbody></table></div>"

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
