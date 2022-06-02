#include <stdio.h>
#include <stdlib.h>
#include <libgen.h>


int main( int argc, char *argv[] ) {

    FILE *f;
    int cur_depth, next_depth;
    int cnt_increases = 0;

    // Assumes first cmdline param will be input filename. If not passed, print usage and exit
    if (argc < 2) {
        printf("ERROR: Missing input file\n");
        printf("       Usage %s input-file-name\n", basename(argv[0]));

        exit(EXIT_FAILURE);
    }

    // Open the file for reading
    if ((f = fopen(argv[1], "r")) == NULL) {
        printf( "ERROR: failed to open %s\n", argv[1]) ;
        exit(EXIT_FAILURE);
    }
    
    // Read the first depth;
    fscanf(f, "%d", &cur_depth);

    // Loop thru rest
    while (fscanf(f, "%d", &next_depth) != EOF) {
        if (cur_depth < next_depth) // Check if we increased
            cnt_increases++;
        cur_depth = next_depth ;
    }

    // cleanup 
    fclose(f);

    // Print the result
    printf( "Number of increases %d\n", cnt_increases) ;

}