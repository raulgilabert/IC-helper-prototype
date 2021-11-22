# Made by Raúl Gilabert on 22/11/2021


def binary_to_decimal(binary: str) -> str:
    if binary[0] == "1":
        new_binary: str = ""
        for num in binary:
            if num == "1":
                new_binary += "0"
            else:
                new_binary += "1"

        new_binary: int = int(new_binary, 2)

        new_binary += 1

        decimal: int = 0 - new_binary
    else:
        decimal: str = str(int(binary, 2))

    return str(decimal)


def decimal_to_binary(decimal: str, bits: int) -> str:
    decimal: int = int(decimal)

    string_format: str = "{:0" + str(bits) + "b}"

    if decimal < 0:
        decimal_unsigned: int = 0 - decimal

        binary: str = string_format.format(decimal_unsigned)

        new_binary: str = ""
        for num in binary:
            if num == "1":
                new_binary += "0"
            else:
                new_binary += "1"

        new_binary: int = int(new_binary, 2)

        new_binary += 1

        new_binary: str = string_format.format(new_binary)

    else:
        new_binary: str = string_format.format(decimal)

    return new_binary


if __name__ == "__main__":
    print(binary_to_decimal(decimal_to_binary("-5", 4)))
