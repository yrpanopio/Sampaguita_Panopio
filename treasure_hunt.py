name = input("Enter player name: ")
coins = 0
def check_guess(guess):
    if guess == 3:
        return 10
    else:
        return 0

def get_achievement(coins):
    if check_guess(guess) >= 30:
        return "Treasure Master!"
    elif check_guess(guess) >= 20:
        return "Gold Explorer!"
    elif check_guess(guess) >= 10:
        return "Bronze Explorer!"
    elif check_guess(guess) < 0:
        return "Treasure Beginner!"

def display_result(name, coins,title):
    print(f"Player name: {name}")
    print(f"Total coins: {coins}")
    print(f"Achievement: {get_achievement(coins)}")

for i in range(1, 4):
    guess = int(input("Guess the secret number (1-5): "))
    check_guess(guess)
    if check_guess(guess) == 10:
        print ("Correct! You've earned 10 coins.")
    else:
        print("Incorrect! You've earned 0 coins.")
    guess += coins

get_achievement(coins)
display_result(name, coins, get_achievement(coins))



