#!/usr/bin/env python3

import argparse

argparser = argparse.ArgumentParser(prog="no",
                                    description="Like yes but actually no")
argparser.add_argument("STRING", type=str, help="string to output", nargs='*', default='n')
args = argparser.parse_args()

no = args.STRING

print(*no)
