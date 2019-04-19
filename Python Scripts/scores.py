import requests
from bs4 import BeautifulSoup
import subprocess as s


url = "http://www.goal.com/en-in/live-scores"
r=requests.get(url);


data=r.text
soup = BeautifulSoup(data, "html5lib")
elements = soup.find_all("div",{"class":"match-main-data"})

for item in elements:
	a1=''
	#home-team and goals
	i1 = item.contents[1].find_all("div",{"class":"team-home"})
	i2 = i1[0].find_all("span",{"class":"team-name"})[0].text
	i7 = i1[0].find_all("span",{"class":"goals"})[0].text

	#away-team and goals
	i3 = item.contents[1].find_all("div",{"class":"team-away"})
	i4 = i3[0].find_all("span",{"class":"team-name"})[0].text
	i8 = i3[0].find_all("span",{"class":"goals"})[0].text

	#match status
	i5 = item.contents[1].find_all("div",{"class":"match-status"})[0]
	i6 = i5.find_all("span")[0].text

	if i6 != '':
		a1 = i2 + "  " + i7 + " - " + i8 + "  " + i4 +  " -----> " + i6
		print(a1)
		s.call(['notify-send',a1])
