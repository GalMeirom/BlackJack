from random import shuffle

#Stage 1
class Card():
    def __init__ (self, sign, value = 10):
        self.sign = sign
        self.value = value
        self.wrote = value
    def show(self):
        print ("The {} of {}s".format(self.wrote, self.sign))
    def represent(self):
        return ("[{}|{}|{}]".format(self.wrote, self.sign, self.wrote))

class Deck():
    def __init__(self):
        self.cards = []
        
    def __len__(self):
        return len(self.cards)

    def build(self):
        for s in ["Haert","Diamond","Spade","Club"]:
            for v in (range(2,11)):
                card = Card(s,v)
                self.cards.append(card)
            for w in ["Prince","Queen","King"]:
                card = Card (s,v)
                card.wrote = w
                self.cards.append(card)
            card = Card (s,11)
            card.wrote = "Ace"
            self.cards.append(card)
    def show(self):
        for card in self.cards:
            card.show()

class Player():
#The Person itself
	def __init__ (self,name,money):
		self.name = name
		self.money = int(money)
		self.handsum = 0
		self.handcards = []
		self.lose = False
		self.maxsum = 0

	def start(self):
		for card in self.handcards:
			self.handsum += card.value

	def hit (self):
		global i
		i += 1
		self.handcards.append(d1.cards[i])
		self.handsum += d1.cards[i].value

	def stay (self):
		self.maxsum = self.handsum

	def represent (self):
		for card in self.handcards:
			print(card.represent())

	def restartnewhand(self):
		self.handsum = 0
		self.handcards = []
		self.lose = False
		self.maxsum = 0

class Diller():
	def __init__(self):
		self.name = "Diller"
		self.handsum = 0
		self.handcards = []
		self.lose = False
		self.maxsum = 0

	def start(self):
		for card in self.handcards:
			self.handsum += card.value

	def hit (self):
		global i
		print("The diller decideds to hit")
		i += 1
		self.handcards.append(d1.cards[i])
		self.handsum += d1.cards[i].value
		self.maxsum = self.handsum

	def represent (self):
		for card in self.handcards:
			print(card.represent())

	def restartnewhand(self):
		self.handsum = 0
		self.handcards = []
		self.lose = False
		self.maxsum = 0

#functions to use inside the code
def checklose():
	#Checking if sombody loses
		for person in [player,diller]:
			if person.handsum > 21:
				person.lose = True
				break

def aceconvert(person):
	#converting the ace if needed
		if person.handsum > 21:
			for card in person.handcards:
				if card.wrote == "Ace":
					if card.value == 11:
						person.handsum -= 10
					else:
						pass
				else:
					pass

def showtable():
	#prints the board
	for person in [diller,player]:
		print ("The {} cards are: ".format(person.name))
		person.represent()

def playerdecision ():
	#The Player turns
	global playerplays
	while playerplays:
		a = input("So {}, would you like to Hit or Stay ?".format(player.name))
		if a == "Hit":
			player.hit()
			showtable()
			aceconvert(player)
			print ("your hand sum is: {}".format(player.handsum))
			if player.handsum > 21:
				break
		elif a == "Stay":
			player.stay()
			playerplays = False
		else:
			pass

def dillerplay():
	#The diller play
	while diller.handsum <= player.handsum:
		diller.hit()
		aceconvert(diller)
		showtable()
		print (diller.handsum)        
		if diller.handsum > player.handsum:
			break
		if diller.handsum >= 21:
			break

def decidingwinnerprimal():
	global handwinner
	if player.lose == True:
		handwinner = diller
		print ("I'm sorry, the diller won the hand")
	elif diller.lose == True:
		handwinner = player
		print ("Congrasulations, You won the Hand!")
            
def decidingwinnerfinal():
	global handwinner
	while handwinner == None:
		if player.lose == True:
			handwinner = diller
			print ("I'm sorry, the diller won the hand")
			break
		elif diller.lose == True:
			handwinner = player
			print ("Congrasulations, You won the Hand!")
			break
		else:
			decidingwinnerbydef()
			break

def decidingwinnerbydef():
	if player.maxsum > diller.handsum:
		handwinner = player
		print ("Congrasulations, You won the Hand!")
	elif diller.handsum > player.maxsum:
		handwinner = diller
		print ("I'm sorry, the diller won the hand")
	else:
		pass

def moneyoutcome():
	if handwinner == player:
		player.money = player.money + bet
		print ("You Have {} money left".format(player.money))
	elif handwinner == diller:
		player.money = player.money - bet
		print ("You Have {} money left".format(player.money))
	else:
		pass
#script START
playerplays = True
d1 = Deck()
d1.build()
i = 0
diller = Diller()
a = None
handwinner = None
bet = 0
wanttoplay = True
newname = None
newmoney = 0
drivetoplay = None
upsidecard = Card("?",0)

#Game Starts
print ("Hello and welcome to our BlackJack game!!")
print ("You will be playing againt our diller")
newname = input("But first what is your name ?")
newmoney = input("And with how much money you'll want to play today ?")
player = Player(newname,newmoney)
print ("Great! Lets get stated")
while wanttoplay:
	shuffle(d1.cards)
	playerplays = True
	i = 0
	handwinner = None
	bet = 0
	drivetoplay = None
	a = None
	for person in [player,diller]:
		person.restartnewhand()
	while handwinner == None:
		bet = int(input("On how much do you want to bet ?"))
		if bet <= player.money:
			pass
		else:
			print ("You can't do that, you dont have enough money")
			break
		print ("The diller will now give you your two cards and show you his own card")
		player.handcards.append(d1.cards[i])
		i += 1
		diller.handcards.append(d1.cards[i])
		i += 1
		player.handcards.append(d1.cards[i])
		diller.handcards.append(upsidecard)
		player.start()
		diller.start()
		print ("This is now the borad:")
		showtable()
		playerdecision()
		checklose()
		decidingwinnerprimal()
		moneyoutcome()
		if handwinner != None:
			break
		diller.handcards.pop(1)
		dillerplay()
		checklose()
		decidingwinnerfinal()
		moneyoutcome()
	if player.money == 0:
		break
	drivetoplay =  input("Would you like to play again ?")
	if drivetoplay == "yes":
		wanttoplay = True
	else:
		wanttoplay = False
print("Thank you for playing with us!!")