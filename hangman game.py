import random

def hangman_stage(life):
    stages = [
        """
        +--------+
        |        | 
        |        O
        |       \\|/
        |        |
        |       / \\
        |
        |___________ life: 0
        """,
        """
        +--------+
        |        |
        |        O
        |       \\|/
        |        |
        |       / 
        |
        |___________ life: 1
        """,
        """
        +---------+
        |         |
        |         O
        |        \\|/
        |         |
        |         
        |          
        |____________ life: 2
        """,
        """
        +----------+
        |          |
        |          O
        |         \\|
        |          |
        |
        |
        |_____________ life: 3
        """, 
        """
        +------------+
        |            |
        |            O
        |            |
        |            |
        |             
        |              
        |_______________ life: 4
        """,
        """
        +------------+
        |            |
        |            O
        |            
        |
        |
        |
        |______________ life: 5
        """,
        """
        +--------+
        |        |
        |
        |
        |
        |
        |___________ life: 6
        """
    ]
    return stages[life]

def play_game(score):
    word_list = ["python", "cloud", "sky", "editor", "hello"]
    chosen_word = random.choice(word_list)
    life = 6
    display = ['_' for _ in chosen_word]
    guessed_letters = set()
    game_over = False

    print("\n🎮 New Game of Hangman!\n")
    print(hangman_stage(life))

    while not game_over:
        print(' '.join(display))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:
            for position in range(len(chosen_word)):
                if chosen_word[position] == guess:
                    display[position] = guess
            print("✅ Correct!")
        else:
            life -= 1
            print(f"❌ Wrong! Lives left: {life}")

        print(hangman_stage(life))
        print(f"Used letters: {', '.join(sorted(guessed_letters))}")

        if '_' not in display:
            game_over = True
            score += 1
            print(f"🎉 You WIN! The word was '{chosen_word}'")
        elif life == 0:
            game_over = True
            print(f"💀 You lose! The word was '{chosen_word}'")

    print(f"🏆 Current Score: {score}")
    return score

def start():
    score = 0
    while True:
        score = play_game(score)
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print(f"\nThanks for playing! 🧠 Final Score: {score} 🏁")
            break

start()