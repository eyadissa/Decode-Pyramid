def decode(msg_file):
    # Read the CSV file
    try:
        with open(msg_file, 'r') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        print("Unicode Decode Error")
    except FileNotFoundError:
        print("File Not Found")

    print(f'Decoding, {msg_file}')

    key_value_pairs = {}

    for line in lines:
        if len(line.strip()) != 0:
            key, value = line.split(' ')
            key_value_pairs[key.strip()] = value

    nums = list(key_value_pairs.keys())
    nums = [int(x) for x in nums]
    nums.sort()
    print(key_value_pairs['3'])
    print(nums)


    #make a list of indicies of the edge of a triangle up to the length of the file
    edge = []
    new_edge = 1
    i = 1
    code = ''
    print('max' + str(max(nums)))
    while new_edge < int(max(nums)):
        new_edge = i*(i+1)//2
        if new_edge > int(max(nums)):
            raise Exception("Warning: Total number of items does not make a triangle!")
        edge.append(new_edge)
        code += key_value_pairs[str(new_edge)]
        i += 1
        print(new_edge)

    code = code.replace('\n', ' ').strip()
    print(edge)
    print(code)
    return code


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    decode(msg_file)
