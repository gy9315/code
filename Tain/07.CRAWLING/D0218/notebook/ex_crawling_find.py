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
# recursive값을 False로 사용 시 직접자식요소만 검색할 수 있고 나머지는 검색이 안된다
print(soup.find('html',recursive=False))
# 개별로 찾고 싶을 떄 속성값 집어넣고, 딕셔너리 형태로 관련 속성 저장하면된다.
print(soup.find('div',{'id':'text_id2'}))
print(soup.find('div',id='text_id2'))
# find 두번사요 해서 찾아보기
print(soup.find('div').find('a',class_='internal_link'))
print(soup.find('div').find('a').attrs)
# find_all은 해당되는 태그에 전체 값을 반환해줌, 태그에 태그내용 전부 출력해줌
print(soup.find_all('div'))
## class의 속성은 무조건 list형태로 반환
## 나머지 속성은 문자형태로 반환

href=soup.find('a',href='www.google.com')
print(href.attrs.values())
print(href.text)

# span 태그의 속성 가져오기
span_tag=soup.find('span')
print(span_tag)
print(span_tag.attrs)
print(span_tag.text)

a_tag=soup.find_all('a')
for x in a_tag:
    print(x)