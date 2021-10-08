def play_again() -> bool:
    #in a while loop with condition True, input string return True or False
    #
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    #play = input('Play again?\n')
    while True:
        play = input('Play again?\n')
        if play == 'Y' or 'Yes':
            return get_bank()
        elif play == 'N' or 'No':
            return play
        else:
            print('Please enter another value')
            return play

    return True
     
def get_wager(bank : int) -> int:
    #in a while loop input integer
    #return wager if it is valid
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    bank = int(input('How many chips do you want to start with?\n'))
    while bank >= 0:
        if bank >= 101:
            print('Too high a value, you can only choose 1-100 chips')
            return bank
        elif bank <= 0:
            print('Too low a value, you can only choose 1-100 chips')
        else:
            wager = int(input('How many chips do you want to wager'))
            return 
    return 1            

def get_slot_results() -> tuple:
    #reela, reelb, reelc = random.randint(1,10), random.randint(1,10)
    ''' Returns the result of the slot pull '''
    reela == random.randint(1,10)
    reelb == random.randint(1,10)
    reelc == random.randint(1,10)
    return reela, reelb, reelc

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    matches = 0
    if reela == reelb:
        matches += 2
        if reela == reelc:
            mathces += 1
    elif reela == reelc:
        matches =+ 2
        if reela == reelb:
            matches += 1
    elif reelb == reelc:
        matches += 2
        if reelb == reela:
            matches += 1
    return matches

def get_bank() -> int:
    #in a while loop, input integer
    ''' Returns how many chips the user wants to play with. Loops until a value greater than 0 and less than 101 '''
    num = 0
    while num == 0:
        bankStart = int(input('How many chips do you want to start with?\n'))
        if bankStart <= 0:
            print('Too low a value, you can only choose between 1 - 100 chips')
        elif bankStart > 100:
            print('Too high a value, you can only choose between 1 - 100 chips')
        else:
            num = 1
    return bankStart

def get_payout(wager, matches):
    #wager * 10  - wager
    #wager * 3 - wager
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 5 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        x = (wager * 10) - wager
    elif matches == 2:
        x = (wager * 3) - wager
    elif matches == 0:
        x = wager - wager - wager
    return x   


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while True:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()


How many chips do you want to start with? ==> -1
Too low a value, you can only choose 1 -100 chips
How many chips do you want to start with? ==> 500
Too high a value, you can only choose 1 -100 chips
How many chips do you want to start with? ==> 10
How many chips do you want to wager? ==> -1
The wager amount must be greater than 0.Please enter again.
How many chips do you want to wager? ==> 12
The wager amount cannot be greater than how much you have.  10
How many chips do you want to wager? ==> 5
Your spin 4 2 9
You matched 0 reels
You won/lost -5
Current bank 5
How many chips do you want to wager? ==> 1
Your spin 9 6 6
You matched 2 reelsYou won/lost 2
Current bank 7
How many chips do you want to wager? ==> 8
The wager amount cannot be greater than how much you have.  7
How many chips do you want to wager? ==> 7
Your spin 3 33
You matched 3 reels
You won/lost 63
Current bank 70
How many chips do you want to wager? ==> 70
Your spin 6 1 3
You matched 0 reelsYou won/lost -70
Current bank 0
You lost all 10 in 4 spins
The most chips you had was 70
Do you want to play again? ==>e
You must enter Y/YES/N/NO to continue.  
Please try again
Do you want to play again? ==> n