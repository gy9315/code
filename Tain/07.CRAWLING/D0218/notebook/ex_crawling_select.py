html_example = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link external_link2" href="www.google.com">google</a>
        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="external_link" href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')
# 단체로 찾기에 리스트형태로 나옴
footer=soup.select_one('h1#footer')
print(footer.text)
class_link=soup.select_one('a.internal_link')
print(class_link)
## select_one사용
# 부모tag>자식tag
class_link=soup.select_one('div#link>a.internal_link')
print(class_link)
# find사용
a=soup.find('div',id='link').find('a',class_='external_link')
print(a)

# 부모tag 자손tag
# 자식은 상위tag바로 밑에 존재하는 tag를 말한다.
a=soup.select_one('div#class1 p#second')
print(a)
a=soup.select_one('div#link a.internal_link')
print(a)
print(a['href'])
print(a.text)

alls=soup.select('h1')
print(alls[0].text)

for x in alls:
    print(x.text)
    
a=soup.select('div#class1 >a')
print(a)
print(a[0]['href'])
a=soup.select('div#class1 a')
print(a)
print(soup.prettify())