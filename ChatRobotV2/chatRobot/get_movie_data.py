import requests
from bs4 import BeautifulSoup

def get_html(url):
	r = requests.get(url)
	r.encoding = r.apparent_encoding
	return r
def make_soup(html,n):

	movies = []
	s = "{0:{3}^5}{1:{3}^5}{2:{3}^5}"
	soup = BeautifulSoup(html.text,'html.parser')
	orign = soup.find('ol',class_="grid_view")
	a = orign.find_all('li')
	
	
	for i in a:
		data = []
		if i.find('span',class_='title'):
			data.append(i.find('span',class_='title').string)
		else:
			data.append("无")
		if i.find('span',class_='rating_num'):
			data.append(i.find('span',class_='rating_num').string)
		else:
			data.append("无")
		if i.find('span',class_='inq'):
			data.append(i.find('span',class_='inq').string)
		else:
			data.append("无")
		movies.append(data)

	with open("D:\\ChatRobot\\ChatRobotV2\\text\\db_movie.txt",'a',encoding='utf-8') as f:
		# f.write(s.format("电影名称","评分","短评",chr(12288))+'\n')
		an = 0
		for i in movies:
			# print(i)
			f.write(s.format(i[0],i[1],i[2],chr(12288))+'\n')
		
def main():

	for i in range(0,10):
		url = "https://movie.douban.com/top250"+"?start="+str(25*i)
		html = get_html(url)
		make_soup(html,25*i)

main()
