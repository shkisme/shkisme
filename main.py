import feedparser, time

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

"""  # list of blog posts will be appended here

MAX_POST = 5
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
