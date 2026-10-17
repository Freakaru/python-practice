
#Navn input
name = input("hva er navnet dit? ")
if not name:
    name = "Person"

print(f"Hello {name} ")

import random

#Addisjon

math_question_0 = random.randint(-100, 1000)
math_question_1 = random.randint(-100, 1000)

#Subbstraksjon
math_question_2 = random.randint (1, 1000)
math_question_3 = random.randint (1, 1000)

#Multiplikasjon 
math_question_4 = random.randint (0, 100)
math_question_5 = random.randint (0, 100)

#Divisjon
math_question_6 = random.randint (100, 1000)
math_question_7 = random.randint (1, 10)

#dice roll
result = random.randint(1, 5)

#bruk # her for å ha spesefik result
print ("the question is:", result)
#result = 5
#result = 4
#result = 3
#result = 2
#result = 1

#if result osv
if result == 1:
    print ("Hva er svaret?")
    print (f"{math_question_0} + {math_question_1}")
    svaret_0 = input("Svar? ")
    if not svaret_0:
        print ("Feil")
    elif int(svaret_0) == math_question_0 + math_question_1:
        print ("korrekt")
    else:
        print ("Feil")

if result == 2:
    print ("Hva er SVARET?")
    print (f"{math_question_2} - {math_question_3}")
    svaret_1 = input ("Svar? ")
    if not svaret_1:
        print ("Feil")
    elif int (svaret_1) == math_question_2 - math_question_3:
        print ("korrekt")
    else:
        print ("Feil")

if result == 3:
    print ("Hva er svaret?!")
    print (f"{math_question_4} * {math_question_5}")
    svaret_2 = input("Svar? ")
    if not svaret_2:
        print ("Feil")
    elif int (svaret_2) == math_question_4 * math_question_5:
        print ("korrekt")
    else:
        print ("Feil")

if result == 4:
    print ("hva er svaret til denne oppgaven som jeg har kodet til deg min veldig gode venn")
    print (f"{math_question_6} / {math_question_7}")
    svaret_3 = input ("Hva er svaret til denne oppgaven som jeg har gitt til deg min veldig gode venn? ")
    if not svaret_3:
        print ("Feil")
    elif float (svaret_3) == math_question_6 / math_question_7:
        print ("korrekt")
    else:
        print ("Feil")

if result == 5:
    print (f"HELLO {name} AND WELCOME TO MY QUIZ!!! by Simen")
    score = 0
    questions_0 = {
        "Whats the Creators Name?": "Simone",
        "Whos the best teacher?": "Øyvind",
        "Who is the best student?": "Simone"
    } 
    for q, ans in questions_0.items():
        r = input(q + " ")
        if r == ans: score += 1
    print (f"Score: {score}/{len(questions_0)}")

    












