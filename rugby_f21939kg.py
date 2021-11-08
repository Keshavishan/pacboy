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

    out = open(args.__dict__['output_file_path'], "a")
    out.write(f'{str(T1)}:{str(T2)}')
    out.close()
