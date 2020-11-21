import random
VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self, n):
        self.name = n
        self.prizeMoney = 0
        self.prizes = []
    def addMoney(self, amt):
        self.prizeMoney = self.prizeMoney + amt
    def goBankrupt(self):
        self.prizeMoney = 0
    def addPrize(self, prize):
        self.prizes.append(prize)
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)
        
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        print("{} has ${}".format(self.name, self.prizeMoney))
        print()
        print("Category: {}".format(category))
        print("Phrase: {}".format(obscuredPhrase))
        print("Guessed: {}".format(guessed))
        inp = input("Guess a letter, phrase, or type 'exit' or 'pass':")
        while inp != 'exit':
            if len(inp) == 1:
                guessed.append(inp)
                getMove(category, obscuredPhrase, guessed)
            else:
                if inp == 'pass':
                    getMove(category, obscuredPhrase, guessed)
                else:
                    guessed.append(inp)
                    getMove(category, obscuredPhrase, guessed)
        return guessed
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    def __init__(self, n, d):
        WOFPlayer.__init__(self, n)
        self.difficulty = d
    
    def smartCoinFlip(self):
        rand_num = random.randint(1, 10)
        if rand_num > self.difficulty:
            return True
        else:
            return False
    
    def getPossibleLetters(self, guessed):
        lst = list()
        for x in LETTERS:
            if x not in guessed and self.prizeMoney > VOWEL_COST:
                lst.append(x)
            elif x not in guessed and x not in VOWELS and self.prizeMoney <= VOWEL_COST:
                lst.append(x)
            else:
                pass
        return lst
    
    def getMove(self, category, obscuredPhrase, guessed):
        ls = self.getPossibleLetters(guessed)
        for i in ls:
            if (i in LETTERS) and (i in VOWELS) and (self.prizeMoney < VOWEL_COST):
                return 'pass'
            elif len(ls) == 0:
                return 'pass'
            else:
                a = self.smartCoinFlip()
                if a == True:
                    for l in WOFComputerPlayer.SORTED_FREQUENCIES:
                        if l in ls:
                            return l
                else:
                    return random.choice(ls)