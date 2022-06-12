import RPi.GPIO as GPIO
from time import sleep
import sys
from datetime import datetime

#PINS
A = 8
B = 10
C = 12
D = 16
E = 18
F = 22
G = 24
DP = 26
DIG1 = 3
DIG2 = 5
DIG3 = 7
DIG4 = 11

SEGMENTS = [A, B, C, D, E, F, G, DP]
DIGITS = [DIG1, DIG2, DIG3, DIG4]
COLON = 13

PERIOD = 0.005

BRIGHTNESS=1

def choose_digit(i):
    #assert i <= len(DIGITS) and i > 0
    GPIO.output(DIGITS, GPIO.HIGH)
    GPIO.output(DIGITS[i-1], GPIO.LOW)

def write_zero():
    GPIO.output([A, B, C, D, E, F], GPIO.HIGH)
    GPIO.output([G, DP], GPIO.LOW)

def write_one():
    GPIO.output([B, C], GPIO.HIGH)
    GPIO.output([A, D, E, F, G, DP], GPIO.LOW)

def write_two():
    GPIO.output([A, B, G, E, D], GPIO.HIGH)
    GPIO.output([C, F, DP], GPIO.LOW)

def write_three():
    GPIO.output([A, B, C, D, G], GPIO.HIGH)
    GPIO.output([E, F, DP], GPIO.LOW)

def write_four():
    GPIO.output([B, C, F, G], GPIO.HIGH)
    GPIO.output([A, D, E, DP], GPIO.LOW)

def write_five():
    GPIO.output([A, C, D, F, G], GPIO.HIGH)
    GPIO.output([B, E, DP], GPIO.LOW)

def write_six():
    GPIO.output([A, C, D, E, F, G], GPIO.HIGH)
    GPIO.output([B, DP], GPIO.LOW)

def write_seven():
    GPIO.output([A, B, C], GPIO.HIGH)
    GPIO.output([D, E, F, G, DP], GPIO.LOW)

def write_eight():
    GPIO.output([A, B, C, D, E, F, G], GPIO.HIGH)
    GPIO.output(DP, GPIO.LOW)

def write_nine():
    GPIO.output([A, B, C, D, F, G], GPIO.HIGH)
    GPIO.output([E, DP], GPIO.LOW)

def write_clear():
    GPIO.output([A, B, C, D, E, F, G, DP], GPIO.LOW)


functions = [
        write_zero,
        write_one,
        write_two,
        write_three,
        write_four,
        write_five,
        write_six,
        write_seven,
        write_eight,
        write_nine
    ]
def write_digit(d):
    #assert d >= 0 and d <= 9
    functions[d]()

def clear():
    GPIO.output(SEGMENTS, GPIO.LOW)
    GPIO.output(DIGITS, GPIO.HIGH)

def display_all(four_digits, times):
    d1 = int(four_digits / 1000)
    d2 = int(four_digits / 100) % 10
    d3 = int(four_digits / 10) % 10
    d4 = int(four_digits) % 10
    for t in range(times):
        choose_digit(1)
        write_digit(d1)
        sleep(PERIOD)
        write_clear()
        choose_digit(2)
        write_digit(d2)
        sleep(PERIOD)
        write_clear()
        choose_digit(3)
        write_digit(d3)
        sleep(PERIOD)
        write_clear()
        choose_digit(4)
        write_digit(d4)
        sleep(PERIOD)
        write_clear()

def clock():
    c = GPIO.LOW
    times = int(1 / PERIOD / 8)
    clk = 0
    while True:
        if clk % 10 == 0:
            time = int(datetime.now().strftime("%H%M"))
        clk = (clk + 1) % 10
        display_all(time, times)
        if c == GPIO.LOW:
            c = GPIO.HIGH
        else:
            c = GPIO.LOW
        GPIO.output(COLON, c)

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    for pin in SEGMENTS:
        GPIO.setup(pin, GPIO.OUT, initial = GPIO.LOW)

    for pin in DIGITS:
        GPIO.setup(pin, GPIO.OUT, initial = GPIO.HIGH)

    GPIO.setup(COLON, GPIO.OUT, initial = GPIO.LOW)

    if (len(sys.argv) > 1 and sys.argv[1] == "debug"):
        display_all(int(sys.argv[1]), 60000)
    else:
        clock()

if __name__ == "__main__":
    main()
