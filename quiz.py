
a_count = 0 #Katherine Johnson
b_count = 0 #Marie Curie
c_count = 0 #Radia Perlmen
d_count = 0 #Edith Clarke

q1_answer = raw_input("What is your favourite subject? a) Maths, b) Science, c) Technology, d) Engineering ")

if q1_answer.lower() == 'a':
    a_count += 1
elif q1_answer.lower() == 'b':
    b_count += 1
elif q1_answer.lower() == 'c':
    c_count +=1
elif q1_answer.lower() == 'd' :
    d_count+=1
else: print("Sorry, I don't understand that response.")

q2_answer = raw_input("Which area do you have the most interest in? a) Space, b) Medicine, c) Computers and the internet, d) Electrical engineering ")

if q2_answer.lower() == 'a':
    a_count += 1
elif q2_answer.lower() == 'b':
    b_count += 1
elif q2_answer.lower() == 'c':
    c_count +=1
elif q2_answer.lower() == 'd' :
    d_count+=1
else: print("Sorry, I don't understand that response.")

q3_answer = raw_input("What are you best at? a) Long maths equations, b) Research, c) Inventing something to make life easier, d) Sharing what you have learnt ")

if q3_answer.lower() == 'a':
    a_count += 1
elif q3_answer.lower() == 'b':
    b_count += 1
elif q3_answer.lower() == 'c':
    c_count +=1
elif q3_answer.lower() == 'd' :
    d_count+=1
else: print("Sorry, I don't understand that response.")

q4_answer = raw_input("What would you like to be awarded? a) Presidential Medal of Freedom, b) Nobel Prize, c) National Inventors Hall of Fame , d)  Society of Women Engineers Achievement Award ")

if q4_answer.lower() == 'a':
    a_count += 1
elif q4_answer.lower() == 'b':
    b_count += 1
elif q4_answer.lower() == 'c':
    c_count +=1
elif q4_answer.lower() == 'd' :
    d_count+=1
else: print("Sorry, I don't understand that response.")

q5_answer = raw_input("How many siblings do you have? a) 0, b) Between 1 and 3, c) Between 4 and 6 , d) More than 6 ")

if q5_answer.lower() == 'a':
    c_count += 1
elif q5_answer.lower() == 'b':
    a_count += 1
elif q5_answer.lower() == 'c':
    b_count +=1
elif q5_answer.lower() == 'd' :
    d_count+=1
else: print("Sorry, I don't understand that response.")

if a_count > b_count and a_count > c_count and a_count > d_count:
    print "You're Katherine Johnson!" #include info and photo?
elif b_count > a_count and b_count > c_count and b_count > d_count:
    print "You're Marie Curie!"
elif c_count > a_count and c_count > b_count and c_count > d_count:
    print "You're Radia Perlman!"
elif d_count > a_count and d_count > b_count and d_count > c_count:
    print "You're Edith Clarke!"
