from custom_input import hex_input
from binary_to_SISA import *


def conversion_mnemonic_binary():
    data: dict = data_json.get()
    data_operations: dict = data.get("mnemonicToBinary")
    data_registers: dict = data.get("registers")

    data_received: list = input("SISA mnemonic to convert to binary: \n").split(
        " ")

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

    list_regs.append(list_regs[0])
    del list_regs[0]

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

        elif element_to_print[0] == "num":
            string_format: str = "{:0" + str(element_to_print[1]) + "b}"
            binary += string_format.format(int(
                data_received[len(data_received) - 1]))

    print("binary: " + binary)

    # Convert the string binary to an integer in base 2 and print it in
    # hexadecimal
    print("hexadecimal: {:04X}".format(int(binary, 2)))


def conversion_binary_mnemonic(binary: str = ""):
    if binary == "":
        binary: str = input("Binary to convert to SISA: \n")

    operation: str = binary[:4]

    switch_operations: dict = {
        "0000": type0,
        "0001": type0,
        "0010": type1,
        "0011": type1,
        "0100": type1,
        "0101": type1,
        "0110": type1,
        "1000": type2,
        "1001": type2,
        "1010": type2
    }

    switch_operations.get(operation)(binary)


def conversion_hexadecimal_mnemonic():
    hexadecimal: str = hex_input("Hexadecimal to convert to SISA: \n", 16)

    conversion_binary_mnemonic(hexadecimal)
