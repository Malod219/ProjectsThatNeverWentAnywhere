
import random
import sys

headlines = open("empireHeadline.txt", "r").read()
headlines = ''.join([i for i in headlines if not i.isdigit()]).replace("\n\n", " ").split(' ')

editorials = open("empireEditorial.txt","r").read()
editorials = ''.join([i for i in editorials if not i.isdigit()]).replace("\n\n", " ").split(' ')

trades = open("empireTrade.txt","r").read()
trades = ''.join([i for i in trades if not i.isdigit()]).replace("\n\n", " ").split(' ')

drills = open("empireDrill.txt","r").read()
drills = ''.join([i for i in drills if not i.isdigit()]).replace("\n\n", " ").split(' ')

domestic = open("empireDomestic.txt","r").read()
domestic = ''.join([i for i in domestic if not i.isdigit()]).replace("\n\n", " ").split(' ')

finance = open("empireFinance.txt","r").read()
finance = ''.join([i for i in finance if not i.isdigit()]).replace("\n\n", " ").split(' ')
# This process the list of poems. Double line breaks separate poems, so they are removed.
# Splitting along spaces creates a list of all words.

class markov:

	def __init__(self, count):
		self.index = 1
		self.chain = {}
		self.count = count # Desired word count of output
		self.bannedWords = ["the","and","until","with","then","is","of", "a", "if", "but","There","it","using","not","very","be","i'm"]
		self.bannedGrammar = bannedGrammar = [",",":",";","\\","/","\"","'","(",")"]

	def goodWordiser(self, message):
		loopAgain = True
		message = message.split(' ')
		while (loopAgain == True):
			loopAgain = False
			if len(message)>2:
				for word in self.bannedWords:
					if word.lower() in message[-1].lower():
						message.pop(-1)
						loopAgain = True
				for word in self.bannedGrammar:
					if word in message[-1]:
						message[-1]=message[-1][0:-1]
						loopAgain = True
			else:
				break
		message = ' '.join(message)
		return message

	# This loop creates a dicitonary called "chain". Each key is a word, and the value of each key
	# is an array of the words that immediately followed it.
	def generateChain(self, poems):
		for word in poems[self.index:]: 
			key = poems[self.index - 1]
			if key in self.chain:
				self.chain[key].append(word)
			else:
				self.chain[key] = [word]
			self.index += 1

	def loopChain(self):
		word1 = random.choice(list(self.chain.keys())) #random first word
		message = word1.capitalize()

		# Picks the next word over and over until word count achieved
		while len(message.split(' ')) < self.count:
			word2 = random.choice(self.chain[word1])
			word1 = word2
			message += ' ' + word2

		return message

	def resetChain(self):
		self.chain = {}

news = "The Autonomy - The Voltigeur's Automated AI News Source - #0 Issue:5th of Evening Star 2018\n\n"

def quickMarkov(sourcetext, count=100, clean=True):
	mc1 = markov(count)
	mc1.generateChain(sourcetext)
	output = mc1.loopChain()
	if clean == True:
		output = mc1.goodWordiser(output)
	mc1.resetChain()

	return output

news += "HEADLINES\n\nEDITORIAL\n\nTRADE\n\nDRILLS\n\nDOMESTIC\n\nFINANCE\n\nORDERS\n\n___\n\n"
news += "HEADLINES:\n\n"
news += quickMarkov(headlines)
news += "\n\n___\n\nEDITORIAL-\n\n"
news += quickMarkov(editorials)
news += "\n\n___\n\nTRADE - US MineZ Trade Run\n\n"
news += quickMarkov(trades,30)
news += "\n\n___\n\nPvP Drill 145th Mass PvP Event\n\n"
news += quickMarkov(drills, 20)
news += "\n\n___\n\nDOMESTIC-\n\n"
news += quickMarkov(domestic,50)
news += "\n\n___\n\nFINANCE-\n\n"
news += quickMarkov(finance,30)
news += "\n\n___\n\nTHE VOLTIGEURS,THE CLAN'S AUTOMATED NEWS SOURCE AND BRAIN WASHING TOOL. AW YEAH!"
news += ("\n\n```\nPi- This is an experiment. Using markov chains, where the state space is all the various THE EMPIRE "+
		"News posts. The code will likely be made open source as a MarkovChain tool for generating texts from "+
		"a source material in the future. Is this gonna be a regular thing? Probably not. I will make an effort "+
		"to show off other procedurally generated stuff I work on. The inspiration behind writing this Markov Chain "+
		"library is so I have a tool for generating markov chains in a quick, hopefully time efficient and just plain "+
		"cool manner. Leave a comment if you have any interesting source materials to generate from, or just generally "+
		"any cool procedurally generated content algorithms. If you want to find more cool shit I make, check out my [site](https://distortionlayers.neocities.org/)\n```")
print(news)

# creates new file with output and prints it to the terminal
with open("output.txt", "w") as file:
	file.write(news)
output = open("output.txt","r")
print(output.read())