import json, readline

def rlinput(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return input(prompt)
   finally:
      readline.set_startup_hook()

newCourses = []

with open("output.json", "r", encoding="utf8") as f:
	courses = json.load(f)
	for c in courses:
		c["title"] = rlinput(c["title"] + ": ", c["title"])
		if "#" not in c["title"]:
			newCourses += [{"link": c["link"], "title": c["title"]}]

with open("filtered.json", "w", encoding="utf8") as f:
	json.dump(newCourses, f, ensure_ascii=False)