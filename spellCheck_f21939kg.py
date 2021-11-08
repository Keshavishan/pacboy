import argparse
from enum import Flag
import re

parser = argparse.ArgumentParser()
parser.add_argument('dictionary', type=str, help='Path of dictionary file')
parser.add_argument('input_file_path', type=str, help='Path of input file')
parser.add_argument('output_file_path', type=str,
                    help='Path of output file')

args = parser.parse_args()

inputFile = open(args.__dict__['input_file_path'], "r")
sentences = inputFile.readlines()
sentence = "".join(sentences)


nos = re.findall("\d", sentence)
punc = re.findall("[^a-zA-Z\d\s]", sentence)
upper = re.findall("[A-Z]", sentence)

sentence = re.sub("[^a-zA-Z\s]", "", sentence)
sentence = sentence.lower()
sentence = ' '.join(sentence.split())

dictionary = open(args.__dict__['dictionary'])
allWords = dictionary.readlines()
words = sentence.split(" ")

# print(words)

correct, incorrect = 0, 0
for word in words:
    if (word + "\n" or word) in allWords:
        correct = correct + 1
    else:
        incorrect = incorrect + 1
out = open(args.__dict__['output_file_path'], "a")
out.write(
    f'Formatting ###################\nNumber of upper case words transformed: {str(len(upper))}\nNumber of punctuation’s removed: {str(len(punc))}\nNumber of numbers removed: {str(len(nos))}\nSpellchecking ###################\nNumber of words in file: {str(len(words))}\nNumber of correct words in file: {str(correct)}\nNumber of incorrect words in file: {str(incorrect)}')
out.close()
