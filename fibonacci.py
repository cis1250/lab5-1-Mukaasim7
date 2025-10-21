#!/usr/bin/env python3
def get_user_input():
    while True:
        n = input("How many terms of the Fibonacci sequence do you want? ")
        if n.isdigit() and int(n) > 0:
            return int(n)
        else:
            print("Please enter a positive integer.")

def generate_fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def print_fibonacci(sequence):
    print("Fibonacci sequence:")
    print(" ".join(map(str, sequence)))


n = get_user_input()
fib_sequence = generate_fibonacci(n)
print_fibonacci(fib_sequence)
