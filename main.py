import custom_input
import json
import pprint


def conversion_mnemonic_binary():
    data: dict = json.load(open("./data.json"))
    switch_operations: dict = data.get("mnemonicToBinary")
    switch_registers: dict = data.get("registers")

    data_received: list = input("Mnemonic to convert to binary: \n").split(" ")

    for element in data_received:
        element.replace(",", "")





def conversion_binary_mnemonic():
    print(2)


def error():
    print("Function not in index")


def main():
    switch: dict = {
        1: conversion_mnemonic_binary,
        2: conversion_binary_mnemonic
    }

    function: int = custom_input.int_input("Function: ")

    switch.get(function, error)()


if __name__ == "__main__":
    main()
