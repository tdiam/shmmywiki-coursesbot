import json
import pywikibot

# before running the bot, you should login `python pwb.py login` with the bot credentials in the shmmywiki site

with open("filtered.json", "r", encoding="utf8") as f:
	courses = json.load(f)
	site = pywikibot.Site()
	for c in courses:
		# fetch the corresponding page of the course
		page = pywikibot.Page(site, c["title"])
		text = page.text
		# search for κωδικόςΜαθήματος || κώδικαςΜαθήματος parameter
		i = text.find("|κωδικόςΜαθήματος")
		if i < 0:
			i = text.find("|κώδικαςΜαθήματος")
		if i < 0:
			continue
		# insert url parameter right before "κωδικόςΜαθήματος" parameter
		text = text[:i] + "|url = " + c["link"] + "\n" + text[i:]
		page.text = text
		page.save(u"Προσθήκη URL προς ιστοσελίδα σχολής για κάθε μάθημα [Αυτόματη επεξεργασία από ShmmywikiBot (χειριστής Tdiam)]")