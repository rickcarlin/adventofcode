#!/usr/bin/env python3

import sys


def main(argv): 

    # input file is supposed to be the first param - check that something was passed in
    if ( len( argv ) > 1 ):
        input_file = argv[1]
    else:
        print( "ERROR: Missing input file" )
        print( "       Usage {} input-file-name\n".format(argv[0].split('/')[-1]) )
        exit(1)

    # Initializations
    cur_depth = sys.maxsize 
    cnt_increases = 0

    # Open file and process line by line (better for large files)
    with open( input_file ) as f:
        for line in f: # Read a line
            next_depth = int( line.strip() ) # Convert string to integer

            if ( next_depth > cur_depth ): # Check if increase
                cnt_increases += 1

            cur_depth = next_depth
        
    f.close( )

    print( "Number of Increases {}".format(cnt_increases) )





if __name__ == "__main__":
   main(sys.argv)