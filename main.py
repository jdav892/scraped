from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_page = response.text

soup = BeautifulSoup(yc_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_text = []
article_links = []
for article_tag in articles:
    a_tag = article_tag.find("a")
    text = article_tag.getText()
    article_text.append(text)
    link = a_tag.get("href")
    article_links.append(link)
    
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


print(article_text)
print(link)
print(article_upvotes)

max_val = max(article_upvotes)
max_index = article_upvotes.index(max_val)
print(f"{article_text[14]}, {article_links[14]}")
