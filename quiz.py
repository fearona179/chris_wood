counter = 0
questions = ["How old is he?", "How many goals has he scored?", "What team does he play for now?", "What was the first club he played for?", "Where was he born?"
, "What position does he play?", "What was his best season (most g/a)?", "How many years has he played professional football for?"]
print("This is a quiz abopuit chris wood, the questions will be multi choice so answer 1,2,3,4")
myanswers = ["1. 42\n2. 28\n3. 34\n4. 37" , "1. 135\n2. 152\n3. 125\n4. 142" ,"1. Liverpool\n2. Nottingham Forest\n2. Arsenal\n3. Mancity\n4. Man United" 
, "1. Wellington Pheonix\n2. Onehunga club\n3. Auckland United\n4. Otumoetai FC", "1. Auckland\n2. Tauranga\n3. Hamilton\n 4. Dunedin", "1. Midfield\n2. Center back\n3. Striker\n4. Winger"
    , "1. 54 G/A\n2. 39 G/A\n3. 25 G/A\n4. 23 G/A" , "1. 17\n2. 25\n3. 28\n4. 22"]
Canswers = ["3", "1", "2", "2", "1", "3", "4", "1"]
index = 0
ansnum = 0
correctans = []
wrongans = []
for i in questions:
    print(questions[counter])
    for i in myanswers:
     print(myanswers[ansnum])
     ans = input("What is your answer: ")
     if ans == Canswers[index]:
       correctans.append(ans)
       break
     else:
      wrongans.append(ans)
      break
    counter = counter + 1
    index = index  + 1
    ansnum = ansnum + 1
len1 = len(correctans)
len2 = len(wrongans)
perc = len1/8
perc = perc*100
print(f"You got {len2} wrong, and {len1} right, meaning you got {perc}%!")