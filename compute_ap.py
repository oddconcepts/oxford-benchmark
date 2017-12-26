#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Sangwhan Moon"
__copyright__ = "Copyright 2016-2017, Odd Concepts Inc."
__credits__ = ["Sangwhan Moon"]
__license__ = "MIT License"
__version__ = "0.1.0"
__maintainer__ = "Sangwhan Moon"
__email__ = "sangwhan@oddconcepts.kr"
__status__ = "Production"

import sys

from typing import List

def load_list(fname: str):
    """Plain text list loader. Reads from file separated by newlines, and returns a
    list of the file with whitespaces stripped.

    Args:
        fname (str): Name of file to be read.

    Returns:
        List[str]: A stripped list of strings, using newlines as a seperator from file.

    """

    return [e.strip() for e in open(fname, 'r').readlines()]

def compute_ap(pos: List[str], amb: List[str], ranked_list: List[str]):
    """Compute average precision against a retrieved list of images. There are some bits that
    could be improved in this, but is a line-to-line port of the original C++ benchmark code.

    Args:
        pos (List[str]): List of positive samples. This is normally a conjugation of
        the good and ok samples in the ground truth data.
        amb (List[str]): List of junk samples. This is normally the junk samples in
        the ground truth data. Omitting this makes no difference in the AP.
        ranked_list (List[str]): List of retrieved images from query to be evaluated.

    Returns:
        float: Average precision against ground truth - range from 0.0 (worst) to 1.0 (best).

    """

    intersect_size, old_recall, ap = 0.0, 0.0, 0.0
    old_precision, j = 1.0, 1.0

    for e in ranked_list:
        if e in amb:
            continue

        if e in pos:
            intersect_size += 1.0

        recall = intersect_size / len(pos)
        precision = intersect_size / j
        ap += (recall - old_recall) * ((old_precision + precision) / 2.0)

        old_recall = recall
        old_precision = precision
        j += 1.0

    return ap

def main():
    if len(sys.argv) != 3:
        print("Usage: ./compute_ap.py [GROUNDTRUTH QUERY] [RANKED LIST]")
        sys.exit(0)

    try:
        ranked_list = load_list(sys.argv[2])
        pos_set = list(set(load_list("%s_good.txt" % sys.argv[1]) + load_list("%s_ok.txt" % sys.argv[1])))
        junk_set = load_list("%s_junk.txt" % sys.argv[1])

        print(compute_ap(pos_set, junk_set, ranked_list))
    except IOError as e:
        print("IO error while opening files. %s" % e)
        sys.exit(1)


if __name__ == '__main__':
    main()