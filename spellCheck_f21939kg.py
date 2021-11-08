import argparse
from enum import Flag
import re

def getScore(score):
    if score == "t":
        return 5
    elif score == "c":
        return 2
    else:
        return 3


if __name__ == '__main__':
    word = "123"

    parser = argparse.ArgumentParser()
    parser.add_argument('dictionary', type=str, help='Path of dictionary file')
    parser.add_argument('input_file_path', type=str, help='Path of input file')
    parser.add_argument('output_file_path', type=str, help='Path of output file')

    args = parser.parse_args()

    inputFile = open(args.__dict__['input_file_path'], "r")
    sentences = inputFile.readlines()
    sentence = "".join(sentences)
    numbers = 0
    punc = 0
    uppercase = 0

    nos = re.findall("\d", sentence)
    punc = re.findall("[^a-zA-Z\d\s]", sentence)
    upper = []

    # sentence = re.sub("\d", "", sentence)
    # out = open(args.__dict__['output_file_path'], "a")
    # out.write(f'{str(T1)}:{str(T2)}')
    # out.close()
