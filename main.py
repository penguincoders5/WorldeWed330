import random
import sys
import os


f = open('words.txt', 'r')
data = f.read()

datalist = data.split(',')


for i in range(len(datalist)):
  datalist[i] = datalist[i][4:]
  datalist[i] = datalist[i][:5]
  

# print(datalist)
wordle = random.choice(datalist)
'🟥'
'🟩'
'🟨'

def pretty(boxes):
  s = ''
  for box in boxes:
    s += box
  print(s)

responses = []

for i in range(6):

  guess = input('Guess a 5 letter word: ')
  # os.system('clear')

  boxes = ['🟥', '🟥', '🟥', '🟥', '🟥']
  

  
  for i in range(5):
    if wordle[i] == guess[i] :
      boxes[i] = '🟩'
    elif guess[i] in wordle:
      boxes[i] ='🟨'
  boxes.append(guess)
  responses.append(boxes)
  os.system('clear')
  for response in responses:
    pretty(response)

  
  if guess == wordle :
    print('Congrats! you win.')

print('The wordle is: ')
print(wordle)

