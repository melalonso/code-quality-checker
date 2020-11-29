#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Code Quality Checker
Melvin Elizondo Perez
Universidad de Costa Rica
"""

import sys
import sqlite3
import logging
import argparse
import shutil
import tempfile
from pathlib import Path
import time

from tqdm import tqdm


def print_unique(info: int) -> None:
    pass


def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--out', type=Path,
                        help='Filename of the resultant database')
    parser.add_argument('--fix', choices=('dual', 'left', 'right'),
                        help='The strategy for fixing')
    parser.add_argument('--mistakes-list', type=Path)
    parser.add_argument('-n', '--mistakes', type=int,
                        help='Maximum number of mistakes to evaluate on')
    parser.add_argument('--models', type=Path, required=True,
                        help='Common prefix the path to forwards/backwards models')
    return parser


if __name__ == '__main__':
    # parser = init_parser()
    # args = parser.parse_args()
    print(" Code Quality Checker ".center(40, "-"))
    model = None
    my_sum = 0
    for i in tqdm(range(100000)):
        my_sum += i
        time.sleep(0.00005)
    print(my_sum)

