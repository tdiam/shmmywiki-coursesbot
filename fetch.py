from pyquery import PyQuery as pq
from urllib.request import urlopen
import sys, json, urllib, time

def readPage(url, start = 1):
	global courseList
	time.sleep(1) # prevent DDOS
	f = urlopen(url + str(start)).read().decode('utf-8')
	html = pq(f)
	courses = html("tr.clickable-row .title a")
	for c in courses:
		cobj = pq(c)
		course = {"link": cobj.attr["href"], "title": cobj.html()}
		courseList += [course]
	if url[-9:-1] == "semester" and start >= 7:
		return
	if url[-5:-1] == "flow" and start >= 12:
		return
	readPage(url, start + 1)

courseList = []
url = "https://www.ece.ntua.gr/gr/undergraduate/courses/semester/"
readPage(url)
url = "https://www.ece.ntua.gr/gr/undergraduate/courses/flow/"
readPage(url)

with open("output.json", "w", encoding="utf8") as fout:
	json.dump(courseList, fout, ensure_ascii=False)