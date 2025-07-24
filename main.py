import random


easy_words = [
    "apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "pear", "plum",
    "mango", "peach", "lime", "melon", "berry"
]
normal_words = [
    "elderberry", "honeydew", "papaya", "apricot", "coconut",
    "nectarine", "orange", "pomegranate", "mulberry", "cranberry"
]
hard_words = [
    "rambutan", "durian", "longan", "persimmon", "tamarillo",
    "jackfruit", "loquat", "soursop", "physalis", "cherimoya"
]


print("Welcome to the word guessing game")
print("choose your dificulty level : easy, normal, hard")


lever=input("Enter the level: ").lower()
if lever == "easy":
    secret = random.choice(easy_words)
elif lever == "normal":
    secret = random.choice(normal_words)
elif lever == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid level. defaulting to easy level")
    word_list = easy_words
    secret = random.choice(easy_words)

attempts = 0
print("\n Guess the word")

while True:
  guess=input("Enter your guess: ").lower()
  attempts += 1

  if guess == "exit":
    print("Good Bye")
    break
  if guess == secret:
    print(f"Congratulations! You guessed the word {secret} in {attempts} attempts.")
    break


  hint=""
  for i in range(len(secret)):
    if i < len(guess) and guess[i] == secret[i]:
      hint += secret[i]
    else:
      hint += "*"
  print(f"Hint: {hint}")
print(  )
