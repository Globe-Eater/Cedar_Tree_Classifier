#include <stdio.h>
#include <stdlib.h>

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

int main() {

    int width, height, channels; 

    unsigned char *trees = stbi_load("/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/raw_images/Z3S3.jpg", &width, &height, &channels, 3);
    if (trees == NULL) {
        printf("Image has failed to load.\n");
        exit(1);
    } 
    printf("Loaded image with a width of %dpx, a height of %dpx and %d channels\n", width, height, channels);
    
    // create a quarter section from trees
    size_t trees_size = width * height * channels;
    size_t small_trees_size = (width * 0.25) * (height * 0.25) * channels;
    printf("This is small_trees_size: %lu\n", small_trees_size);
    
    int small_width = width * 0.25 * channels;
    int small_height = height * 0.25 * channels;

    // allocating memory to save small_trees:
    unsigned char *small_trees = malloc(small_trees_size);
    if(small_trees == NULL) {
        printf("Unable to allocate memory for the smaller image.\n");
        exit(1);
    }

    // iterate through old image. Write old image quadrant to new image.
    for (unsigned char *p = trees, *pn = small_trees; pn != small_trees + small_trees_size; p += channels, pn += channels) {
        *pn = (*p);
    }
    
    stbi_write_jpg("/Users/kellenbullock/Desktop/small_trees.jpg", small_width, small_height, channels, small_trees, 100);

    stbi_image_free(small_trees);    
    stbi_image_free(trees);
    return 0;
}
