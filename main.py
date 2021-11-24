# Made by Raúl Gilabert on 14/11/2021

from custom_input import int_input
from mnemonic import *
from alu import *


def error():
    print("Function not in index")


def main():
    switch: dict = {
        1: conversion_mnemonic_binary,
        2: conversion_binary_mnemonic,
        3: conversion_hexadecimal_mnemonic,
#        4: mnemonic_to_alu,

        0: sys.exit
    }

    print("""
 ___   _____     _   _   _____   _       ____    _____   ____
|_ _| /  ___|   | | | | | ____| | |     |  _ \  | ____| |  _ \ 
 | |  | |       | |_| | |  _|   | |     | |_) | |  _|   | |_) |
 | |  | |___    |  _  | | |___  | |___  |  __/  | |___  |  _ <
|___| \_____|   |_| |_| |_____| |_____| |_|     |_____| |_| \_\ v1.0.2
    """)

    print()
    print("IMPORTANT: NUMERIC INPUT AND OUTPUT ARE ONLY ACCEPTED AND RETURNED "
          "IN BASE 10")
    print()

    function: int = 1

    # Main loop
    while function != "0":
        print("""
1 -> SISA to binary and hexadecimal to control unit
2 -> Binary to SISA
3 -> Hexadecimal to SISA

0 -> Exit

        """)

#        try:
        function: int = int_input("Function: ")

        print()

        switch.get(function, error)()

#        except Exception as ex:
#            print()
#
#            if hasattr(ex, "message"):
#                print("Error: " + ex.message)
#            else:
#                print("Error: " + str(ex))

        print()
        input("Press [Enter] to continue")
        print()
        print()


if __name__ == "__main__":
    main()