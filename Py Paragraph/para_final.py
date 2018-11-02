import os
import re

f = open('paragraph_1.txt', 'r')
content = f.read()

words = re.split(r"[\s\.,\?]+",content)
characters = 0


#Calculate number of words
d = len(words)

#Calculate number of sentences
sentence = content.count('.')

#Calculate Average number of sentences
avg_sent_count = d/sentence

#Calculate Average Letter Count
for words in content:
        if words not in [" ",",",";","."]:
                characters += sum(len(letter) for letter in words)
                average_char = characters/d

#Final Result     
print ("Paragraph Analysis")
print ("-----------------")
print ("Approximate Word Count: " + str(d))
print ("Approximate Sentence Count: " + str(sentence))
print ("Average Sentence Length: " + str(avg_sent_count))
print ("Average Letter Count: " + str(average_char))



