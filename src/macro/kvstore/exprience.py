#!/bin/python

import os
import subprocess
import time
import sys
from threading import Event
import signal

# running experiments
EXPS = [(1, 5), (1, 20), (1, 50)]
SC = "ycsb"
WAIT_TIME = 20
IS_INT = 0
WORKLOAD = "workloada.spec"

# Event object used to send signals from one thread to another
stop_event = Event()


def replaceTotalReq(oldTotal, newTotal):
    total = "recordcount=" + str(newTotal)

    with open("workloads/workloada.spec", 'r+') as f:
        contents = f.read().replace('recordcount=' + str(oldTotal), total)
        f.seek(0)
        f.truncate()
        f.write(contents)


def run_exp_change_total_req():
    cmd = './driver -db {} -threads {} -P workloads/{} -txrate {} -endpoint {} -wl {} -wt {} -isint {} 2>&1 | tee {}'

    start = time.time()
    i = 0
    oldTotal = 200
    for (t, r, q) in EXPS:
        print('********************** **********************')
        replaceTotalReq(oldTotal, q)
        begin_exp = time.time() - start
        OUTPUT_FILE = "logs/" + str(i) + str(t) + "_threads_" + str(r) + "_rates" + "_start" + str(begin_exp)

        print("start = ", begin_exp)
        print("rate = ", r)
        os.system(cmd.format(TARGET, t, WORKLOAD, r, ENDPOINT, SC, WAIT_TIME, IS_INT, OUTPUT_FILE))
        end_exp = time.time() - start
        print("end = ", end_exp)
        interval = end_exp - begin_exp
        if interval > 60:
            print("sleep ", (60 - interval))
            time.sleep(60 - interval)
        i += 1


def send_transactions(i, t, r, begin_exp):
    cmd = './driver -db {} -threads {} -P workloads/{} -txrate {} -endpoint {} -wl {} -wt {} -isint {}  | tee {}'
    OUTPUT_FILE = "logs/" + str(i) + "_" +  str(t) + "_threads_" + str(r) + "_rates" + "_start" + str(begin_exp)
    cmd_f = cmd.format(TARGET, t, WORKLOAD, r, ENDPOINT, SC, WAIT_TIME, IS_INT, OUTPUT_FILE)

    try:
        process = subprocess.Popen(cmd_f,
                       shell=True, preexec_fn=os.setsid)
        print('Running in process', process.pid)
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        print('Timed out - killing', process.pid)
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        time.sleep(1)
    print("Done")


class TimeoutException(Exception):  # Custom exception class
    pass


def timeout_handler(signum, frame):  # Custom signal handler
    raise TimeoutException


def saturation():
    start = time.time()
    i = 0
    for (t, r) in EXPS:
        print("********exp ************", i)
        begin_exp = time.time() - start
        i = i + 1
        send_transactions(i, t, r, begin_exp)


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
    saturation()
    print("done")



