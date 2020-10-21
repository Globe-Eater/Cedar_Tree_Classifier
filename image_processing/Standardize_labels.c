#include <stdio.h>
#include <stdlib.h>

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

int main() {

    int width, height, channels;

    unsigned char *trees = stbi_load("/Users/kellenbullock/Desktop/Natural_Resources_Project/datasets/Labels2.jpg", &width, &height, &channels, 3);
    if (trees == NULL) {
        printf("Image has failed to load.\n");
        exit(1);
    }
    printf("Loaded image with a width of %dpx, a height of %dpx and %d channels\n", width, height, channels);

    // Measuring trees size:
    size_t trees_size = width * height * channels;
    int gray_channels = channels == 4 ? 2 : 1;
    size_t gray_img_size = width * height * gray_channels;

    // allocating memory to save label data:
    unsigned char *labels = malloc(gray_img_size);
    if(labels == NULL) {
        printf("Unable to allocate memory for the newer image.\n");
        exit(1);
    }

    // iterate through old image. Replace values between 0 and 1 with 0. 
    for (unsigned char *p = trees, *pn = labels; p != trees + trees_size; p += channels, pn += gray_channels) {  
        //Convert to grayscale
        *pn = (uint8_t)((*p + *(p + 1) + *(p + 2))/3.0);
        if(channels == 4) {
            *(pn + 1) = *(p + 3);		      // OTHER? / alpha?
        }
        if (*p < 255) {                               // RED
           *pn = 0;
        }
        if (*(p+1) < 255) {                           // GREEN
           *(pn + 1) = 0;
        }
        if (*(p+2) < 255) {                           // BLUE
           *(pn + 2) = 0;
        }
        if (*(pn + 3) < 255) {
            *(pn + 3) = 0;
        }
    }

    stbi_write_png("/Users/kellenbullock/Desktop/Labels.png", width, height, gray_channels, labels, width * gray_channels);
    //stbi_write_jpg("/Users/kellenbullock/Desktop/Labels.jpg", width, height, channels, labels, 100);

    stbi_image_free(labels);
    stbi_image_free(trees);
    return 0;
}


