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

    #Read the lines of the csv file into a dictionary
    key_value_pairs = {}
    for line in lines:
        if len(line.strip()) != 0:
            key, value = line.split(' ')
            key_value_pairs[key.strip()] = value

    #make a list of the keys (number values) and order them from low to high
    nums = list(key_value_pairs.keys())
    nums = [int(x) for x in nums]
    nums.sort()
    #print(nums)

    #find the values that are on the edge a triangle up to the length of the file
    edge = []
    new_edge = 1
    i = 1
    code = ''
    #print('max' + str(max(nums)))
    #print('len' + str(len(nums)))
    while new_edge < int(max(nums)):
        new_edge = i*(i+1)//2
        if new_edge > int(max(nums)):
            raise Exception("Warning: Total number of items does not make a triangle!")
        edge.append(new_edge)
        #print(new_edge)
        code += key_value_pairs[str(nums[new_edge-1])]
        i += 1

    code = code.replace('\n', ' ').strip()
    #print(edge)
    print(code)
    return code


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    decode(msg_file)
