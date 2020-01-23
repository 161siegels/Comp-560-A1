def readFromFile(file_name):

    file = open(file_name, mode="r")
    inputs = {
        "colors": [],
        "states": [],
        "connections": [],
    }

    input_type = inputs.keys()
    type_iterator = iter(input_type)
    current = next(type_iterator)

    for line in file:

        if line.rstrip() == '':
            current = next(type_iterator)
            continue

        if current == "colors":
            inputs["colors"].append(line.rstrip())
        elif current == "states":
            inputs["states"].append(line.rstrip())
        else:
            inputs["connections"].append(line.rstrip())

    file.close()
    return inputs
