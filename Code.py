print("""Welcome to my Games Console what game would you like to play:
1. Tic Tac Toe
2. Cookie Clicker
3. Hangman
4. Who Wants To Be a Millionaire
5. Rock, Paper, Scissors (1p)
6. Rock, Paper, Scissors (2p)
7. Learning Chatbot
8. Story Generator """)

def menu():
	choice = int(input("Choose a number: "))
	if choice == 1:
					
					
					
	elif choice == 2:
					
			
							
	elif choice == 3:
		#Hangman (vs computer) -Daniel Jennings
		#imports
		import random
		#define globals
		global hm_l1
		global hm_l2
		global hm_l3
		global hm_14
		global hm_l5
		global hm_l6
		global hm_l7

		global WsoF
		global word
		global word_l1
		global word_l2
		global word_l3
		global word_l4
		global word_l5
		global word_l6
		global word_l7
		global word_l8
		global word_l9
		global word_l10

		global real_l1
		global real_l2
		global real_l3
		global real_l4
		global real_l5
		global real_l6
		global real_l7
		global real_l8
		global real_l9
		global real_l10

		global done_1
		global done_2
		global done_3
		global done_4
		global done_5
		global done_6
		global done_7
		global done_8
		global done_9
		global done_10

		global wrong_letters
		global fail_count

		#setting up variables
		hm_l1 = ""
		hm_l2 = ""
		hm_l3 = ""
		hm_14 = ""
		hm_l5 = ""
		hm_l6 = ""
		hm_l7 = ""
		wrong_letters = ""
		fail_count = 0

		def fail1():
		  #ading globals
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  global fail_count
		  hm_l1 = ""
		  hm_l2 = ""
		  hm_l3 = ""
		  hm_14 = ""
		  hm_l5 = ""
		  hm_l6 = ""
		  hm_l7 = " _____ "
		  fail_count = 1
		  what()

		def fail2():
		  #ading globals
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  global fail_count
		  hm_l1 = ""
		  hm_l2 = "| "
		  hm_l3 = "| "
		  hm_14 = "| "
		  hm_l5 = "| "
		  hm_l6 = "| "
		  hm_l7 = "|_____ "
		  fail_count = 2
		  what()

		def fail3():
		  #ading globals
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  global fail_count
		  hm_l1 = "________ "
		  hm_l2 = "| "
		  hm_l3 = "| "
		  hm_14 = "| "
		  hm_l5 = "| "
		  hm_l6 = "| "
		  hm_l7 = "|_____ "
		  fail_count = 3
		  what()

		def fail4():
		  #ading globals
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  global fail_count
		  hm_l1 = "________ "
		  hm_l2 = "|/ "
		  hm_l3 = "| "
		  hm_14 = "| "
		  hm_l5 = "| "
		  hm_l6 = "| "
		  hm_l7 = "|_____ "
		  fail_count = 4
		  what()

		def fail5():
		  #ading globals
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  global fail_count
		  hm_l1 = "________ "
		  hm_l2 = "|/     | "
		  hm_l3 = "|      O "
		  hm_14 = "| "
		  hm_l5 = "| "
		  hm_l6 = "| "
		  hm_l7 = "|_____ "
		  fail_count = 5
		  what()
		  
		def fail6():
		  #ading globals
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  global fail_count
		  hm_l1 = "________ "
		  hm_l2 = "|/     | "
		  hm_l3 = "|      O "
		  hm_14 = "|      | "
		  hm_l5 = "| "
		  hm_l6 = "| "
		  hm_l7 = "|_____ "
		  fail_count = 6
		  what()
		  
		def fail7():
		  #ading globals
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  global fail_count
		  hm_l1 = "________ "
		  hm_l2 = "|/     | "
		  hm_l3 = "|      O "
		  hm_14 = "|     /| "
		  hm_l5 = "| "
		  hm_l6 = "| "
		  hm_l7 = "|_____ "
		  fail_count = 7
		  what()
		  
		def fail8():
		  #ading globals
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  global fail_count
		  hm_l1 = "________ "
		  hm_l2 = "|/     | "
		  hm_l3 = "|      O "
		  hm_14 = "|     /|\ "
		  hm_l5 = "| "
		  hm_l6 = "| "
		  hm_l7 = "|_____ "
		  fail_count = 8
		  what()
		  
		def fail9():
		  #ading globals
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  global fail_count
		  hm_l1 = "________ "
		  hm_l2 = "|/     | "
		  hm_l3 = "|      O "
		  hm_14 = "|     /|\ "
		  hm_l5 = "|     / "
		  hm_l6 = "| "
		  hm_l7 = "|_____ "
		  fail_count = 9
		  what()

		def fail10():
		  #ading globals
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  global fail_count
		  hm_l1 = "________ "
		  hm_l2 = "|/     | "
		  hm_l3 = "|      O "
		  hm_14 = "|     /|\ "
		  hm_l5 = "|     / \ "
		  hm_l6 = "| "
		  hm_l7 = "|_____ "
		  fail_count = 10
		  print("game over")
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  print("The real word was "+str(real_l1)+str(real_l2)+str(real_l3)+str(real_l4)+str(real_l5)+str(real_l6)+str(real_l7)+str(real_l8)+str(real_l9)+str(real_l10))
		  
		def Hangman():
		  #globals
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global done_1
		  global done_2
		  global done_3
		  global done_4
		  global done_5
		  global done_6
		  global done_7
		  global done_8
		  global done_9
		  global done_10
		  
		  global wrong_letters
		  global fail_count
		  
		  #game choice
		  word = random.randint(1,25)
		  done_1 = ""
		  done_2 = ""
		  done_3 = ""
		  done_4 = ""
		  done_5 = ""
		  done_6 = ""
		  done_7 = ""
		  done_8 = ""
		  done_9 = ""
		  done_10 = ""
		  print("Welcome to Hangman created by Daniel Jennings")
		  print("Guess the word:")
		  if word == 1:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = "_ "
		    word_l8 = "_ "
		    word_l9 = ""
		    word_l10 = ""
		    wrd1()
		  elif word == 2:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = ""
		    word_l6 = ""
		    word_l7 = ""
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd2()
		  elif word == 3:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = ""
		    word_l7 = ""
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd3()
		  elif word == 4:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = ""
		    word_l6 = ""
		    word_l7 = ""
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd4()
		  elif word == 5:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = "_ "
		    word_l8 = "_ "
		    word_l9 = "_ "
		    word_l10 = ""
		    wrd5()
		  elif word == 6:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = "_ "
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd6()
		  elif word == 7:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = "_ "
		    word_l8 = "_ "
		    word_l9 = "_ "
		    word_l10 = "_ "
		    wrd7()
		  elif word == 8:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = ""
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd8()
		  elif word == 9:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = ""
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd9()
		  elif word == 10:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = "_ "
		    word_l8 = "_ "
		    word_l9 = "_ "
		    word_l10 = ""
		    wrd10()
		  if word == 11:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = "_ "
		    word_l8 = " "
		    word_l9 = ""
		    word_l10 = ""
		    wrd11()
		  elif word == 12:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = ""
		    word_l6 = ""
		    word_l7 = ""
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd12()
		  elif word == 13:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = ""
		    word_l7 = ""
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd13()
		  elif word == 14:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = ""
		    word_l7 = ""
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd14()
		  elif word == 15:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = "_ "
		    word_l8 = "_ "
		    word_l9 = "_ "
		    word_l10 = ""
		    wrd15()
		  elif word == 16:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = ""
		    word_l7 = ""
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd16()
		  elif word == 17:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = "_ "
		    word_l8 = "_ "
		    word_l9 = "_ "
		    word_l10 = ""
		    wrd17()
		  elif word == 18:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = ""
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd18()
		  elif word == 19:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = ""
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd19()
		  elif word == 20:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = "_ "
		    word_l8 = "_ "
		    word_l9 = "_ "
		    word_l10 = "_ "
		    wrd20()
		  elif word == 21:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = "_ "
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd21()
		  elif word == 22:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = "_ "
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd22()
		  elif word == 23:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = "_ "
		    word_l7 = ""
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd23()
		  elif word == 24:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = ""
		    word_l5 = ""
		    word_l6 = ""
		    word_l7 = ""
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd24()
		  elif word == 25:
		    word_l1 = "_ "
		    word_l2 = "_ "
		    word_l3 = "_ "
		    word_l4 = "_ "
		    word_l5 = "_ "
		    word_l6 = ""
		    word_l7 = ""
		    word_l8 = ""
		    word_l9 = ""
		    word_l10 = ""
		    wrd25()
		    
		def wrd1():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count
		  
		  real_l1 = "C"
		  real_l2 = "O"
		  real_l3 = "M"
		  real_l4 = "P"
		  real_l5 = "U"
		  real_l6 = "T"
		  real_l7 = "E"
		  real_l8 = "R"
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "COMPUTER":
		    print("YOU WIN!!")
		  else:
		   guessing()

		def wrd2():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "B"
		  real_l2 = "E"
		  real_l3 = "A"
		  real_l4 = "M"
		  real_l5 = " "
		  real_l6 = " "
		  real_l7 = " "
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "BEAM":
		    print("YOU WIN!!")
		  else:
		   guessing()
		   
		def wrd3():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "P"
		  real_l2 = "H"
		  real_l3 = "O"
		  real_l4 = "N"
		  real_l5 = "E"
		  real_l6 = " "
		  real_l7 = " "
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "PHONE":
		    print("YOU WIN!!")
		  else:
		   guessing()
		   
		def wrd4():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count
		  
		  real_l1 = "E"
		  real_l2 = "A"
		  real_l3 = "S"
		  real_l4 = "Y"
		  real_l5 = " "
		  real_l6 = " "
		  real_l7 = " "
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "EASY":
		    print("YOU WIN!!")
		  else:
		   guessing()

		def wrd5():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "D"
		  real_l2 = "E"
		  real_l3 = "S"
		  real_l4 = "T"
		  real_l5 = "R"
		  real_l6 = "O"
		  real_l7 = "Y"
		  real_l8 = "E"
		  real_l9 = "D"
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "DESTROYED":
		    print("YOU WIN!!")
		  else:
		   guessing()

		def wrd6():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count
		  
		  real_l1 = "J"
		  real_l2 = "U"
		  real_l3 = "S"
		  real_l4 = "T"
		  real_l5 = "I"
		  real_l6 = "C"
		  real_l7 = "E"
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "JUSTICE":
		    print("YOU WIN!!")
		  else:
		   guessing()

		def wrd7():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "D"
		  real_l2 = "E"
		  real_l3 = "M"
		  real_l4 = "O"
		  real_l5 = "C"
		  real_l6 = "R"
		  real_l7 = "A"
		  real_l8 = "T"
		  real_l9 = "I"
		  real_l10 = "C"
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "DEMOCRATIC":
		    print("YOU WIN!!")
		  else:
		   guessing()
		   
		def wrd8():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "F"
		  real_l2 = "U"
		  real_l3 = "T"
		  real_l4 = "U"
		  real_l5 = "R"
		  real_l6 = "E"
		  real_l7 = " "
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "PHONE":
		    print("YOU WIN!!")
		  else:
		   guessing()
		   
		def wrd9():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count
		  
		  real_l1 = "B"
		  real_l2 = "I"
		  real_l3 = "G"
		  real_l4 = "G"
		  real_l5 = "E"
		  real_l6 = "R"
		  real_l7 = " "
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "BIGGER":
		    print("YOU WIN!!")
		  else:
		   guessing()

		def wrd10():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "C"
		  real_l2 = "A"
		  real_l3 = "T"
		  real_l4 = "H"
		  real_l5 = "E"
		  real_l6 = "D"
		  real_l7 = "R"
		  real_l8 = "A"
		  real_l9 = "L"
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "DESTROYED":
		    print("YOU WIN!!")
		  else:
		   guessing()
		   
		def wrd11():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count
		  
		  real_l1 = "A"
		  real_l2 = "N"
		  real_l3 = "I"
		  real_l4 = "M"
		  real_l5 = "A"
		  real_l6 = "L"
		  real_l7 = "S"
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "ANIMALS":
		    print("YOU WIN!!")
		  else:
		   guessing()

		def wrd12():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "C"
		  real_l2 = "O"
		  real_l3 = "I"
		  real_l4 = "N"
		  real_l5 = " "
		  real_l6 = " "
		  real_l7 = " "
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "COIN":
		    print("YOU WIN!!")
		  else:
		   guessing()
		   
		def wrd13():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "C"
		  real_l2 = "L"
		  real_l3 = "O"
		  real_l4 = "U"
		  real_l5 = "D"
		  real_l6 = " "
		  real_l7 = " "
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "CLOUD":
		    print("YOU WIN!!")
		  else:
		   guessing()
		   
		def wrd14():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count
		  
		  real_l1 = "A"
		  real_l2 = "P"
		  real_l3 = "P"
		  real_l4 = "L"
		  real_l5 = "E"
		  real_l6 = " "
		  real_l7 = " "
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "APPLE":
		    print("YOU WIN!!")
		  else:
		   guessing()

		def wrd15():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "A"
		  real_l2 = "D"
		  real_l3 = "D"
		  real_l4 = "I"
		  real_l5 = "C"
		  real_l6 = "T"
		  real_l7 = "I"
		  real_l8 = "O"
		  real_l9 = "N"
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "ADDICTION":
		    print("YOU WIN!!")
		  else:
		   guessing()

		def wrd16():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count
		  
		  real_l1 = "S"
		  real_l2 = "H"
		  real_l3 = "I"
		  real_l4 = "N"
		  real_l5 = "E"
		  real_l6 = " "
		  real_l7 = " "
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "SHINE":
		    print("YOU WIN!!")
		  else:
		   guessing()

		def wrd17():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "B"
		  real_l2 = "E"
		  real_l3 = "G"
		  real_l4 = "I"
		  real_l5 = "N"
		  real_l6 = "N"
		  real_l7 = "I"
		  real_l8 = "N"
		  real_l9 = "G"
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "BEGINING":
		    print("YOU WIN!!")
		  else:
		   guessing()
		   
		def wrd18():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "E"
		  real_l2 = "X"
		  real_l3 = "P"
		  real_l4 = "E"
		  real_l5 = "R"
		  real_l6 = "T"
		  real_l7 = " "
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "EXPERT":
		    print("YOU WIN!!")
		  else:
		   guessing()
		   
		def wrd19():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count
		  
		  real_l1 = "A"
		  real_l2 = "C"
		  real_l3 = "I"
		  real_l4 = "D"
		  real_l5 = "I"
		  real_l6 = "C"
		  real_l7 = " "
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "ACIDIC":
		    print("YOU WIN!!")
		  else:
		   guessing()

		def wrd20():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "P"
		  real_l2 = "H"
		  real_l3 = "E"
		  real_l4 = "N"
		  real_l5 = "O"
		  real_l6 = "M"
		  real_l7 = "E"
		  real_l8 = "N"
		  real_l9 = "A"
		  real_l10 = "L"
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "PHENOMENAL":
		    print("YOU WIN!!")
		  else:
		   guessing()
		   
		def wrd21():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count
		  
		  real_l1 = "G"
		  real_l2 = "O"
		  real_l3 = "R"
		  real_l4 = "I"
		  real_l5 = "L"
		  real_l6 = "L"
		  real_l7 = "A"
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "GORILLA":
		    print("YOU WIN!!")
		  else:
		   guessing()

		def wrd22():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "S"
		  real_l2 = "C"
		  real_l3 = "I"
		  real_l4 = "E"
		  real_l5 = "N"
		  real_l6 = "C"
		  real_l7 = "E"
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "SCIENCE":
		    print("YOU WIN!!")
		  else:
		   guessing()
		   
		def wrd23():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "P"
		  real_l2 = "Y"
		  real_l3 = "T"
		  real_l4 = "H"
		  real_l5 = "O"
		  real_l6 = "N"
		  real_l7 = " "
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "PYTHON":
		    print("YOU WIN!!")
		  else:
		   guessing()
		   
		def wrd24():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "G"
		  real_l2 = "I"
		  real_l3 = "T"
		  real_l4 = " "
		  real_l5 = " "
		  real_l6 = " "
		  real_l7 = " "
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "GIT":
		    print("YOU WIN!!")
		  else:
		   guessing()
		   
		def wrd25():
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7
		  
		  global WsoF
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global wrong_letters
		  global fail_count

		  real_l1 = "S"
		  real_l2 = "H"
		  real_l3 = "A"
		  real_l4 = "R"
		  real_l5 = "E"
		  real_l6 = " "
		  real_l7 = " "
		  real_l8 = " "
		  real_l9 = " "
		  real_l10 = " "
		  print(hm_l1)
		  print(hm_l2)
		  print(hm_l3)
		  print(hm_14)
		  print(hm_l5)
		  print(hm_l6)
		  print(hm_l7)
		  WsoF = str(word_l1) + str(word_l2) + str(word_l3) + str(word_l4) + str(word_l5) + str(word_l6) + str(word_l7) + str(word_l8) + str(word_l9) + str(word_l10)
		  print("Word: "+str(WsoF))
		  print ("Wrong Letters: "+str(wrong_letters))
		  if WsoF == "SHARE":
		    print("YOU WIN!!")
		  else:
		   guessing()

		def guessing():
		  #globals
		  global hm_l1
		  global hm_l2
		  global hm_l3
		  global hm_14
		  global hm_l5
		  global hm_l6
		  global hm_l7

		  global WsoF
		  global word
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global real_l1
		  global real_l2
		  global real_l3
		  global real_l4
		  global real_l5
		  global real_l6
		  global real_l7
		  global real_l8
		  global real_l9
		  global real_l10
		  
		  global done_1
		  global done_2
		  global done_3
		  global done_4
		  global done_5
		  global done_6
		  global done_7
		  global done_8
		  global done_9
		  global done_10
		  
		  global wrong_letters
		  global fail_count
		  
		  #Guess
		  this_turn = "no"
		  print("Remember always enter letters in CAPITALS")
		  letter_guess = str(input("Guess a letter: "))
		  if letter_guess == real_l1 and done_1 == "":
		    word_l1 = letter_guess
		    done_1 = "_"
		    this_turn = "yes"
		  if letter_guess == real_l2 and done_2 == "":
		    word_l2 = letter_guess
		    done_2 = "_"
		    this_turn = "yes"
		  if letter_guess == real_l3 and done_3 == "":
		    word_l3 = letter_guess
		    done_3 = "_"
		    this_turn = "yes"
		  if letter_guess == real_l4 and done_4 == "":
		    word_l4 = letter_guess
		    done_4 = "_"
		    this_turn = "yes"
		  if letter_guess == real_l5 and done_5 == "":
		    word_l5 = letter_guess
		    done_5 = "_"
		    this_turn = "yes"
		  if letter_guess == real_l6 and done_6 == "":
		    word_l6 = letter_guess
		    done_6 = "_"
		    this_turn = "yes"
		  if letter_guess == real_l7 and done_7 == "":
		    word_l7 = letter_guess
		    done_7 = "_"
		    this_turn = "yes"
		  if letter_guess == real_l8 and done_8 == "":
		    word_l8 = letter_guess
		    done_8 = "_"
		    this_turn = "yes"
		  if letter_guess == real_l9 and done_9 == "":
		    word_l9 = letter_guess
		    done_9 = "_"
		    this_turn = "yes"
		  if letter_guess == real_l10 and done_10 == "":
		    word_l10 = letter_guess
		    done_10 = "_"
		    this_turn = "yes"
		  if this_turn == "no":
		    wrong_letters = str(wrong_letters)+" "+(letter_guess)
		    if fail_count == 0:
		      fail1()
		    elif fail_count == 1:
		      fail2()
		    elif fail_count == 2:
		      fail3()
		    elif fail_count == 3:
		      fail4()
		    elif fail_count == 4:
		      fail5()
		    elif fail_count == 5:
		      fail6()
		    elif fail_count == 6:
		      fail7()
		    elif fail_count == 7:
		      fail8()
		    elif fail_count == 8:
		      fail9()
		    elif fail_count == 9:
		      fail10()
		    else:
		      print("An error occured")
		  else:
		    what()
		    
		  #back to checks
		def what():
		  #globals
		  global WsoF
		  global word
		  global word_l1
		  global word_l2
		  global word_l3
		  global word_l4
		  global word_l5
		  global word_l6
		  global word_l7
		  global word_l8
		  global word_l9
		  global word_l10
		  
		  global wrong_letters
		  global fail_count
		  global correct
		  if word == 1:
		    wrd1()
		  elif word == 2:
		    wrd2()
		  elif word == 3:
		    wrd3()
		  elif word == 4:
		    wrd4()
		  elif word == 5:
		    wrd5()
		  elif word == 6:
		    wrd6()
		  elif word == 7:
		    wrd7()
		  elif word == 8:
		    wrd8()
		  elif word == 9:
		    wrd9()
		  elif word == 10:
		    wrd10()
		  elif word == 11:
		    wrd11()
		  elif word == 12:
		    wrd12()
		  elif word == 13:
		    wrd13()
		  elif word == 14:
		    wrd14()
		  elif word == 15:
		    wrd15()
		  elif word == 16:
		    wrd16()
		  elif word == 17:
		    wrd17()
		  elif word == 18:
		    wrd18()
		  elif word == 19:
		    wrd19()
		  elif word == 20:
		    wrd20()
		  elif word == 21:
		    wrd21()
		  elif word == 22:
		    wrd22()
		  elif word == 23:
		    wrd23()
		  elif word == 24:
		    wrd24()
		  elif word == 25:
		    wrd25()
		  else:
		    print("an error has occured")




		  Hangman()
				
				
	elif choice == 4:
				
				
				
	elif choice == 5:
				
				
				
	elif choice == 6:
				
				
				
	elif choice == 7:
				
				
				
	else:
		print("You are too dumb to continue")
