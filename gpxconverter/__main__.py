#!/usr/bin/env python

import sys

from gpxconverter.converter import convert


def main():
    # //TODO: update argv parse to argparse
    convert(sys.argv[1:])


if __name__ == "__main__":
    sys.exit(main())
