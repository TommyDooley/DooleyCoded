import random
random_number = random.randint(1, 9)

name = input("What is your name?: ")
question = input("Ask your question: ")
answer = ""

if question == " ":
  print("YOU WILL BREAK THE FABRIC OF REALITY!!! ASK A QUESTION!")
elif name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

if random_number == 1:
  answer = "Definitely!"
elif random_number == 2:
 answer = "Try again later"
elif random_number == 3:
  answer = "You got it!"
elif random_number == 4:
  answer = "Doubtful."
elif random_number == 5:
  answer = "Yes!"
elif random_number == 6:
  answer = "Nope."
elif random_number == 7:
  answer = "Absolutely!"
elif random_number == 8:
  answer = "I wouldn't count on it."
elif random_number == 9:
  answer = "Unlikely."
else:
  print("Error!")

print("Magic 8-Ball's answer: " + answer)