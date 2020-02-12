#!/usr/bin/env python
import argparse

from file_reader.base import read_file

if __name__ == '__main__':
    usage = ('Sum up numbers inside a file and the inner files')
    parser = argparse.ArgumentParser(usage)
    parser.add_argument('input_file',
                        help='input file with local paths and floats')
    args = parser.parse_args()
    stats = {}
    read_file(args.input_file, stats, [])
    for filename, stats in stats.items():
        print(f"{filename}\n"
              f"- count: {stats.sum_numbers}\n"
              f"- path: {stats.completed_path}\n"
              f"- total_acumulated: {stats.total_sum}\n"
              f"- errors ({len(stats.exceptions)}): {stats.exceptions}")
