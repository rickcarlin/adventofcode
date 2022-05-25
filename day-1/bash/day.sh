#!/usr/bin/bash

printf "AdventOfCode 2021 - Day 1\n"

if [[ -z ${1} ]];
then
    printf "ERROR: Missing input file\n"
    printf "       Usage %s input-file-name\n" `basename ${0}`
    exit
else
    infile=$1
fi 

# get first value
read -r depth < $infile

cnt_increases=0

# Loop thru values in the file
# Note: will read the first line again, 
# but since we are only trying to get the number of increases this won't
# affect the computation (this is quicker than trying to pipe it from tail)
while read -r nextdepth ; 
do 
    if (( $depth < nextdepth ]]
    depth=nextdepth
done < $infile

