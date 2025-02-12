import string 
sent = input("enter your sentence : ")
letters = set(string.ascii_lowercase) # for storing all lower case letters in a list...
sent = sent.lower()
sent = set(sent)
if letters == sent.intersection(letters) :
   print("panagrams")
else :
   print("not panagrams")