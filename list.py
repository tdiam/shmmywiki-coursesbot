import json

with open("output.json", "r", encoding="utf8") as f:
	courses = json.load(f)
	for c in courses:
		print(c["title"] + ": " + c["link"])