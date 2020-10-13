#include <stdint.h>

#define STB_IMAGE_WRITE_IMPLEMENTATION
#define STB_IMAGE_RESIZE_IMPLEMENTATION
#define STB_IMAGE_IMPLEMENTATION

#include "stb_image_write.h"
#include "stb_image_resize.h"
#include "stb_image.h"

#define CHANNEL_NUM 3

int main() {
    int width, height, bpp;
    int outw, outh = 800;

    uint8_t* trees_big = stbi_load("Z3S3 copy.jpeg", &width, &height, &bpp, 3);    
    uint8_t* trees_small;

    printf("The trees_big width is: %d\n", width);
    printf("The trees_big height is: %d\n", height);

    // attempting to resize Z3S3 copy.jpeg...
    stbir_resize_uint8(      trees_big , width , height , 0,
                               trees_small, outw, outh, 0, CHANNEL_NUM);

    printf("Trees_small width is: %d\n", outw);
    printf("Trees_small height is: %d\n", outh);

    //stbi_write_jpg("trees_small.jpeg", outw, outh, CHANNEL_NUM, trees_small, width*CHANNEL_NUM);

    stbi_image_free(trees_big);
    stbi_image_free(trees_small);

    return 0;
}
