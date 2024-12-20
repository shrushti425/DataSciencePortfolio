class TextAnalyzer():
    def __init__(self,text):
        self.text=text
        fortext=text.replace('.','').replace(',','').replace('!','').replace('?','')
        fortext=fortext.lower()
        self.fmttext=fortext
    def freqAll(self):
        wordlist=self.fmttext.split(' ')
        freqmap={}
        for word in set(wordlist):
            freqmap[word]=wordlist.count(word)
        return freqmap
    def freqof(self,word):
        freqdict=self.freqAll()
        if word in freqdict:
            return freqdict[word]
        else:
            return 0
s=input('Enter the passage')
analyzed=TextAnalyzer(s)
print("Formatted text:\n",analyzed.fmttext)
freQmap=analyzed.freqAll()
print(freQmap)
word = input('Enter the word to be searched')
frequency = analyzed.freqof(word)
print("The word",word,"appears",frequency,"times.")
    