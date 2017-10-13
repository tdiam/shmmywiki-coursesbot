from pyquery import PyQuery as pq
from urllib.request import urlopen
from urllib.parse import quote
from urllib.error import HTTPError
import json, urllib, time

def spaceToUnderscore(s):
	return s.replace(' ', '_')

filtered = []
base_url = "https://shmmy.ntua.gr/wiki/index.php/"

with open("output.json", "r", encoding="utf8") as j:
	courses = json.load(j)
	for c in courses:
		try:
			url = base_url + quote(spaceToUnderscore(c["title"]))
			f = urlopen(url).read()
			html = pq(f)
			isCourse = len(html("th.lessonTitle")) > 0
			if isCourse:
				filtered.append(c)
			else:
				print(c["title"] + " has no page")
		except HTTPError:
			print(c["title"] + " was not found in Shmmywiki")

with open("filtered.json", "w", encoding="utf8") as f:
	json.dump(filtered, f, ensure_ascii=False)