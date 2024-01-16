
import random, os, time


card_numbers = []

def ran():
  number = random.randint(1,90)
  return number

for i in range(3):
  card_numbers.append([ran(), ran(), ran()])
  if ran() in card_numbers:
    ran() 

def pretty_printing(list):
  for i in list:
    for j in i:
      list[1][1] = "BINGO"  
      print(j, end=" | ")     
    print()

while True: 
  pretty_printing(card_numbers)
   
  player_number = int(input("Choose your number: "))
  counter = 0
  for i in range(3):
    for j in range(3):
      if card_numbers[i][j] == player_number:
        card_numbers[i][j] = "X"
  
  for row in card_numbers:
    for item in row:
      if item == "X":
        counter+=1  

  if counter == 8:
    print("BINGOOOO!")
    break
  time.sleep(0.5)
  os.system("cls")