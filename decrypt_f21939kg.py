import argparse

def getScore(score):
    if score == "t":
        return 5
    elif score == "c":
        return 2
    else:
        return 3


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file_path', type=str, help='Path of input file')
    parser.add_argument('output_file_path', type=str,
                        help='Path of output file')

    args = parser.parse_args()

    inputFile = open(args.__dict__['input_file_path'], "r")
    input = inputFile.readline()

    encoding = input.split(":")
    decrypted_string = ""
    
    if encoding[0] == "Hex":
        decrypted_string = bytes.fromhex(encoding[1]).decode()
    # elif encoding[0] == "Caesar Cipher(+3)":
        # a = collections.deque(string.ascii_letters)
        # print(a)
    # out = open(args.__dict__['output_file_path'], "a")
    # out.write(decrypted_string)
    # out.close()
