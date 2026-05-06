'''Austin Fearon 20/4/26 This program will ask the user questions about Chris
   Wood like a quiz. After the user has answered all 8 questions appropriotely
   it will give a percentage score and state how many you got right and wrong'''
#index for questions
counter = 0
#my list of questions
questions = ["How old is he?", "How many goals has he scored?", 
             "What team does he play for now?", 
             "What was the first club he played for?",
             "Where was he born?",
             "What position does he play?",
             "What was his best season (most g/a)?",
             "How many years has he played professional football for?"]
print("This is a quiz abopuit chris wood, the questions will be multi choice " 
        "so answer 1,2,3,4")
#list for my answers
myanswers = ["1. 42\n2. 28\n3. 34\n4. 37" , 
             "1. 135\n2. 152\n3. 125\n4. 142" ,
             "1. Liverpool\n2. Nottingham Forest\n2. Arsenal\n3. Mancity\n4. Man United" ,
             "1. Wellington Pheonix\n2. Onehunga club\n3. Auckland United\n4. Otumoetai FC", 
             "1. Auckland\n2. Tauranga\n3. Hamilton\n4. Dunedin", "1. Midfield\n2. Center back\n3. Striker\n4. Winger" ,
             "1. 54 G/A\n2. 39 G/A\n3. 25 G/A\n4. 23 G/A" , "1. 17\n2. 25\n3. 28\n4. 22"]
# variables, lists and indexes that I need
canswers = [3, 1, 2, 2, 1, 3, 4, 1]
index = 0
ansnum = 0
correctans = []
wrongans = []
#making for loop which asks each question and answer whilst checking for
#boundaries and invalid input
for i in questions:
    print(questions[counter])
    for i in myanswers:
      print(myanswers[ansnum])
      ans = input("What is your answer: ")
      print("")
      while True :
        try:
            ans_int = int(ans)
            if ans_int >= 1 and ans_int <= 4:
              break
            else:
              print("Please enter an actual number between 1 and 4.")
              ans = input("What is your answer: ")
              print("")
        except ValueError:
            print("Please enter an actual number between 1 and 4.")
            ans = input("What is your answer: ")
            print("")
      if ans_int == canswers[index]:
        correctans.append(ans_int)
        break
      else:
       wrongans.append(ans_int)
       break
    counter = counter + 1
    index = index  + 1
    ansnum = ansnum + 1
#collected data from each list to check how many user got right and wrong
#calculating percentage
len1 = len(correctans)
len2 = len(wrongans)
perc = len1/8
perc = perc*100
#final print statement
print(f"You got {len2} wrong, and {len1} right, meaning you got {perc}%!")