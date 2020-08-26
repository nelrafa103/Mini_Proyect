from Chess_Chips import play
from Chess_Board import letters_in_board
from Chess_Board import values_of_chips

boolean = True
play_1 = play()
count = 2
while boolean:
   try:
     play_1.case_1(count)
     count += 1
     #x = range(0,9)
     if 3 in range(3,3) :
       print("Hola Mundo")
    # if letters_in_board["A"] in list(1):
     #if [3] in [9]:
    # print(list("7"))
   except:
      #print('Incorrect')
    # break
      continue
