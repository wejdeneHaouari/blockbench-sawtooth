#!/bin/python

import os
import time
import sys

# running experiments
EXPS = [(1, 20), (1, 100), (1, 50), (1, 300)]
TARGET_eth = "ethereum"
TARGET = "sawtooth-v1.2"
WORKLOAD = "workloada.spec"
ENDPOINT_eth = "localhost:8545"
ENDPOINT = "localhost:9001,localhost:8000"
SC = "ycsb"
WAIT_TIME = 20
IS_INT = 0
OUTPUT_FILE = "output.txt"


def run_exp():
    cmd = './driver -db {} -threads {} -P workloads/{} -txrate {} -endpoint {} -wl {} -wt {} -isint {} 2>&1 | tee {}'


    start = time.time()
    for (t, r) in EXPS:
        print('********************** **********************')
        begin_exp = time.time() - start
        print("start = ", begin_exp)
        print("rate =", r)
        os.system(cmd.format(TARGET, t, WORKLOAD, r, ENDPOINT, SC, WAIT_TIME, IS_INT, OUTPUT_FILE))
        end_exp = time.time() - start
        print("end = ", end_exp)
        print("interval = ", end_exp - begin_exp )
        





if __name__ == '__main__':
   start = time.time()
   run_exp()
   interval = time.time() - start
   print(2000/interval)
   print(interval)
   print("done")

