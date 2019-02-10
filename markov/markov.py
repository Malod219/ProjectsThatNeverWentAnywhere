import random


poemBeginnings = {}
poemCorpus = {}

def corpusAdd(poem):
	lines = poem.readlines()
	for line in lines:
		line = line.split()
		try:
			if line[0] in poemBeginnings:
				try:
					poemBeginnings[line[0]].append(line[i+1])
				except:
					poemBeginnings[line[0]].append("\n")
			else:
				try:
					poemBeginnings[line[0]] = [line[i+1]]
				except:
					poemBeginnings[line[0]] = ["\n"]
		except:
			pass

		for i, word in enumerate(line):
			if word in poemCorpus:
				try:
					poemCorpus[word].append(line[i+1])
				except:
					poemCorpus[word].append("\n")
			else:
				try:
					poemCorpus[word] = [line[i+1]]
				except:
					poemCorpus[word] = ["\n"]

def recursiveMarkov(finalOut, lastWord, wordsGeneral):
	wordPosition=-1
	for i, word in enumerate(wordsGeneral):
		if lastWord in word[0]:
			wordPosition = i
	if wordPosition == -1:
		wordPosition = random.randint(0,len(wordsGeneral)-1)
	options = len(wordsGeneral[wordPosition][1])-1
	optionChoice = random.randint(0,options)
	word = wordsGeneral[wordPosition][1][optionChoice]
	finalOut += word+" "
	if (word is "\n") or ("." in word):
		return finalOut
	else:
		return recursiveMarkov(finalOut, word, wordsGeneral)

for i in range(19):
	with open("poem"+str(i)+".txt","r") as poem:
		corpusAdd(poem)

poem = ""
wordBeginnings = []
for item in poemBeginnings.items():
	wordBeginnings.append(item)

wordsGeneral = []
for item in poemCorpus.items():
	wordsGeneral.append(item)

paragraphs = random.randint(1,6)

finalOut = ""

for i in range(paragraphs):
	lines = random.randint(1,6)
	for line in range(lines):
		beginning = random.randint(0, len(poemBeginnings)-1)
		word = wordBeginnings[beginning][0]
		finalOut += word+" "
		finalOut = recursiveMarkov(finalOut, word, wordsGeneral)
	finalOut+="\n"
print(finalOut)