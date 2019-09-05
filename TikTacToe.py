import random
print("Welcome to The TicTackToe")
game_over=True
a=int(input("Press 1 to begin the game and 0 to exit"))
arr=["_","_","_","_","_","_"," "," "," "]
arr1=[1,2,3,4,5,6,7,8,9]
def for_loop(b,c):
    if c==1:
        arr[b-1]="0"     
    if c==2:  
        arr[b-1]="X"
    for i in range(0,9,3):
            print(f"{arr[i]}|{arr[i+1]}|{arr[i+2]}")
def win_only():
    for i in range(0,9):
        global game_over
        if i%3==0:
            if arr[i]==arr[i+1]==arr[i+2] and (arr[i]!="_" and arr[i]!=" "):
                game_over=False
        if i==1 or i==2 or i==0:
            if arr[i]==arr[i+3]==arr[i+6] and (arr[i]!="_" and arr[i]!=" "):
                game_over=False
        if arr[0]==arr[4]==arr[8] and (arr[0]==arr[4]==arr[8]!="_" and arr[0]==arr[4]==arr[8]!=" "):
            game_over=False
        if arr[2]==arr[4]==arr[6] and (arr[2]==arr[4]==arr[6]!="_" and arr[2]==arr[4]==arr[6]!=" "):
            game_over=False
    return game_over
def comp(cc):
    c=random.choice(arr1)
    arr1.remove(c)
    cc+=1
    for_loop(c,2)
    return cc
def game():
    counter=0
    print("\t1|2|3")
    print("\t4|5|6")
    print("\t7|8|9 \n")
    print("These are the respective positions.Please remember them")
    print("your sign is 0 and computer's is X")
    print("Game Start's")
    for h in range(5):
        if win_only():
          b=int(input("Enter your position where you want to enter the number"))
          counter+=1
          arr1.remove(b)
          if b>=1 and b<=9:
            for_loop(b,1)
        if win_only():
           counter=comp(counter)  
        else:
            break  
    return counter
if a==1:
    print("Let's begin.")
    if game()%2==0:
        print("Computer won")
    else:
        print("You won")
elif a==0:
    print("Bye! Have a nice day")
else:
    print("Enter the coreect number")