#Every great project starts with... ENTERPRISE QUALITY.
#
# CODE OF CONDUCT THE SJWS HAVE INVADED
#  * be nice
#  * be accepting
#  * be civil
#  * install gentoo
#
#lets make a shitpost generator 
#ok 
#great idea
#this quality


#can anyone see this???
#Please respond if yoiu can see this
#
#limiting this shit to prefixes is terrible we need shitposts generated so real that we could make an OP with them
#how could we do that?
#something along the lines of 'only niggers will use "thing" why are you still using "thing" /tech/?'
#we could remake the prefixes to something where you do like: "only [noun] will use [thing] like that
#that could work
#ill make a list of formats
#more grammar 
#how i end a function in python?
#you dont, you just let it be
#that upsets me
#yea python is a bit original with its syntax and it can be hard to get used to but its a really nice language
#i just use ruby and c
# its all fuckin in the tabs man let the tabs do all the work
# drop a tab drop a brace ezpz lemonsqueezy
#it lets you do things a lot of different ways

##############################################################
#         INDUSTRIAL GRADE SHITPOST MACHINERY                #
#                 "Oh my god, it's so lifelike"              #
# "I refuse to use linux if it doesnt have a shitpost        #
#  generator built-in and no sane person would either"       #
##############################################################


import random, re, os

prefix = prefixes = [
	'i hate', 'I hate', 'I fucking hate',
	'Hey guys', 'hey guys', 'hey guise',
	'fucking', 'Fucking', 'FUCKING',
	'the best meme is',
	'kill all',
	'the worst meme is',
	'the real botnet is',
	'>yfw',
	'>yrw',
	'>tfw',
	'smh tbh',
	'DAE le',
	'>implying',
	'Hey faggots,',
	'How do you',
	'It\'s like I\'m really',
	'Do you suck',
	'Slide thread,',
	'That',
	'now that the dust has settled, how do we feel about',
	'repost if you',
	'op is a faggot'
]

formats = [
	'[prefix] [adjective] [noun]',
	'fucking [noun] [noun] [noun] [noun]',
	'Nice try, [noun]',
	'Fucking [noun]fags',
	'\n\n>2015 \n >still [verb] [noun]\n >ISHYGDDT\n\n',
	'anyone have that [noun] webm?',
	'[noun] thread',
	'[adjective] [noun] detected',
	'[verb] [adjective] [noun] detected',
	'Can\'t [verb] the [noun]',
	'Nice try you [verb] [noun]',
	'>>>/[place]/',
	'>[year] + [number]\n>[verb] the [noun]',
	'as a [noun]fag i feel like [noun]\'s are [adjective]..', #idk
	'I kind of like [adjective] [noun] tbh fam.',
	'>[verb] the [adjective] jew',
	'If you see this shitpost while scrolling, you\'ve been visited by the [adjective] [noun] of [verb]. [noun] and [adjective] [noun] will be yours, but only if you post [noun] [verb] [noun].',
	'>Posting in a [noun] thread'
	'What did you [verb] did you just [adjective] about me, you [little] [noun]? I\'ll have you know I [verb] top of my [noun] in the [place], and I\'ve been involved in numerous secret raids on [noun], and I have over [number]',
	#'testing: [number] [number] [number]'
]

# i luv u, /tech/

# LOLOLOLOLOLOLOLOLOLOLOLOLOLOLLLLLLLLLLLLLLLLLLLLLL

# if the prefix is singular then noun should be plural and vice versa
# could use a dictionary with word type and singularity
#we could just make 2 different prefixes tables, one which needs singular ones and one which needs plural, and with formatting we can just add s at the end idk
#that's probably easier

# sorting this list with no survivors
# you nigger just fucking print it out sorted
# and copy and paste it back into this
# but muh lines
# print it with lines
noun = nouns = [
 'AIDS',
 'Arch',
 'Bait', 'BAIT', 'bait',
 'BENIS',
 'BSD',
 'CANCER',
 'CIA',
 'CISA',
 'CISC',
 'CUCKS',
 'dicks', 'DICKS', 
 'FBI',
 'Gentoo',
 'Goy','Goys','Goyim',
 'KIKES','KIKE',
 'Lisp',
 'NIGGERS',
 'NORMIES',
 'mate', 'm8', 'm80s', 
 'NSA', 
 'Normies', 
 'PENIS', 
 'RISC', 
 'SHILLS', 
 'SICP', 
 'SJWs', 
 'SPICS', 
 'SYSTEMD', 
 'Shlomo', 
 'TPP', 
 'TROLL',
 'VN', 
 'Windows 10', 
 'Windows 7', 
 'Windows XP',
 'Windows [number]',
 '[number] memers', 
 'anime', 
 'anonymous', 
 'apple', 
 'archfags', 
 'benis', 
 'big guys', 
 'cancer', 
 'cock',
 'cucks', 
 'faggot', 
 'fam', 
 'feel', 
 'feminist', 
 'google chrome',
 'hack', 
 'hacker', 
 'kek', 
 'keks', 
 'kikes', 
 'loli',
 'maymays', 
 'mint', 
 'niggers', 
 'newfag', 'newfriend',
 'normie', 
 'os-tan', 
 'penis', 
 'plebbit', 
 'ruse',
 'shills', 
 'shitposts',
 'shazbot',
 'spics', 
 'systemd', 
 'the [number]0000000 that died in the holocaust', 
 'the jews', 
 'thread', 
 'troll', 
 'ubuntu',
 'neghole',
 'pozhole',
 'shekel'
]


adjective = adjectives = [
	'gay',
	'the best',
	'with no survivors',
	'ebin',
	'qt 3.1415926535897932384626433832795',
	'memed',
	'epic',
	'poz',
	'fat',
	'dank',
	'6,000,000',
	'hack',
	'stupid',
	'retarded',
	'hand-rubbing', 'hook-nosed'
]

# we need verbs
#then make a format with verbs you faggot
verb = verbs = [
	'crash this plane',
	'crashing',
	'fucking',
	'shitposting',
	'memeing',
	'trolling',
	'flaming',
	'cucked',
	'detect','pleb detected',
	'sperging',
	'stumped',
	'niggin'
]


place = places = [ #what if we put synonymns on the same line # ok
	'g',
	'tech', 'Church of RMS',
	'leftypol', 'r9k', 'fem', 'mgtow', 'pol',
	'4chan', 'cuckchan', '4chad', 'halfchan',    
	'9gag', '9shit', '9fag',
	'plebbit',
	'tumblr',
	'voat',
	'jewbook', 'kikebook','gaschamber','auschwitz',
	'Twatter'
]

year = years = [
	'3000 BC'
	'1990'
	'Y2K',
	'Y2K38',
	'2014',
	'2015',
	'2016',
	'CURRENT_YEAR',
	'2014 + 1',
	'The year of our lord, 2015'
]

#function just in case
# wait how does this make sense, we never reseed
# it should hit the same problem when it executes twice in the same second
#it just werks
#the old funtcion would just get one result, and replace the string with that one result
#this splits every space, and replaces every instance of the filter with the function result
#who fucked it up
#nvm someone put s after everything
# let me fix that
def shitpost():
	c = random.choice
	format = c(formats)
	#what the fuck are you doing it worked perfectly fine
	# cleaner, if it works
	# YEE BOI
	#ooh nice
	# is it being hashed? the value of c(array)? 
	#what do you want to do here?
	# if we have [number] [number] [number]
	# it currently replaces all instances of [number] with the same value
	# replace() already do that
	# right, that's NOT what we wanted. I think the value of c() is being hashed during the replce
	#why didnt that work?
	#i always have the old sexy lambda code to use
	# its uglier tho
	#but it werks
	# we are tech we do better than works
	# we do quality 100%
	#you can make the lambdas sexy
	#but not the nested for loops
	#yea but ill just put it here in case you need it
	
	'''
	c = random.choice
	format = c(formats)
	
	filters = {
		"[prefix]": lambda: c(prefixes),
		"[adjective]": lambda: c(adjectives),
		"[verb]": lambda: c(verbs),
		"[noun]": lambda: c(nouns).replace("[number]", str(random.randrange(-1000, 1000))),
		"[place]": lambda: c(places),
		"[number]": lambda: str(random.randrange(-1000, 1000)),
		"[year]": lambda: c(years)
	}

	split = format.split(" ")
	
	for index, word in enumerate(split):
		for filter, func in filters.items():
			if filter in word:
				split[index] = word.replace(filter, func())
	
	format = " ".join(split)
	return format
	'''
	
	def c(array):
		random.seed(os.urandom(256))
		return random.choice(array)
	
	def replace_number():
		random.seed(os.urandom(256))
		return str(random.randrange(-1000, 1000))
	
	# Its set to only replace the first found instance on each loop
	# so when it comes round again, the first found instance should be the second occurence
	for x in range(10):
		   return format.replace("[prefix]", c(prefixes), 1) \
			.replace("[adjective]", c(adjectives), 1) \
			.replace("[noun]", c(nouns), 1) \
			.replace("[verb]", c(verbs), 1) \
			.replace("[place]", c(places), 1) \
			.replace("[year]", c(years), 1) \
			.replace("[number]", replace_number(), 1)

# now we just need to push this onto a web server (github-pages? django?)
# django's just a web generator, we need a server for hosting this shit
# also flask is supposed to be cooler according to the cool kids

#flask is easy


def htmlwrapper():
	full = "<html><head><title>Welcome to the Shitposting Machinery</title></head><body> "
	for i in range(10):
		full += "<p>" + shitpost() + "</p>"
	full += "</body> </html>"
	return full

#whats the point of this? we already fixed the bug
#lisp memes
#ah i never programmed in lisp
def parse_sexp(string):
	sexp = [[]]
	atom = ''
	in_str = False

	LIST_OPEN = '('
	LIST_CLOSE = ')'
	QUOTE = '"'
	WHITESPACE = ' \n\t'
	
	for c in string:
		if c == LIST_OPEN and not in_str:
			sexp.append([])
		elif c == LIST_CLOSE and not in_str: 
			if(len(atom) > 0): 
				sexp[-1].append(solve_atom(atom))

				atom = ''
			temp = sexp.pop()
			sexp[-1].append(temp)
		elif c in WHITESPACE and not in_str:
			sexp[-1].append(solve_atom(atom))
			atom = ''
		elif c == QUOTE:
			in_str = not in_str
		else:
			atom += c
	return sexp[0]

def solve_atom(atom):
	is_number = True
	has_decimal = False
	is_negative = atom[0] == '-'
	if is_negative:
		atom_to_check = atom[1:]
	else:
		atom_to_check = atom[:]
	for c in atom_to_check:
		if c not in '0123456789':
			if not c == '.' or has_decimal:
				is_number = False
				break
			else:
				has_decimal = True
	if is_number:
		if has_decimal:
			return float(atom)
		else:
			return int(atom)
	else:
		return '"' + atom + '"'
		
def sexp_eval(sexp):
	code = '{0}('.format(sexp[0][1:-1])
	if len(sexp) == 1:
		code += ')'
		return eval(code)
	for s in sexp[1:-1]:
		code += '{0},'.format(str(s))
	code += str(sexp[-1])
	code += ')'
	return eval(code)

#test

# What are u doing? do you want to create a Lisp? ok
#lisp interpeter
'''
print('\nS-Expression Test \n------------------')
print(parse_sexp('(+ 5 3 (* 4.5 4))'))
print(parse_sexp('(print "test"')[0])
print(sexp_eval(parse_sexp('(range 5)')[0]))
print('---------------\nEnd S-Expression Test.\n\n')
'''

#excuse my shitty code
#im gonna do a raw_input thing
#function this and pass input
def shitpost_by_amount(amount):
	for i in range(amount): # fucking py3 whatever
		print(shitpost())

use_input = True

if use_input:
	amount = -1
	
	while amount == -1:
		try:
			amount = int(input("Amount of shitposts: "))
			
			if amount < 0:
				raise ValueError("penis lol xD")
		except ValueError:
			amount = -1
	
	shitpost_by_amount(amount)


# TODO:
# post numbers
# quoting
# botnet implementation

#now what
#im gonna paste this to the main one, it looks like the autism cleared up
#nah
#anyone want contrib to the git
#over here
#we need to add a new feature to our sick ass shitposting machinery
#this all started with "lets make a shitpost generator"
# and we made it something more
#a shitposting robot
# a shitposting algorithm
#how do i commit this to linux
# the fuck does that mean
#im retarded sorry
# I don't understand the question, do you mean commit it to git?
#the linux source code git whateverthefuck
# what
# you want to submit this to kernel?
# yu're fucking insane a complete madman
#i refuse to use linux if it doesnt hvae a shitpost generator built in and any sane person wouldnt either
#whats the point of an os if it doesnt have a shitpost generator
#no os gives me that power so i just use the internet through telekinesis
# it's nt linux that needs the shitposting machinery, we need to add it to GNU core tools
# add this to systemd then people will want to use it
# let's just make it a service that produces a shitpost every 10s to stdout
# just like on 8chan
#someone mix this with django so we can have a shitpost generator website
# make a shitpost on a timer and when the timer expires quote it and reply
# recursive shitposting
#fuck is there anyway i can bypass that prorgam hlated for too long thing so i can have infinite shitposting?
# okay my interpreter is kind of shit.
# 
#Nice try you niggin NIGGERS 
# do you think we can do this recursively
# to like three steps, a format that uses format[2] 
# to any actual value I mean
#WHO THE FUCK CHANGED THE VARIABLE NAMES?6
#dont do that.
#shit i fucked up
# wow fuck there's vim keybinds on this shit
# woulda made life so much simpler

# >as a KIKEfag i feel like KIKEs are the best.. 
# it's become sentient

#What if we add a flag to determine whether or not you want a new letter of that type?
#wot
#so like
# [noun] [noun]
#If the noun "ass" is selected, that will end up being
# ass ass
#But what if you wanted two different nouns?
#that sounds retarded, so do it
