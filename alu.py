# Made by Raúl Gilabert on 24/11/2021

import data as input_data


def mnemonic_to_alu() -> dict:
    data = input("SISA instruction: \n")

    # Convert input to a list of the elements inside it
    data_received: list = data.split(" ")

    counter_elements: int = 0
    for element in data_received:
        data_received[counter_elements] = element.replace(",", "")
        counter_elements += 1

    elements_data: dict = input_data.get().get("alu_to_binary").get(
        data_received[0])

    

    return elements_data