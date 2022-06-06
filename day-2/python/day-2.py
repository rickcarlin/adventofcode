#!/usr/bin/env python3

import sys

class Position:
    def __init__(self):
        self.horizonatal = 0
        self.depth = 0

    def print_vals(self):
        print(f'Horizinal = {self.horizonatal}')
        print(f'Depth = {self.depth}')

    def process_command(self, command: str, delta: str):
        #print(f"Command {command}, Delta {delta}")
         
        if hasattr(self, command) and callable(cmd_method := getattr(self, command)):
            cmd_method(int(delta))
        else:
            print(f"Command {command} not found")

    def forward(self, delta: int):
        #print(f"In forward")
        self.horizonatal += delta

    def up(self, delta: int):
        #print(f"in up")
        self.depth -= delta

    def down(self, delta: int):
        #print(f"in down")
        self.depth += delta

    


def main(argv): 

    # input file is supposed to be the first param - check that something was passed in
    if (len(argv) > 1):
        input_file = argv[1]
    else:
        print("ERROR: Missing input file")
        print("       Usage {} input-file-name\n".format(argv[0].split('/')[-1]))
        exit(1)

    # Create a new Position object
    cur_position = Position()

    # Open file and process line by line (better for large files)
    with open( input_file ) as f:
        for line in f: # Read a line
            command, delta = ( line.strip().split() ) # Get the command and correspoinding change

            cur_position.process_command(command, delta)
            #print( f'Command {command} delta {delta}' )   
    f.close( )

    #print( "Number of Increases {}".format(cnt_increases) )

    cur_position.print_vals()



if __name__ == "__main__":
   main(sys.argv)