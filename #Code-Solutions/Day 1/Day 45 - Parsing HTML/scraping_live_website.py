from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, 'html.parser')


article_titles = soup.find_all(name='span', class_='titleline')
scores = soup.find_all(name='span', class_='score')
article_texts= []
article_links= []
article_scores= []

for article, score in zip(article_titles, scores):
    anchor = article.find(name='a')
    article_text = anchor.get_text()
    article_link = anchor.get('href')
    score_text = score.getText()

    article_texts.append(article_text)
    article_links.append(article_link)
    article_scores.append(int(score_text.split()[0]))

top_upvoted = max(article_scores)
top_article_index = article_scores.index(top_upvoted)

print(f"Top Article: {article_texts[top_article_index]}")
print(article_links[top_article_index])






# from bs4 import BeautifulSoup
# import lxml

# with open ("website.html", encoding="utf-8") as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.a) #prints the first anchor tag

# all_anchor_tags = soup.find_all(name='a')
# for tag in all_anchor_tags:
#     text = tag.getText()
#     print(tag.get("href"))

# heading = soup.find(name="h1", id='name')
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# headings = soup.select('.heading')
# print(headings)

