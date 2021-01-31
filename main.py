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


def deep_bugs_example():
    import os
    import json
    import numpy as np
    from keras.models import Sequential
    from keras.layers.core import Dense, Dropout

    # Loading the Data

    calls = []
    for file in os.listdir("DeepBugs_data/calls"):
        with open(os.path.join("DeepBugs_data/calls", file)) as fp:
            calls.extend(json.load(fp))

    print(f"Have read {len(calls)} function calls")
    print(calls[28000])
    print("-" * 100)

    with open("DeepBugs_data/token_to_vector.json") as fp:
        token_to_vector = json.load(fp)

    print(f"Have loaded {len(token_to_vector)} token embeddings.")
    print("-" * 100)

    # Preparing the Data

    xs = []  # Inputs given to the model: Each element is
    #   the vector representation of a function call.
    ys = []  # Outputs expected from the model: For each
    #   call, predict the probability that it's buggy.

    for call in calls:
        if (call["callee"] in token_to_vector and
                call["arguments"][0] in token_to_vector and
                call["arguments"][1] in token_to_vector):
            callee_vec = token_to_vector[call["callee"]]
            arg1_vec = token_to_vector[call["arguments"][0]]
            arg2_vec = token_to_vector[call["arguments"][1]]

            # Positive, i.e., correct example
            x_correct = callee_vec + arg1_vec + arg2_vec
            # Negative, i.e., buggy example
            x_buggy = callee_vec + arg2_vec + arg1_vec

            xs.append(x_correct)
            ys.append(0)  # Probability that buggy is 0
            xs.append(x_buggy)
            ys.append(1)  # Probability that buggy is 1

    # Split into training and validation data
    nb_training = int(0.9 * len(xs))
    xs_training = np.array(xs[:nb_training])
    ys_training = np.array(ys[:nb_training])
    xs_validation = np.array(xs[nb_training:])
    ys_validation = np.array(ys[nb_training:])

    print(f"{len(xs_training)} training examples")
    print(f"{len(xs_validation)} validation examples")

    # Training the Model

    x_length = len(xs[0])
    print("Tamaño de los vectores debería ser 200 * 3 = ", x_length)
    model = Sequential()
    model.add(Dropout(0.2, input_shape=(x_length,)))
    model.add(Dense(200, input_dim=x_length, activation="relu", kernel_initializer='normal'))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation="sigmoid", kernel_initializer='normal'))

    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    model.fit(xs_training, ys_training, batch_size=100, epochs=5, verbose=1)

    validation_stats = model.evaluate(xs_validation, ys_validation)
    print(f"Validation accuracy: {validation_stats[1]}")

    # Using the Learned Bug Detection Model
    # Function call: setTimeout(delay, fn)
    callee = "ID:setTimeout"  # Prefix "ID:" is to indicate that it's an identifier.
    arg1 = "ID:delay"
    arg2 = "ID:fn"

    x = token_to_vector[callee] + token_to_vector[arg1] + token_to_vector[arg2]
    xs = np.array([x])

    buggy_probabilities = model.predict(xs)
    print(f"Call is buggy with probability {str(round(buggy_probabilities[0][0], 4))}")


if __name__ == '__main__':
    # parser = init_parser()
    # args = parser.parse_args()
    print(" Code Quality Checker ".center(40, "-"))
    model = None

    deep_bugs_example()

    # my_sum = 0
    # for i in tqdm(range(100000)):
    #     my_sum += i
    #     time.sleep(0.00005)
    # print(my_sum)


