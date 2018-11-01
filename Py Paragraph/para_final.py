import os
import re

f = open('paragraph_1.txt', 'r')
content = f.read()

words = re.split(r"[\s\.,\?]+",content)
characters = 0



d = len(words)

sentence = content.count('.')

avg_sent_count = d/sentence

for words in content:
        if words not in [" ",",",";","."]:
                characters += sum(len(letter) for letter in words)
                average_char = characters/d
     
print ("Paragraph Analysis")
print ("-----------------")
print ("Approximate Word Count: " + str(d))
print ("Approximate Sentence Count: " + str(sentence))
print ("Average Sentence Length: " + str(avg_sent_count))
print ("Average Letter Count: " + str(average_char))



