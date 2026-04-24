import sys

tape = [0] * 30000
ptr = 0

tape[ptr] += 33
print(chr(tape[ptr] % 256), end="")