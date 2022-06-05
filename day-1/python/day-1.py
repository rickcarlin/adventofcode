#!/usr/bin/env python3

import sys


def main(argv): 

    # input file is supposed to be the first param - check that something was passed in
    if ( len( argv ) > 1 ):
        input_file = argv[1]
    else:
        print( "ERROR: Missing input file" )
        print( "       Usage {} input-file-name\n".format(argv[0].split('/')[-1]) )
  


if __name__ == "__main__":
   main(sys.argv) 