import custom_input
import json


def conversion_mnemonic_binary():
    data: dict = json.load(open("./data.json"))
    data_operations: dict = data.get("mnemonicToBinary")
    data_registers: dict = data.get("registers")

    data_received: list = input("Mnemonic to convert to binary: \n").split(" ")

    list_regs: list = []

    # Add elements inputted from the user to a list splitting by the spaces
    # and deleting the commas
    index: int = 0
    for element in data_received:
        data_received[index] = element.replace(",", "")

        # Add element to the list if it is a register
        if element[0] == "R":
            list_regs.append(data_received[index])

        index += 1

    # get the data of the command inputted by the user
    data_mnemonic: dict = data_operations.get(data_received[0])

    counter_regs: int = 0
    binary: str = ""

    # Convert the input to binary
    for element_to_print in data_mnemonic.get("dataInfo"):
        if element_to_print[0] == "code":
            binary += data_mnemonic.get("code")

        elif element_to_print[0] == "reg":
            binary += data_registers.get(list_regs[counter_regs])

            counter_regs += 1

        elif element_to_print[0] == "operation":
            binary += data_mnemonic.get("operation")

    print("binary: " + binary)

    # Convert the string binary to an integer in base 2 and print it in
    # hexadecimal
    print("hexadecimal: {:04X}".format(int(binary, 2)))


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
