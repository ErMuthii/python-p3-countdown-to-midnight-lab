
import time

def countdown(x):
    x = 10
    while x > 0:
        print(f'{x} SECONDS(S)!')
        x -= 1

print('HAPPY NEW YEAR!')


def countdown_with_sleep(x):
    x = 10
    while x > 0:
        print(f'{x} SECONDS(S)')
        time.sleep(1)
        x -= 1
print('HAPPY NEW YEAR')