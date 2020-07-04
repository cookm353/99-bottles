#!/usr/bin/env python3


def sing(num_bottles):
    while num_bottles:
        print(f"{num_bottles} bottles of beer on the wall,")
        print(f"{num_bottles} bottles of beer on the wall,")
        print("Take one down, pass it around,")
        print(f"{num_bottles} bottles of beer on the wall.\n")
        num_bottles = take_one_down(num_bottles)


def take_one_down(num_bottles):
    num_bottles = num_bottles - 1
    return num_bottles


def __main__():
    num_bottles = 99
    sing(num_bottles)


if __name__ == "__main__":
    __main__()
