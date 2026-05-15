import sys

tape = [0] * 30000
ptr = 0

tape[ptr] += 8
while tape[ptr]:
    ptr += 1
    tape[ptr] += 4
    while tape[ptr]:
        ptr += 1
        tape[ptr] += 2
        ptr += 1
        tape[ptr] += 3
        ptr += 1
        tape[ptr] += 3
        ptr += 1
        tape[ptr] += 1
        ptr -= 4
        tape[ptr] -= 1
    ptr += 1
    tape[ptr] += 1
    ptr += 1
    tape[ptr] += 1
    ptr += 1
    tape[ptr] -= 1
    ptr += 2
    tape[ptr] += 1
    while tape[ptr]:
        ptr -= 1
    ptr -= 1
    tape[ptr] -= 1
ptr += 2
print(chr(tape[ptr] % 256), end="")
ptr += 1
tape[ptr] -= 3
print(chr(tape[ptr] % 256), end="")
tape[ptr] += 7
print(chr(tape[ptr] % 256), end="")
print(chr(tape[ptr] % 256), end="")
tape[ptr] += 3
print(chr(tape[ptr] % 256), end="")
ptr += 2
print(chr(tape[ptr] % 256), end="")
ptr -= 1
tape[ptr] -= 1
print(chr(tape[ptr] % 256), end="")
ptr -= 1
print(chr(tape[ptr] % 256), end="")
tape[ptr] += 3
print(chr(tape[ptr] % 256), end="")
tape[ptr] -= 6
print(chr(tape[ptr] % 256), end="")
tape[ptr] -= 8
print(chr(tape[ptr] % 256), end="")
ptr += 2
tape[ptr] += 1
print(chr(tape[ptr] % 256), end="")
ptr += 1
tape[ptr] += 2
print(chr(tape[ptr] % 256), end="")