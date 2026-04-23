counter = 0
questions = ["How old is he?", "How many goals has he scored?", "What team does he play for now?", "What was the first club he played for?", "Where was he born?"
, "What position does he play?", "What was his best season (most g/a)?", "How many years has he played professional football for?"]
print("This is a quiz abopuit chris wood, the questions will be multi choice so answer 1,2,3,4")
myanswers = ["1. 42\n2. 28\n3. 34\n4. 37" , "1. 135\n2. 152\n3. 125\n4. 142" ,"1. Liverpool\n2. Nottingham Forest\n2. Arsenal\n3. Mancity\n4. Man United" 
, "1. Wellington Pheonix\n2. Onehunga club\n3. Auckland United\n4. Otumoetai FC"]
Canswers = ["3", "1", "2", "2", "1", "3", "4", "1"]
index = 0
correctans = []
wrongans = []
for i in questions:
    print(questions[counter])
    for i in myanswers:
     print(i)
     ans = input("What is your answer: ")
     if ans == Canswers[index]:
       correctans.append(ans)
     else:
      wrongans.append(ans)
     counter = counter + 1
     index = index  + 1