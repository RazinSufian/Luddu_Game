import time
import random
from isdigit import IsDigit

class Ludu:
    Result_output={}
    Result={}
    standing_count=0
    player_completed=[]
    def __init__(self) -> None:
        pass
        
    def standings(self,player_name):
        Ludu.standing_count+=1
        print(f"{player_name} has took the {Ludu.standing_count} position ")
        Ludu.player_completed.append(player_name)


class Player(Ludu):
    def __init__(self,n,p_no):
        self.name=n
        self.player_no=p_no
        self.token={1:False,2:False,3:False,4:False}
        text_4=f"WELCOME to the game as player{p_no}: {self.name[0:len(self.name)-2:1]}"
        for char in text_4:
            print(char, end='', flush=True)
            time.sleep(0.05)
        Ludu.Result[self]=self.token
        Ludu.Result_output[self.name]=self.token
        self.game_status=True
        pass


    def points(self,lst):
        active_tokens= [val for val in self.token.values() if isinstance(val,(int))]
        if (all([type(x)==bool and x== False for x in self.token.values()])) and 6 not in lst:
            return(print(f"Your Score{lst}\nAll false\nNo token can be palyed"))
        elif ((len(active_tokens)*25)-sum(active_tokens))<sum(lst):
            return(print(f"Your Score{lst}\nTotalScore_Overload\nNo token can be palyed"))

        elif  all([max(lst)>(25-x) for x in active_tokens]):
            return(print(f"Your Score{lst}\nIndividualToken_Overload\nNo token can be palyed"))
        else:
            print(f"Your score is {lst}")
            print(Ludu.Result_output) 
            for i in lst:
                Attempt=True
                while Attempt:
                    token_no=int(input((f"Play {i} in token no:")))
                    if type(token_no)!= int or token_no>4:
                        print("Wrong input. Try again")


                    else:
                        
                        if Ludu.Result[self][token_no]==False and i==6:
                            Ludu.Result[self][token_no]=0
                            print(Ludu.Result_output) 
                            break

                        elif type(Ludu.Result[self][token_no])== bool or (Ludu.Result[self][token_no]+i) >25:
                            print("Wrong token choosen. Try again")
                            print(Ludu.Result_output)
    
                        else:
                            new_place_occuppied=Ludu.Result[self][token_no]+i
                            if new_place_occuppied==25:
                                Ludu.Result[self][token_no]=True
                                print(Ludu.Result_output) 
                                break
                            else:
                                Ludu.Result[self][token_no]=new_place_occuppied
                                count=0
                                for loc,dic in  Ludu.Result.items():
                                    count+=1
                                    if count==self.player_no:
                                        pass
                                    else:
                                        for token_no,place in dic.items():
                                            if new_place_occuppied== place:
                                                print(Ludu.Result[loc][token_no])
                                                Ludu.Result[loc][token_no]=False
                                print(Ludu.Result_output) 
                                break
        
        if all(self.token.values()):
            self.game_status=False
            super().standing_count(self.name)



player_obj=[]

def _player_making(num):
    count=1
    for i in range (num):
        text_2=f"you are Player-{count}\nEnter your name:"
        for char in text_2:
            print(char, end='', flush=True)
            time.sleep(0.05)
        name=input("")
        name=name+(f"_{count}")
        player_obj.append(Player(name,count))
        print("")

        count+=1
    #print(player_obj)



text_1 = "Welcome to the game...\nEnter how many players want to play(MAX 4):"

for char in text_1:
    print(char, end='', flush=True)
    time.sleep(0.05)

_num_player=input()
Input=True


while Input:

    if _num_player.isdigit() and int(_num_player)<=4:
        _num_player=int(_num_player)
        Input=False
        _player_making(_num_player)
        pass
    else:
        text_3="Wrong_input...\nTry again...\nEnter how many players want to play(MAX 4):"
        for char in text_3:
            print(char, end='', flush=True)
            time.sleep(0.05)
        _num_player=input()


def die_roll(str):
    roll=True
    while roll:
        if str=="s" or str=="S":
            roll==False
            return True
        else:
            print("Wrong botton. Try again")
            str=input("Press s to role your die play")


def rolling_a_die(player_no):
    temp_score=[]
    count=0
    for i in range(3):
        inpt=input(f"Press s to roll your die Player{player_no}:")
        if die_roll(inpt):
            for i in range(3):
                trial=random.randint(1,6)
                if trial==6:
                    score=trial
                    break
                else:
                    score=trial

            if score==6:
                print("You scored a six congo")
                count+=1
                if count==3:
                    print("You got six 3 times. Unlucky")
                    return rolling_a_die(player_no)
                temp_score.append(score)
            else:
                temp_score.append(score)
                return temp_score

Game=True
while Game:

    rolling_num=1
    for i in player_obj:
        #print(i.name)
        if i.game_status==True:
            scored=rolling_a_die(rolling_num)
            i.points(scored)
            rolling_num+=1
            if Ludu.player_completed==_num_player:
                print("Game Has Ended")
                print (Ludu.player_completed)
                Game=False

        else:
            rolling_num+=1
            pass
        

            









    
