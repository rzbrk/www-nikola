#!/usr/bin/env python3

import argparse
import re

# Main routine
def main(args):
    fh = open(args.linkfile, "r")
    for line in fh:
        regexp=".*Remote link moved PERMANENTLY to \"([\S]+)\" and should be updated in ([\S]+): ([\S]+) \[HTTP: 301\]$"
        match_obj = re.match(regexp, line)
        if match_obj:
            art_file = match_obj.groups()[1]
            link_old = match_obj.groups()[2]
            link_new = match_obj.groups()[0]

            print(art_file, link_old, link_new)

###############################################################################
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("linkfile", help="output from nikola check -l -r")
    args = parser.parse_args()
    main(args)
