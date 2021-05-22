import random
import math
def play():
    user=input("what's your choice? press r for rock \n press p for paper \n press s for scissor")
    user=user.lower()
    
    computer=random.choice(['r','p','s'])

    if user==computer:
        return (0,user,computer)

    if is_win(user,computer):
        return (1,user,computer)
    return (-1,user,computer)

def is_win(player,opponent):
    #return true if the player beats the opponent
    #winning condition
    if(player=='r' and opponent=='s') or (player=='s'and opponent=='p') or (player=='p' and opponent=='r'):
        return True
    return False  

def play_best_of(n):
    player_wins=0
    computer_wins=0
    wins_necessary = math.ceil(n/2)
    while player_wins<wins_necessary and computer_wins<wins_necessary:
        result,user,computer =play()
        #tie
        if result==0:
            print("its a tie. you and computer both have same choice {}. \n".format(user))
        #you win
        elif result==1:
            player_wins +=1
            print("you choose {} and computer choose {}. you won! \n".format(user,computer))    
        else:
            computer_wins+=1
            print("you choose {} and computer choose {}. you lost! \n".format(user,computer))    
        print("\n")  
    if player_wins==computer_wins:
        print("you have won the best of {} game".format(n))
    else:
        print("computer has won the best of {} games". format(n))


if __name__ == '__main__':
    play_best_of(3) #2
    play_best_of(9) #5




