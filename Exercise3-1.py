# Programming Exercise 3-1

def squared(): # define function
    cmd = input("Please enter an integer: ") # takes input from user 
    i = 1 # set counter var - starts at 1 
    while i <= int(cmd): # while counter is less or equal to user input 
        if i == 5: # checks if counter equals 5 
            break # function break
        print(f'{i} squared is {i**2}') # f string within print statement that returns "i squared is i^2"
        i += 1 # add to counter 
        
squared()