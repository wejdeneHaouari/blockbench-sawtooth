#! /usr/bin/env python

import sys
import re


def main():
    if len(sys.argv) != 3 or sys.argv[1] == '-h':
        print("Usage: %s InputFileName OutputFileName" % sys.argv[0])
        print("Statistics (.cv file) for each workload " + \
              "will be written to the target file.")
        sys.exit(-1)

    path = sys.argv[1]
    target = 'results/' + sys.argv[2]

    with open(path) as file_in:
        with open(target, "a") as f, open("results/block.csv", "a") as b:
            f.write("time,txt_count,latency,outstanding\n")
            for line in file_in:
                block = re.search('polled block (.*) ', line)
                txt_count = re.search('tx count = (.+?) ', line)
                latency = re.search('latency = (.+?) ', line)
                outstanding_request = re.search('outstanding request = (.+?) ', line)
                time = re.search('time = (.*)', line)
                if latency and txt_count and outstanding_request and time:
                    txt_count_res = txt_count.group(1)
                    latency_res = latency.group(1)
                    outstanding_request_res = outstanding_request.group(1)
                    time_res = time.group(1)
                    f.write(time_res + "," + txt_count_res + "," + latency_res + "," + outstanding_request_res + "\n")
                if block:
                    block_res = block.group(1)
                    b.write(block_res + "\n")


if __name__ == '__main__':
    main()