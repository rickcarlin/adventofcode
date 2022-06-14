#!/usr/bin/env python3

import sys

class DiagInfo:
    def __init__(self, info_rec: str):
        self.cnt_ones = [0] * len(info_rec) # Initial an array/list with zero
        self.rec_cnt = 0
        self.process_record(info_rec)
        self.gamma = 0
        self.epsilon = 0

    def process_record(self, info_rec):
        self.rec_cnt += 1
        for i, c in enumerate(info_rec):
            self.cnt_ones[i] += int(c)
        
    def power_consumption(self):

        # Get the Gamma digits - 1 if cnt_ones > half of rec_cnt, else 0
        gamma_digits = list(map(lambda x: '1' if x > self.rec_cnt/2 else '0', self.cnt_ones))
        # Convert Gamma Digits to decimal number (join and then convert)
        self.gamma = int(''.join(gamma_digits), 2)

        #print(gamma_digits)
        #print(''.join(gamma_digits))
        print(f'Gamma: {self.gamma}')
        
        # Epsilon should be bit wise inverse of gamma
        epsilon_digits = list(map(lambda x: '1' if x == '0' else '0', gamma_digits))
        self.epsilon =  int(''.join(epsilon_digits), 2)
        
        #print( epsilon_digits)
        
        print(f'Epsilon: {self.epsilon}')
        print(f'Power Consumption: {self.epsilon * self.gamma}')
        
        
def main(argv): 

    # input file is supposed to be the first param - check that something was passed in
    if (len(argv) > 1):
        input_file = argv[1]
    else:
        print("ERROR: Missing input file")
        print("       Usage {} input-file-name\n".format(argv[0].split('/')[-1]))
        exit(1)

    # Open file and process line by line (better for large files)
    with open( input_file ) as f:

        # Read first line of file
        line = f.readline().strip()

        # Use first line to create a new Position object 
        diag_info = DiagInfo(line)

        # Process rest of the lines 
        for line in f: # Read a line
            #print(f'Line = {line}')
            diag_info.process_record(line.strip())

    f.close( )
    
    diag_info.power_consumption()


if __name__ == "__main__":
   main(sys.argv)