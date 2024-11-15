import feedparser, time
from bs4 import BeautifulSoup

URL="https://shkisme.vercel.app/rss.xml"
RSS_FEED = feedparser.parse(URL)

markdown_text = """## [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fshkisme&count_bg=%23DAB628&title_bg=%232D2B55&icon=github.svg&icon_color=%23E7E7E7&title=GitHub&edge_flat=false)](https://hits.seeyoufarm.com)

<div align="center">

[![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=shkisme&rank_icon=github&include_all_commits=true&count_private=true&show_icons=true&theme=shades-of-purple&show=reviews,discussions_started,discussions_answered,prs_merged,prs_merged_percentage)](https://github.com/anuraghazra/github-readme-stats) 
[![GitHub Streak](https://streak-stats.demolab.com?user=shkisme&theme=shades-of-purple&card_width=350)](https://git.io/streak-stats)  

</div>

"""

markdown_text += """## 📝 My [Blog](https://shkisme.vercel.app) Posts

<div align="center">
<table>
<thead>
<tr>
<th>Title</th>
<th>Date</th>
<th>Description</th>
</tr>
</thead>
<tbody>
"""

# Add pinned posts
for idx, feed in enumerate(RSS_FEED['entries']):
    feed_date = time.strftime('%Y/%m/%d', feed['published_parsed'])
    title = feed['title']
    link = feed['link']
    description = feed['description']
    soup = BeautifulSoup(description, 'html.parser')
    summary = soup.find('div', class_='content').text
    isPinned = soup.find('div', class_='isPinned').text
    if isPinned == "false":
        continue

    markdown_text += f"""
<tr>
<td><a href="{link}">{title}</a></td>
<td>{feed_date}</td>
<td>{summary}</td>
</tr>
"""

markdown_text += """
</tbody>
</table>
</div>
"""

# Add latest posts
markdown_text += """<details>
<summary>⭐️ Latest Blog Posts</summary>

<div align="center">
<table>
<thead>
<tr>
<th>Title</th>
<th>Date</th>
<th>Description</th>
</tr>
</thead>
<tbody>
"""

MAX_POST = 5
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break

    feed_date = time.strftime('%Y/%m/%d', feed['published_parsed'])
    title = feed['title']
    link = feed['link']
    description = feed['description']
    soup = BeautifulSoup(description, 'html.parser')
    summary = soup.find('div').find_next('div').text

    markdown_text += f"""
<tr>
<td><a href="{link}">{title}</a></td>
<td>{feed_date}</td>
<td>{summary}</td>
</tr>
"""

markdown_text += """
</tbody>
</table>
</div>
"""

with open("README.md", mode="w", encoding="utf-8") as f:
    f.write(markdown_text)
