
wordinput = raw_input("Enter a fucking word: ")

def dankmeth(word):
	if(len(word)==0):
		#print "enter cond 1"
		return "true"
	elif(len(word)==1):
		#print "enter cond 2"
		return "true"
	elif(word[0]==word[len(word)-1]):
		#print "enter cond 3"
		word = word[1:len(word)-1]
		print word
		return dankmeth(word)


#print type(wordinput)
print(dankmeth(wordinput))
#print("true")


'''
def palindrome(word):
	if len(word)<=1:
		return True
	else:
		if word[0] == word[len(word)-1]:
			word_ = word[1:len(word)-1]
			return palindrome(word_)
		else:
			return False

if(palindrome(wordinput)):
	print "True"
else:
	print "False"
'''