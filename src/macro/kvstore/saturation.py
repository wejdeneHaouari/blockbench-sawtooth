#!/bin/python

import os
import time
import sys

# running experiments
EXPS = [(1, 5), (1, 10), (1,30)]
SC = "ycsb"
WAIT_TIME = 20
IS_INT = 0
OUTPUT_FILE = "output.txt"
WORKLOAD = "workloada.spec"

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
        print("interval = ", end_exp - begin_exp)


if __name__ == '__main__':

    if len(sys.argv) != 2 or sys.argv[1] == '-h':
        print("Usage: %s (-e or -s or -f)" % sys.argv[0])
        sys.exit(-1)

    target = sys.argv[1]
    if target == "-e":
        TARGET = "ethereum"
        ENDPOINT = "localhost:8545"
    elif target == "-f":
        TARGET = "fabric-v2.2"
        ENDPOINT = "localhost:8800,localhost:8801"
    elif target == "-s":
        TARGET = "sawtooth-v1.2"
        ENDPOINT = "localhost:9001,localhost:8000"
    else:
        print("argument must be -f -e or -s")
        sys.exit(-1)

    run_exp()
    print("done")