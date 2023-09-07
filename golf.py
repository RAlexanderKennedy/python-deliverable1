name = input("Welcome to GC mini golf! What is your name?")
length = int(input("Hi, " + name + "! Would you like to play 3 or 6 holes?"))
score = 0

for current in range(length):
    putts = int(input("How many putts for hole " + str(current + 1) + "? (par: 3)"))
    score += putts

par = 3*length

if score > par:
    print("Nice try, " + name + "... Your total score was: +" + str(score - par))
elif score == par:
    print("Good game, " + name + ". Your total score was: 0")
else:
    print("Great job, " + name + "! Your total score was: -" + str(par - score))

