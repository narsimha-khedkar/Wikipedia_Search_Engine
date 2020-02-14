#from wikipedia import search
import wikipedia

def wiki_search(arg=None):    		
	try:
		if arg:
			# access the wikipedia api, first look for suggestions, then get
			# the page
			suggestion = wikipedia.search(arg, results=1, suggestion=True)
			
			if len(suggestion[0]) > 0:
				page = wikipedia.page(suggestion[0][0])
				summary = wikipedia.summary(arg, sentences=2)
				print(summary)
			else:
				page = wikipedia.page(arg)
				summary = wikipedia.summary(arg, sentences=2)
				#print(summary)
			return page.url
		else:
			return 'https://en.wikipedia.org/wiki/Main_Page'
	except:
		return 'https://en.wikipedia.org/wiki/Main_Page'

print(wiki_search("einstein"))

#print(wikipedia.summary("google", sentences=2))