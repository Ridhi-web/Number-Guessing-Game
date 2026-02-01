import random
import sys

ICONS = {
    'game': '\uf11b',
    'chart': '\uf080',
    'target': '\uf140',
    'error': '\uf00d',
    'fire': '\uf06d',
    'warm': '\uf2c9',
    'cold': '\uf2dc',
    'dice': '\uf522',
    'pin': '\uf041',
    'bye': '\uf2b5',
    'warn': '\uf071',
    'win': '\uf091',
    'party': '\uf79c',
    'up': '\uf062',
    'down': '\uf063',
    'retry': '\uf021'
}

LEVELS = {
    '1': {'name': 'Easy',   'min': 1, 'max': 50,  'attempts': 10},
    '2': {'name': 'Medium', 'min': 1, 'max': 100, 'attempts': 7},
    '3': {'name': 'Hard',   'min': 1, 'max': 200, 'attempts': 6}
}

def play_game():
    print(f"\n{ICONS['game']} WELCOME TO NUMBER GUESS {ICONS['game']}")
    
    games_played = 0
    games_won = 0
    total_score = 0
    
    while True:
        games_played += 1
        
        print(f"\n{ICONS['target']} Select Difficulty:")
        for key, level in LEVELS.items():
            print(f" {key}. {level['name']} (Range: {level['min']}-{level['max']}, Tries: {level['attempts']})")
        
        choice = input("> ").strip()
        while choice not in LEVELS:
            print(f"{ICONS['error']} Invalid! Please choose 1, 2, or 3.")
            choice = input("> ").strip()
        
        settings = LEVELS[choice]
        min_number = settings['min']
        max_number = settings['max']
        max_tries = settings['attempts']
        
        target_number = random.randint(min_number, max_number)
        
        print(f"\n{ICONS['dice']} I'm thinking of {min_number}-{max_number}. You have {max_tries} tries.")
        
        player_won = False
        
        for attempt in range(max_tries):
            tries_left = max_tries - attempt
            print(f"\n{ICONS['pin']} Attempt {attempt + 1}/{max_tries}")
            
            try:
                user_input = input("  Guess: ").strip().lower()
                
                if user_input in ['q', 'quit']:
                    print("Quitting game...")
                    return
                
                guess = int(user_input)
                
                if guess < min_number or guess > max_number:
                    print(f"  {ICONS['warn']} Please guess between {min_number} and {max_number}!")
                    continue
                
                if guess == target_number:
                    points = (tries_left * 10)
                    total_score += points
                    games_won += 1
                    player_won = True
                    
                    print(f"\n{ICONS['party']} CORRECT! The number was {target_number}.")
                    print(f"  You earned {points} points! {ICONS['win']}")
                    break
                
                difference = abs(guess - target_number)
                
                if difference <= 5:
                    hint = "VERY CLOSE!"
                    icon = ICONS['fire']
                elif difference <= 10:
                    hint = "Warm"
                    icon = ICONS['warm']
                else:
                    hint = "Cold"
                    icon = ICONS['cold']
                
                if guess < target_number:
                    direction = "Too Low"
                    arrow = ICONS['up']
                else:
                    direction = "Too High"
                    arrow = ICONS['down']
                
                print(f"  {arrow} {direction}! {icon} {hint}")
                
            except ValueError:
                print(f"  {ICONS['error']} Please enter a valid number!")
        
        if not player_won:
            print(f"\n{ICONS['cold']} Game Over! The number was {target_number}.")
            
        print(f"\n{ICONS['chart']} Games: {games_played} | Won: {games_won} | Score: {total_score}")
        
        play_again = input(f"\n{ICONS['retry']} Play again? (y/n): ").lower()
        if play_again not in ['y', 'yes']:
            break
            
    print(f"\n{ICONS['bye']} Thanks for playing!")

if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        sys.exit()
