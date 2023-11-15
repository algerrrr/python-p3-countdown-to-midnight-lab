import time

def countdown(num):
    x = num
    while x > 0:
        print(f'{x} SECOND(S)!')
        x-= 1
    print("HAPPY NEW YEAR!")

#countdown(10)

def countdown_with_sleep(num):
    x = num
    while x > 0:
        print(f'{x} SECOND(S)!')
        x-= 1
        time.sleep(2)
    print("HAPPY NEW YEAR!")
