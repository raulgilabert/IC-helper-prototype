# Made by Raúl Gilabert on 22/11/2021


# Converts binary input in two's complement to a base 10 number
def binary_to_decimal(binary: str) -> str:
    if binary[0] == "1":
        # Inverts the number
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


def binary_to_decimal_unsigned(binary: str) -> str:
    decimal: str = str(int(binary, 2))

    return str(decimal)


# Converts base 10 number input to a binary in format two's complement
def decimal_to_binary(decimal: str, bits: int) -> str:
    decimal: int = int(decimal)

    string_format: str = "{:0" + str(bits) + "b}"

    if decimal < 0:
        decimal_unsigned: int = 0 - decimal

        if decimal_unsigned > pow(2, bits - 1):
            print("Number not in range")

            return ""

        binary: str = string_format.format(decimal_unsigned)

        # Inverts the number
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
        if decimal >= pow(2, bits - 1):
            print("Number not in range")

            return ""

        new_binary: str = string_format.format(decimal)

    return new_binary


def decimal_to_binary_unsigned(decimal: str, bits: int) -> str:
    decimal: int = int(decimal)

    string_format: str = "{:0" + str(bits) + "b}"

    if decimal >= pow(2, bits):
        print("Number not in range")

        return ""

    new_binary: str = string_format.format(decimal)

    return new_binary
