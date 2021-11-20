import sys
import data as data_json

data: dict = data_json.get()


def type0(input_data: str) -> None:
    print(input_data)

    SISA_data: dict = data.get("binary_to_mnemonic").get(input_data[:4])
    regs_data: dict = data.get("registers_bin")

    SISA: str = SISA_data.get(input_data[13:]) + " " + regs_data.get(
        input_data[10:13]) + ", " + regs_data.get(input_data[4:7]) + ", " \
            + regs_data.get(input_data[7:10])

    print(SISA)


def type1(input_data: str) -> None:
    SISA_data: dict = data.get("binary_to_mnemonic").get(input_data[:4])
    regs_data: dict = data.get("registers_bin")

    SISA: str = SISA_data + " " + regs_data.get(input_data[7:10]) + ", " + \
        regs_data.get(input_data[4:7]) + ", {:02X}".format(
            int(input_data[10:], 2))

    print(SISA)


def type2(input_data: str) -> None:
    SISA_data: dict = data.get("binary_to_mnemonic").get(input_data[:4])
    regs_data: dict = data.get("registers_bin")

    SISA: str = SISA_data.get(input_data[7]) + " " + regs_data.get(
        input_data[4:7]) + ", {:02X}".format(int(input_data[8:], 2))

    print(SISA)
