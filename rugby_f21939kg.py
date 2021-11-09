import os
import argparse


def getScore(score):
    if score == "t":
        return 5
    elif score == "c":
        return 2
    else:
        return 3

def rugby(input_name, output_name):
    inputFile = open(input_name, "r")
    score = inputFile.readline()
    n = 3
    scores = [score[i:i+n] for i in range(0, len(score), n)]

    T1 = 0
    T2 = 0

    for s in scores:
        team = s[0:2]
        score = s[2]

        if team == "T1":
            T1 += getScore(score)
        else:
            T2 += getScore(score)

    if T1 > T2:
        print("T1 wins")
    elif T1 < T2:
        print("T2 wins")
    else:
        print("T1 drew with T2")

    out = open(output_name, "a")
    out.write(f'{str(T1)}:{str(T2)}')
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

    for file in input_files:
        basename = os.path.basename(file)
        print(basename)
        f = os.path.splitext(basename)
        
        rugby(file, os.path.join(outPath, f[0] + "_f21939kg" + f[1]))


   