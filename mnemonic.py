# Made by Raúl Gilabert on 19/11/2021

from custom_input import hex_input
from binary_to_SISA import *
from binary_and_decimal import decimal_to_binary, decimal_to_binary_unsigned
from parse_data import parse


# Converts from SISA to binary
def conversion_mnemonic_binary():
    data: dict = data_json.get()
    data_operations: dict = data.get("mnemonicToBinary")
    data_registers: dict = data.get("registers")

    data_input: str = input("SISA mnemonic to convert to binary: \n").upper()

    print()

    data_received: list
    list_regs: list

    data_received, list_regs = parse(data_input)

    # get the data of the command inputted by the user
    data_mnemonic: dict = data_operations.get(data_received[0])

    counter_regs: int = 0
    binary: str = ""

    try:
        data_mnemonic.get("dataInfo")
    except AttributeError:
        print('Function "' + data_received[0] + '" does not exist')
        return

    # Convert the input to binary
    for element_to_print in data_mnemonic.get("dataInfo"):
        if element_to_print[0] == "code":
            binary += data_mnemonic.get("code")

            # Case of store operations where the register are in different
            # order compared with all the other operations
            if data_mnemonic.get("code") == "0100" or data_mnemonic.get(
                    "code") == "0110":
                counter_regs: int = 1

        elif element_to_print[0] == "reg":
            try:
                binary += data_registers.get(list_regs[counter_regs])
            except TypeError:
                print("Register not valid")

                return

            if data_mnemonic.get("code") == "0100" or data_mnemonic.get(
                    "code") == "0110":
                counter_regs -= 1

            else:
                counter_regs += 1

        elif element_to_print[0] == "operation":
            binary += data_mnemonic.get("operation")

        elif element_to_print[0] == "num":
            try:
                # Case of ADDI, move operations, branch zero, input and output
                if data_mnemonic.get("code") == "1010":
                    num: str = decimal_to_binary_unsigned(data_received[len(
                        data_received) - 1], element_to_print[1])

                else:
                    num: str = decimal_to_binary(data_received[len(
                        data_received) - 1], element_to_print[1])

                if num != "":
                    binary += num
                else:
                    return

            except ValueError:
                try:
                    # Load from memory operations
                    num: str = decimal_to_binary(data_received[len(
                        data_received) - 2], element_to_print[1])
                    if num != "":
                        binary += num
                    else:
                        return

                except ValueError:
                    try:
                        # Store on memory operations
                        num: str = decimal_to_binary(data_received[len(
                            data_received) - 3], element_to_print[1])
                        if num != "":
                            binary += num
                        else:
                            return

                    except ValueError:
                        print("Number not in base 10")

                        return

    print("binary: " + binary)

    # Convert the string binary to an integer in base 2 and print it in
    # hexadecimal
    print("hexadecimal: {:04X}".format(int(binary, 2)))


# Converts from binary to SISA
def conversion_binary_mnemonic(binary: str = ""):
    if binary == "":
        binary: str = input("Binary to convert to SISA: \n")

    print()

    operation: str = binary[:4]

    switch_operations: dict = {
        "0000": type0,
        "0001": type0,
        "0010": ADDI,
        "0011": type1,
        "0100": type2,
        "0101": type1,
        "0110": type2,
        "1000": type3,
        "1001": type3,
        "1010": type4
    }

    try:
        switch_operations.get(operation)(binary)
    except TypeError:
        print("Input not in data")

        return


# Converts from hexadecimal to SISA
def conversion_hexadecimal_mnemonic():
    try:
        hexadecimal: str = hex_input("Hexadecimal to convert to SISA: \n", 16)

    except Exception as ex:
        print()

        if hasattr(ex, "message"):
            print("Error: " + ex.message)
        else:
            print("Error: " + str(ex))

        return

    conversion_binary_mnemonic(hexadecimal)
