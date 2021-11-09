import os
import argparse


def decrypt(input_name, output_name):
    inputFile = open(input_name, "r")
    input = inputFile.readline()

    encoding = input.split(":")
    decrypted_string = ""

    if encoding[0] == "Hex":
        decrypted_string = bytes.fromhex(encoding[1]).decode()
    elif encoding[0] == "Caesar Cipher(+3)":
        for c in encoding[1]:
            if c.isalpha():
                n = ord(c) - ord('a')
                x = (n - 3) % 26
                dec_char = chr(x + ord('a'))
                decrypted_string += dec_char
            else:
                decrypted_string += c
    else:
        dict = {
            '.-': 'a',
            '-...': 'b',
            '-.-.': 'c',
            '-..': 'd',
            '.': 'e',
            '..-.': 'f',
            '--.': 'g',
            '....': 'h',
            '..': 'i',
            '.---': 'j',
            '-.-': 'k',
            '.-..': 'l',
            '--': 'm',
            '-.': 'n',
            '---': 'o',
            '.--.': 'p',
            '--.-': 'q',
            '.-.': 'r',
            '...': 's',
            '-': 't',
            '..-': 'u',
            '...-': 'v',
            '.--': 'w',
            '-..-': 'x',
            '-.--': 'y',
            '--..': 'z',
            '.-.-.-': '.',
            '..--..': '?',
            '--..--': ',',
            '/': ' ',
            '-.-.--': '!',
            '---...': ':',
            '_._._.': ';',
            '_...._': '-',
            '-.--.': '(',
            '-.--.-': ')',
            '.-..-.': '"',
            '.----.': "'",
            '-----': '0',
            '.----': '1',
            '..---': '2',
            '...--': '3',
            '....-': '4',
            '.....': '5',
            '-....': '6',
            '--...': '7',
            '---..': '8',
            '----.': '9'
        }

        for c in encoding[1].split(" "):
            if c in dict:
                decrypted_string += dict[c]

    out = open(output_name, "a")
    out.write(decrypted_string.lower())
    out.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_folder', type=str, help='Path of input folder')
    parser.add_argument('output_folder', type=str,
                        help='Path of output folder')

    args = parser.parse_args()

    inputPath = args.__dict__['input_folder']
    outPath = args.__dict__['output_folder']

    input_files = []

    for entry in os.listdir(inputPath):
        if os.path.isfile(os.path.join(inputPath, entry)):
            input_files.append(os.path.join(inputPath, entry))

    if not os.path.exists(outPath):
            os.makedirs(outPath)
            
    for file in input_files:
        basename = os.path.basename(file)
        f = os.path.splitext(basename)
        
        decrypt(file, os.path.join(outPath, f[0] + "_f21939kg" + f[1]))