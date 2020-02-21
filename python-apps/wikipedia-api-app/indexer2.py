# /usr/bin/env python3
import sys
import re
from collections import defaultdict


def main(fh):
    results = defaultdict(set)

    for idx, line in enumerate(fh, start=1):
        words = re.findall(r'\w+', line)
        for word in words:
            results[word].add(idx)

    return results


if __name__ == '__main__':
    try:
        in_file, out_file = "570.txt", "index.idx"
    except IndexError:
        print("Usage:\n{} <in_file> <out_file>".format(sys.argv[0]),
              file=sys.stderr)
        exit(2)

    with open(in_file) as input_file:
        index = main(input_file)

    with open(out_file, 'w') as out_fh:
        for word in sorted(index):
            print(word + " " +  " ".join(str(i) for i in sorted(index[word])),
                  file=out_fh)