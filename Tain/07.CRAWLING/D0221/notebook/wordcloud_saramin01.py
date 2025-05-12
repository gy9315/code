from bs4 import BeautifulSoup
from urllib.request import Request
from urllib.parse import quote
from urllib.request import urlopen
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import platform
import numpy as np
from PIL import Image



def get_sector_data(url, keyword, sector_list):
	'''
	사람인에서 <div class="job_sector">데이터분석가</div> 부분만 크롤링 
	크롤링 결과는 sector_list[]에 저장함 
	'''
	try:
		urlrequest = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		html = urlopen(urlrequest)
		soup = BeautifulSoup(html, 'html.parser')
		
		job_items = soup.find_all('div', {'class':'item_recruit'})		
		# 내부에 badge 건너뜀 
		for job in job_items:
			job_sectors = job.find('div', {'class':'job_sector'})
			sector_items = job_sectors.find_all('a', {'target':'_blank'})
			for sector in sector_items:
				sector_text = sector.text .replace('\n', '').strip()				
				sector_list.append(sector_text)
				#print(sector_text)
	except Exception as e:
		print(e)


def make_wordcloud(word_list, stopwords, word_count):
    okt = Okt()

    counts = Counter(word_list)
    tags = counts.most_common(word_count)
    tag_dict = dict(tags)
    # 검색어 제외 방법 2: dict에서 해당 검색어 제거
    for stopword in stopwords:
        if stopword in tag_dict:
            tag_dict.pop(stopword)

    print('-' * 80)
    print('tag_dict:', tag_dict)

    if platform.system() == 'Windows':
        path = r'c:\Windows\Fonts\malgun.ttf'
    elif platform.system() == 'Darwin':  # Mac OS
        path = r'/System/Library/Fonts/AppleGothic'
    else:
        path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

    img_mask = np.array(Image.open('cloud.png'))
    wordcloud = WordCloud(font_path=path, width=800, height=600,
                          background_color="white", max_font_size=200,
                          repeat=True,
                          colormap='inferno', mask=img_mask)

    cloud = wordcloud.generate_from_frequencies(tag_dict)
    plt.figure(figsize=(10, 8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()


if __name__ == '__main__':
	keyword='데이터분석가'
	sector_list = []
	stopwords = [keyword, '데이터엔지니어'] # wordcloud에서 제외할 단어
    
	search_word = quote(keyword)
	for page in range(1, 10):		
		url = f'https://www.saramin.co.kr/zf_user/search?' \
			  	f'search_area=main&search_done=y&search_optional_item=n&searchType=search&' \
		  		f'searchword={search_word}&recruitPage={page}' 

		get_sector_data(url, keyword, sector_list)
		print(f'{page}: {sector_list}')
		print('-' * 90)

	print(f'sector_list len: {len(sector_list)}')	
	make_wordcloud(sector_list, stopwords, 50)
