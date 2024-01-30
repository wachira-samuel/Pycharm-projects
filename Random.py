import random
def rollDice():
    roll=random.randint(1,100);
    if roll==100:
        print(roll,"Roll was 100,you lose.What are the odds?play again!")
        return False
    elif 100>roll>50:
        print(roll,"roll was 51-99,you win! *pretty lights flash*(play more!)")
        return True
def simple_better(funds, initial_wager, wager_count):
    value=funds
    wager=initial_wager
    currentWager=0
    while currentWager<wager_count:
        if rollDice():
            value+=wager
        else:
            value-=wager
        currentWager +=1
        print("Funds:",value)
simple_better(10000,1000,100)
