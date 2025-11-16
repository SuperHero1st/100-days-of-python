from bs4 import BeautifulSoup
# import lxml

with open ("website.html", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
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

company_url = soup.select_one(selector="p a")
print(company_url)

headings = soup.select('.heading')
print(headings)

