import random
import time

def main():
    """The main function that generates random number and id-s where you specific the number or id lenght"""
    
    #Intro User
    print("Number Generator by Rafa")
    statament = True
    # While Statement
    codes = []
    while statament:
        inp = input("""
(INFO) - DON'T PRESS JUST &, THE PROGRAM WILL CRASH!!!
enter your number lenght -ex. 34
type & and lenght id: -ex.&34
quit = to QUIT
show - to show all numbers and id-s
command:: """)
        numbers = [0,1,2,3,4,5,6,7,8,9]
        l = []

        if inp == 'quit':
            statament = False
            print("")
            print("Goodbye  :)) ")
            break
        if inp == '':
            print("")
            print('nothingh')
            # Code
        if inp == 'show':
            print()
            n = 0
            print('Showing your list:')
            for x in codes:
                n += 1
                print(str(n) + ': ' + str(x))

        if inp.startswith('&'):
            characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z'] + numbers
            for i in range(0, int(inp.strip('&'))):
                    random.shuffle(characters)
                    l.append(str(characters[random.randint(0,34)]))   
                    print('creating number...')
                    num = ''.join(l)
            codes.append(num)
            print("")
            print(f"YOUR RANDOM ID IS: {num}")
        else:
            try:
                for i in range(0, int(inp)):
                    random.shuffle(numbers)
                    l.append(str(numbers[random.randint(0,9)]))   
                    print('creating number...')
                num = ''.join(l)
                codes.append(num)
                print("")
                print(f"YOUR NUMBER IS: {num}")
            except ValueError :
                    print("")
                    print("You can not add a string")
    
main()