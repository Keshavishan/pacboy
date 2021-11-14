import os
import argparse
import re

def spellchecker(dictionary, input_name, output_name):
    inputFile = open(input_name, "r")
    sentences = inputFile.readlines()
    sentence = "".join(sentences)

    all_punc = "[.?!,:;\-\(\)\[\]\{\}'\"]"

    ellipsis = re.findall("\.{3}", sentence)
    sentence = re.sub("\.{3}", "", sentence)

    nos = re.findall("\d", sentence)
    punc = re.findall(all_punc, sentence)
    upper = re.findall("[A-Z]", sentence)

    sentence = re.sub("[.?!,:;\-\(\)\[\]\{\}'\"\d]", "", sentence)
    sentence = sentence.lower()
    sentence = ' '.join(sentence.split())

    dictionary = open(dictionary)
    allWords = dictionary.readlines()
    words = sentence.split(" ")

    correct, incorrect = 0, 0
    for word in words:
        if (word + "\n" or word) in allWords:
            correct = correct + 1
        else:
            incorrect = incorrect + 1
        
    out = open(output_name, "a")
    out.write(
        f'f21939kg\nFormatting ###################\nNumber of upper case letters changed: {str(len(upper))}\nNumber of punctuations removed: {str(len(punc) + len(ellipsis))}\nNumber of numbers removed: {str(len(nos))}\nSpellchecking ###################\nNumber of words: {str(len(words))}\nNumber of correct words: {str(correct)}\nNumber of incorrect words: {str(incorrect)}')
    out.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dictionary', type=str, help='Path of dictionary folder')
    parser.add_argument('input_folder', type=str, help='Path of input folder')
    parser.add_argument('output_folder', type=str,
                        help='Path of output folder')

    args = parser.parse_args()

    dictionary = args.__dict__['dictionary']
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
        
        spellchecker(dictionary, file, os.path.join(outPath, f[0] + "_f21939kg" + f[1]))

