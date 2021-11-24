# Made by Raúl Gilabert on 19/11/2021

import data as data_json
from binary_and_decimal import binary_to_decimal, binary_to_decimal_unsigned


# All the arithmetic-logic and compare operations
def type0(input_data: str) -> None:
    data: dict = data_json.get()
    sisa_data: dict = data.get("binary_to_mnemonic").get(input_data[:4])
    regs_data: dict = data.get("registers_bin")

    sisa: str = sisa_data.get(input_data[13:]) + " " + regs_data.get(
        input_data[10:13]) + ", " + regs_data.get(input_data[4:7]) + \
        ", " + regs_data.get(input_data[7:10])

    print(sisa)


# ADDI
def ADDI(input_data: str) -> None:
    data: dict = data_json.get()
    sisa_data: str = data.get("binary_to_mnemonic").get(input_data[:4])
    regs_data: dict = data.get("registers_bin")

    sisa: str = sisa_data + " " + regs_data.get(input_data[7:10]) + ", " + \
        regs_data.get(input_data[4:7]) + ", " + binary_to_decimal(
        input_data[10:])

    print(sisa)


# Load from memory operations
def type1(input_data: str) -> None:
    data: dict = data_json.get()
    sisa_data: str = data.get("binary_to_mnemonic").get(input_data[:4])
    regs_data: dict = data.get("registers_bin")

    sisa: str = sisa_data + " " + regs_data.get(input_data[7:10]) + ", " + \
        binary_to_decimal(input_data[10:]) + "(" + regs_data.get(
        input_data[4:7]) + ")"

    print(sisa)


# Store on memory operations
def type2(input_data: str) -> None:
    data: dict = data_json.get()
    sisa_data: str = data.get("binary_to_mnemonic").get(input_data[:4])
    regs_data: dict = data.get("registers_bin")

    sisa: str = sisa_data + " " + binary_to_decimal(input_data[10:]) + "(" + \
        regs_data.get(input_data[4:7]) + ")" + ", " + regs_data.get(
        input_data[7:10])

    print(sisa)


# Branch zero and move operations
def type3(input_data: str) -> None:
    data: dict = data_json.get()
    sisa_data: dict = data.get("binary_to_mnemonic").get(input_data[:4])
    regs_data: dict = data.get("registers_bin")

    sisa: str = sisa_data.get(input_data[7]) + " " + regs_data.get(
        input_data[4:7]) + ", " + binary_to_decimal(input_data[8:])

    print(sisa)


# Input and output operations
def type4(input_data: str) -> None:
    data: dict = data_json.get()
    sisa_data: dict = data.get("binary_to_mnemonic").get(input_data[:4])
    regs_data: dict = data.get("registers_bin")

    sisa: str = sisa_data.get(input_data[7]) + " " + regs_data.get(
        input_data[4:7]) + ", " + binary_to_decimal_unsigned(input_data[8:])

    print(sisa)
