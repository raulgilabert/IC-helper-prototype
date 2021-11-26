def parse(data: str) -> tuple:
    data_received: list = data.split(" ")

    temp_data_received: list = []

    for element in data_received:
        for elem in element.split("("):
            temp_data_received.append(elem)

    data_received: list = temp_data_received

    temp_data_received: list = []

    for element in data_received:
        for elem in element.split(","):
            temp_data_received.append(elem)

    data_received: list = temp_data_received

    list_regs: list = []

    temp_data_received: list = []
    for element in data_received:
        if element != "":
            temp_data_received.append(element)

    data_received: list = temp_data_received

    # Add elements inputted from the user to a list splitting by the spaces
    # and deleting the commas
    index: int = 0
    for element in data_received:
        data_received[index] = element.replace(",", "")
        data_received[index] = data_received[index].replace(")", "")

        # Add element to the list if it is a register
        try:
            if element[0] == "R" or element == "-":
                list_regs.append(data_received[index])
        except:
            pass

        index += 1

    list_regs.append(list_regs[0])
    del list_regs[0]

    return data_received, list_regs
