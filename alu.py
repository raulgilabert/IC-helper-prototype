# Made by Raúl Gilabert on 24/11/2021

import data as input_data
from parse_data import parse
from tabulate import tabulate
from binary_and_decimal import *
from custom_input import int_input


def mnemonic_to_alu() -> dict:
    data = input("SISA instruction: \n").upper()

    regs_bin: dict = input_data.get().get("registers_alu")

    # Convert input to a list of the elements inside it
    data_received, regs_data = parse(data)

    elements_data: dict = input_data.get().get("alu_to_binary").get(
        data_received[0])

    regs_to_write: list = []

    if data_received[0] == "MOVHI":
        regs_data *= 2

    if elements_data.get("a_address") == "???":
        regs_to_write.append("a_address")

    if elements_data.get("b_address") == "???":
        regs_to_write.append("b_address")

    if elements_data.get("d_address") == "???":
        regs_to_write.append("d_address")

    if elements_data.get("addr_io") == "????????":
        try:
            # Case of ADDI, move operations, branch zero, input and output
            if data_received[0] == "LD" or data_received[0] == "LDB" or \
                    data_received[0] == "ST" or data_received[0] == "STB":
                num: str = decimal_to_binary_unsigned(data_received[len(
                    data_received) - 1], 8)

            else:
                if (data_received[0] == "IN" or data_received[0] == "OUT") \
                        and len(data_received) == 2:
                    num: str = "XXXXXXXX"

                elif data_received[0] == "IN" or data_received[0] == "OUT":
                    num: str = decimal_to_binary_unsigned(
                        data_received[len(data_received) - 1], 8)

                else:
                    num: str = decimal_to_binary(
                        data_received[len(data_received) - 1], 8)

        except ValueError:
            try:
                if (data_received[0] == "IN" or data_received[0] == "OUT") \
                        and len(data_received) == 2:
                    num: str = "XXXXXXXX"

                elif data_received[0] == "IN" or data_received[0] == "OUT":
                    num: str = decimal_to_binary_unsigned(
                        data_received[len(data_received) - 2], 8)

                else:
                    num: str = decimal_to_binary(
                        data_received[len(data_received) - 2], 8)

            except ValueError:
                try:
                    if (data_received[0] == "IN" or data_received[0] == "OUT") \
                            and len(data_received) == 2:
                        num: str = "XXXXXXXX"

                    elif data_received[0] == "IN" or data_received[0] == "OUT":

                        num: str = decimal_to_binary_unsigned(
                            data_received[len(data_received) - 2], 8)

                    else:
                        num: str = decimal_to_binary(
                            data_received[len(data_received) - 3], 8)

                except ValueError:
                    print("Number not in base 10")

                    return

        elements_data["addr_io"] = num

    if elements_data.get("n") == "????????????????":
        try:
            # Case of ADDI, move operations, branch zero, input and output
            if data_received[0] == "LD" or data_received[0] == "LDB" or \
                    data_received[0] == "ST" or data_received[0] == "STB":
                num: str = decimal_to_binary_unsigned(data_received[len(
                    data_received) - 1], 16)

            else:
                num: str = decimal_to_binary(data_received[len(data_received)
                                                           - 1], 16)

        except ValueError:
            try:
                # Load from memory operations
                num: str = decimal_to_binary(data_received[len(data_received)
                                                           - 2], 16)

            except ValueError:
                try:
                    # Store on memory operations
                    num: str = decimal_to_binary(data_received[len(
                        data_received) - 3], 16)

                except ValueError:
                    print("Number not in base 10")

                    return

        if data_received[0] == "BZ" or data_received[0] == "BNZ":
            value_register: int = int_input("Value of the register: ")

            if value_register == 0 and data_received[0] == "BNZ":
                elements_data["tknbr"] = 0
            elif value_register == 1 and data_received[0] == "BZ":
                elements_data["tknbr"] = 0

        elements_data["n"] = num

    if data_received[0] == "ST" or data_received[0] == "STB":
        regs_data[0], regs_data[1] = regs_data[1], regs_data[0]

    for i in range(0, len(regs_data)):
        elements_data[regs_to_write[i]] = regs_bin.get(regs_data[i])

    list_headers: list = []
    list_content: list = []

    for element in elements_data:
        list_headers.append(element)
        list_content.append(elements_data[element])

    print()
    print("IMPORTANT: ila IS OF ONLY ONE BIT IF THE OPERATION IS FROM AN UC AND"
          "NOT FROM AN UCG. IN THAT CASE 00 IS 0 AND 10 IS 1")
    print()

    print(tabulate([list_content], headers=list_headers))

    return elements_data
