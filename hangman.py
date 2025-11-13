import random

words = [
    "In", "a", "quiet", "mountain", "village", "an", "old", "clockmaker", "named", "Harun", "built", "a", "clock", "that", "never", "ticked", "The", "villagers", "mocked", "him", "saying", "What", "use", "is", "a", "silent", "clock", "But", "Harun", "only", "smiled", "and", "said", "It", "will", "speak", "when", "the", "time", "is", "right", "One", "stormy", "night", "lightning", "struck", "the", "tower", "and", "the", "clock", "began", "to", "tick", "slowly", "but", "backward", "Time", "reversed", "Broken", "homes", "repaired", "themselves", "lost", "friends", "returned", "and", "regrets", "turned", "into", "second", "chances", "At", "sunrise", "everything", "went", "still", "Only", "Harun", "remembered", "He", "smiled", "and", "said", "Time", "listens", "to", "those", "who", "use", "it", "wisely", "Lesson", "Value", "time", "before", "it", "chooses", "to", "stop", "for", "you"
]

print("\n\t !!! Hangman Game !!! \n")
print("Rules:")
print("1. I will pick a secret word from a story.")
print("2. You must guess the word one letter at a time.")
print("3. You have 5 wrong attempts — use them wisely!")
print("4. If you reveal all letters before attempts run out, you win!\n")

name = input("Enter your name: ")
print(f"\nAssalam-o-Alaikum {name}! Let's begin the game.\n")

score = 0
play_again = "yes"

while play_again.lower() == "yes":
    word = random.choice(words).lower()
    guessed_letters = []
    attempts = 5
    display_word = ["_"] * len(word)

    print("\nNew Round Starting!\n")
    print("You have", attempts, "wrong attempts. Let's start!\n")

    while attempts > 0 and "_" in display_word:
        print("\nWord:", " ".join(display_word))
        print("Guessed letters:", ", ".join(guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess
        else:
            print("Wrong guess!")
            attempts -= 1
            print("Attempts left:", attempts)

    if "_" not in display_word:
        print(f"\nCongratulations {name}! You guessed the word:", word)
        score += 1
    else:
        print(f"\nGame Over, {name}. The word was:", word)
    print(f"Your current score: {score}\n")

    play_again = input("Do you want to play another round? (yes/no): ")
    while play_again.lower() not in ["yes", "no"]:
        play_again = input("Invalid input. Please enter 'yes' or 'no': ")

print(f"\nThanks for playing, {name}! Your final score: {score}")
print("May your time always move forward wisely, Ameen!")

