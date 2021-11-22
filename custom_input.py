# Made by Raúl Gilabert on 14/11/2021

# The user provides the message and a tuple of two integers, the way that the
# range of the first element and the second should have the inputted number
# inside or an empty tuple, returning the number without checking any range
def int_input(message: str, range_nums: tuple = ()) -> int:
    # Check if the input is an integer or not
    try:
        value_to_return: int = int(input(message))
    except ValueError:
        raise Exception("Input received is not a number")

    # Case of empty tuple
    if len(range_nums) == 0:
        return value_to_return
    # Case of tuple of one integer
    elif len(range_nums) == 1:
        raise Exception("Only one element in range. Expected two.")
    # Case of tuple of more than two integers
    elif len(range_nums) < 2:
        raise Exception("More than two elements in range. Expected two.")
    # Case of tuple of two elements
    else:
        # Some element is not an integer
        if type(range_nums[0]) != int or type(range_nums[1]) != int:
            raise Exception("Element of range is not an integer")
        else:
            # Range not valid because the init is grater than the end
            if range_nums[0] > range_nums[1]:
                raise ValueError("The first number of the range cannot be "
                                 "greater than the second")
            # Valid range
            elif range_nums[0] <= value_to_return <= range_nums[1]:
                return value_to_return
            else:
                raise Exception("Input not in range")


def hex_input(message: str, bits: int) -> str:
    # Check if the input is hexadecimal or not
    hex_data: str = input(message).upper()

    hex_digits: set = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A",
                       "B", "C", "D", "E", "F"}

    counter: int = 0

    for char in hex_data:
        counter += 1
        if char not in hex_digits:
            raise Exception("Input received is not a number")

    if counter != int(bits / 4):
        raise Exception("Input bits different that required")

    string_format: str = "{:0" + str(bits) + "b}"

    return string_format.format(int(hex_data, 16))
