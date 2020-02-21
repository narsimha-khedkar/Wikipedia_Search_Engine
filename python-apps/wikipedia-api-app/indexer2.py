
import sys
import re
from collections import defaultdict


def main(fh):
    print("Processing Index")
    results = defaultdict(set)

    for index, line in enumerate(fh, start=1):
        words = re.findall(r'\w+', line)
        for word in words:
            results[word].add(index)

    return results


if __name__ == '__main__':        
    try:
        inputFile, outputFile = "570.txt", "index.idx"
    except IndexError:
        print("File not found")
        exit(1)

    with open(inputFile) as input_file:
        index = main(input_file)

    with open(outputFile, 'w') as out_fh:
        for word in sorted(index):
            print(word + " " +  " ".join(str(i) for i in sorted(index[word])),
                  file=out_fh)