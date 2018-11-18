import os
import numpy as np
import pandas as pd

DATASET_DIR = '/data'


def main():
    # import dataset
    path = os.path.join(DATASET_DIR, 'xhamster.csv')
    xhamster_dataset = pd.read_csv(path, sep=",")
    print(xhamster_dataset.head)

if __name__ == "__main__":
    main()
