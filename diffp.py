#!/usr/bin/env python
# coding=utf-8
import sys
import codecs
import sys

HEADER = '_-_header_-_'

def merge_diffs():
    patches = {}
    patch_name = HEADER
    with codecs.open(sys.argv[1], "r", "utf-8") as f:
        for line in f:
            if line.startswith('diff '):
                patch_name = line.split(' ')[-1]
            if patch_name not in patches:
                patches[patch_name] = u''
            if patch_name == HEADER:
                patches[patch_name] += line
            elif line.startswith('#'):
                patches[patch_name] += line

    if HEADER in patches:
        p(patches[HEADER])
    with codecs.open(sys.argv[2], "r", "utf-8") as f:
        for line in f:
            p(line)
            if line.startswith('diff '):
                patch_name = line.split(' ')[-1]
                if patch_name in patches:
                    p(patches[patch_name])
                    del patches[patch_name]
                    

if __name__ == '__main__':
    # Wrap sys.stdout with a writer that knows how to handle encoding
    # Unicode data.
    wrapped_stdout = codecs.getwriter('UTF-8')(sys.stdout)
    sys.stdout = wrapped_stdout
    p = sys.stdout.write
    merge_diffs()
