#!/usr/bin/env python3
#-*-coding: utf-8 -*-
#pylint: disable=no-value-for-parameter

"""
realpath.py

click command:
    main()

"""

import os
import click

@click.command()
@click.argument('path', required=True)
def main(path):
    """
    get realpath of a directory/file
    """
    print(os.path.abspath(path))

if __name__ == "__main__":
    main()
