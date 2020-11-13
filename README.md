# cs50-projects
This repository holds random projects I did for Harvard University's CS50 course.

The default branch holds 2 projects (Filter and Recover) that I consider my best work in **this repository**. Other branches hold **entirely different projects** I also created and as such,
their file structures are different from the default branch. In essence, you cannot navigate directly to a branch from a subdirectory in another branch because the URLs will not match. **The other branches may or may not have their respective `README.md` files that tells what each branch is about as at the time you're reading this. They will be updated
in due time.**

##### Table of Contents for this branch

- [Filter](#filter)
- [Recover](#recover)

### Filter
[Filter](/Filter) is a program that applies filters to BMP images. It is built completely with C.

#### Project Description

This project implements 4 filters namely: grayscale, sepia, reflect and blur. You can think of filtering an image as taking the pixels of some original image, and modifying each pixel in such a way that a particular effect is apparent in the resulting image.

The main file where the filter functions (grayscale, sepia, reflect and blur) are implemented is [helpers.c](/Filter/helpers.c). [filter.c](/Filter/filter.c) describes the logic behind accepting command-line arguements, reading an image into memory, outputting the filtered image, among other things. The [images](/Filter/images) folder holds some sample images. [bmp.h](/Filter/bmp.h) defines some necessary data types needed for the program. [helpers.h](/Filter/helpers.h) just provides the function prototypes for the filter functions and [Makefile](/Filter/Makefile) tells the compiler how to compile this program. [Makefile](/Filter/Makefile) is necessary because this program uses multiple files to run correctly.

#### Usage

- Compile [Filter](/Filter) by ruuning:
```
$ make filter
```

- Then, you can run the program by running:
```
$  ./filter -g images/yard.bmp out.bmp
```
which takes the image at `images/yard.bmp`, and generates a new image called `out.bmp` after running the pixels through the grayscale function (represented by `-g`).
For the other filters, substitute in `-s`, `-r` or `-b` for sepia, reflect and blur respectively.




### Recover
[Recover](/Recover) is a program that recovers deleted JPEGs from a forensic image (a copy of a memory card). It is also built completely with C.

#### Project Description

The program itrates over a foresic image looking for JPEG signatures. Whenever a signiature is encountered, the JPEG file is outputted. [card.raw](/Recover/card.raw) is the forensic image (a copy of a memory card) that is to be iterated. [recover.c](/Recover/recover.c) is the main source code that handles command-line arguements and reading files into memory.

#### Usage

- Compile [Recover](/Recover) by ruuning:
```
$ make recover
```

- Then, you can run the program by running:
```
$  ./recover card.raw
```
where `card.raw` is any forensic image you wish to iterate over.








