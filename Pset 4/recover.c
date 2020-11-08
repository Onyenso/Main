#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");

    if (file == NULL)
    {
        printf("NULL file\n");
        return 1;
    }

    int counter = 0;
    int images_counter = 0;
    typedef uint8_t BYTE;
    BYTE buffer[512];
    //unsigned char bytes[512];
    FILE *new_file;
    char filename[8];


    while (fread(buffer, 512, 1, file) == 1)
    {
        // Check first four bytes
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] >= 0xe0 && buffer[3] <= 0xef))
        {
            if (images_counter > 0)
            {
                fclose(new_file);
                sprintf(filename, "%03i.jpg", images_counter);//
                images_counter++;//
                new_file = fopen(filename, "w");
                counter += 512;

                if (new_file == NULL)
                {
                    printf("Couldn't find valid memory location for new file");//
                    return 1;
                }
                fwrite(buffer, 512, 1, new_file);
            }

            if (images_counter == 0)
            {
                sprintf(filename, "%03i.jpg", images_counter);
                images_counter++;//
                new_file = fopen(filename, "w");
                if (new_file == NULL)
                {
                    printf("Couldn't find valid memory location for new file");//
                    return 1;
                }//
                fwrite(buffer, 512, 1, new_file);
            }
        }
        else if (images_counter > 0)
        {
            fwrite(buffer, 512, 1, new_file);
        }
    }
    fclose(new_file);//
    fclose(file);
    return 0;
}
