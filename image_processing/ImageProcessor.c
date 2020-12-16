#include <stdio.h>
#include <stdlib.h>

int main() {
    
    FILE * pimage_read;
    long Sizel;
    char * buffer;
    size_t result;

    pimage_read = fopen("/Users/kellenbullock/Desktop/Natural_Resource_project/datasets/raw_images/Z3S3 copy.jpg", "r");
    if (pimage_read == NULL) {fputs ("File error",stderr); exit(1);}

    // obtain file size:
    fseek (pimage_read, 0, SEEK_END);
    Sizel = ftell (pimage_read);
    rewind (pimage_read);

    // allcate memory to buffer the file:
    buffer = (char*) malloc (sizeof(char)*Sizel);
    if (buffer == NULL) {fputs ("Memory Error",stderr); exit (2);}
    
    // copying file to the buffer:
    result = fread (buffer,1,Sizel,pimage_read);
    if (result != Sizel) {fputs ("Reading error",stderr); exit (3);}

    printf("Buffer is %d\n", *buffer);

    for (int i = 0; i < result; i++) {
        printf("Within buffer: %c\n", buffer[i]);
    }

    // terminate
    fclose (pimage_read);
    free (buffer);
    return 0;

}


