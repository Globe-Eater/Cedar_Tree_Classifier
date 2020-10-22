#include <stdio.h>
#include <stdlib.h>

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"
#define STB_IMAGE_RESIZE_IMPLEMENTATION
#include "stb_image_resize.h"

int main() {

    int width, height, channels; 

    unsigned char *img = stbi_load("/Users/kellenbullock/Desktop/Labels.png", &width, &height, &channels, 1);
    if (img == NULL) {
        printf("Image has failed to load.\n");
        exit(1);
    } 
    printf("Loaded image with a width of %dpx, a height of %dpx and %d channels\n", width, height, channels);
    
    // Created a square sized image:
    size_t img_size = width * height * channels;
    size_t square_img_size = height * height * channels;      

    // allocating memory to save square_img:
    unsigned char *square_img = malloc(square_img_size);
    if(square_img == NULL) {
        printf("Unable to allocate memory for the square image.\n");
        exit(1);
    }

    // resize function:
    stbir_resize_uint8(img, width , height, 0, square_img, height, height, 0, channels);

    // iterate through old image. Write old image to new image.
    //for (unsigned char *p = img, *pn = square_img; pn != square_img + square_img_size; p++, pn++) {
    //    *pn = *p;
    //}
    
    stbi_write_jpg("/Users/kellenbullock/Desktop/Labels_2.png", height, height, channels, square_img, 100);

    stbi_image_free(square_img);    
    stbi_image_free(img);
    return 0;
}
