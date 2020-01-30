def readFromFile(file_name: str) -> str:

    file = open(file_name, mode="r")
    inputs = {
        "colors": [],
        "states": [],
        "connections": [],
    }

    input_type = list(inputs.keys())
    type_iterator = iter(input_type)
    current = next(type_iterator)

    for line in file:

        if line.rstrip() == '':
            current = next(type_iterator)
            continue

        inputs[current].append(line.rstrip())

    file.close()
    return inputs
