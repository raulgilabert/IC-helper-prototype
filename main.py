# Made by Raúl Gilabert on 14/11/2021

from custom_input import int_input
from mnemonic import *


def error():
    print("Function not in index")


def main():
    switch: dict = {
        1: conversion_mnemonic_binary,
        2: conversion_binary_mnemonic,
        3: conversion_hexadecimal_mnemonic,
    }

    print("""
 ___   _____     _   _   _____   _       ____    _____   ____
|_ _| /  ___|   | | | | | ____| | |     |  _ \  | ____| |  _ \ 
 | |  | |       | |_| | |  _|   | |     | |_) | |  _|   | |_) |
 | |  | |___    |  _  | | |___  | |___  |  __/  | |___  |  _ <
|___| \_____|   |_| |_| |_____| |_____| |_|     |_____| |_| \_\ v0.2.0
    """)

    print("""
1 -> SISA to binary and hexadecimal
2 -> Binary to SISA
3 -> Hexadecimal to SISA
    """)

    function: int = int_input("Function: ")

    switch.get(function, error)()


if __name__ == "__main__":
    main()
