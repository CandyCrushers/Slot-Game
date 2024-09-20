import random 

balance = 1000 

def credits(balance):
    if balance >= 0: 
        how_much = int(input("How much would you like to put in?"))
    while how_much > balance: 
        print("That is not a valid amount!")
        how_much = (int(input("How much would you like to put in?")))
    if balance <= 0:
        print("You do not have enough to play!") 
        want_more = input("Would you like to add more into your balance? Y/N").lower()
        if want_more == 'y':
            more(balance)
    
    
    
    
    spin = input("Would you like to spin!? Y/N").lower()
    
    if spin == 'y':
        slot_machine(balance, how_much)
    else: 
        print("Thanks for playing!!") 
        
        
        
def slot_machine(balance, how_much): 
    
    slot1 = random.randint(1,10)
    slot2 = random.randint(1,10)
    slot3 = random.randint(1,10)
    
    print(slot1, slot2, slot3)
    
    if slot1 == slot2 == slot3:
        take_in = how_much * 2
        balance += take_in
        print("You have won " + str(take_in) + " your balance is now: " + str(balance))
        spin = input("Would you like to spin!? Y/N").lower()
    else: 
        balance -= how_much
        print("You have lost! Your balance is now: " + str(balance))
    if balance <= 0:
        credits(balance)
    spin = input("Would you like to spin!? Y/N").lower()    
        
    if spin == 'y':
        credits(balance)
    else: 
        print("Thanks for playing!") 

def more(balance):
    mores = int(input("How much would you like to put into your balance!"))
    balance += mores
    credits(balance)
    
credits(balance)