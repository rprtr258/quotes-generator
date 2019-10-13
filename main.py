#!/usr/bin/env python3
import sys

from ngram import NGram

WORDS_BAG_SIZE = 3


def train():
    model = NGram(WORDS_BAG_SIZE)
    model.train("dataset")
    for _ in range(50):
        print(model.generate())

def generate():
    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Specify what to do: 'train' or 'generate' quote")
        sys.exit(0)
    action = sys.argv[1]
    if not action in ["train", "generate"]:
        print("Unrecognized action")
        sys.exit(0)
    if action == "train":
        train()
    elif action == "generate":
        generate()
