# -*- coding: UTF-8 -*-

import sys
import os

os.chdir(sys.path[0])  

def doImageMagick():
    os.system('find . -iname "*.png" -exec echo {} \; -exec convert {} {} \;')


def main():
    doImageMagick()

if __name__ == '__main__':
    main()

