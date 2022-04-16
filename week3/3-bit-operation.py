key  = input("continue?")

if key == "y" or key == "Y":
    print()
else:
    print("Game over!")
    
key  = input("continue?") 

if not (key == "y" or key =="Y")
    print("Game over!")


"""
if you use & operator directly,
it is very different from the above examples

let's start from system architecture

Current computer architecture would store value as binary format

binary
1: 0b001
2: 0b010
3: 0b011
4: 0b100
5: 0b101

example 1:
x = 1
y = 2
z = x & y

z would be 1
"use & operator on variable" means do logical calcualtion bit by bit
0b01
0b11
----
0b01

bit 0: 1 & 1 -> 1
bit 1: 0 & 1 -> 0


example 2:
x = 1
y = 2
z = x | y

z would be 3
| is or operator
0b01
0b11
----
0b11


bit 0: 1 | 1 -> 1
bit 1: 0 | 1 -> 1
"""

x = 0b111110
y = 0b10001
print(bin(x))
print(bin(y))
print(x&y)


mask  = 0b11110000
value = 0b10101111
print(bin((mask & value)   4))