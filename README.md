##### Table of Contents for this branch

- [Caesar](#caesar)
- [Readability](#readability)

### Caesar
[Caesar](/caesar.c) is a program that encrypts messages using Caesar’s cipher. It is built completely with C.

#### Project Description

This project implements a message encryption. It accepts a user's key and a plaintext that will be encrypted using the key.

#### Usage

- Compile [Caesar](/caesar.c) by ruuning:
```
$ make caesar
```

- Then, you can run the program by running:
```
$  ./caesar key
```
where `key` is a non-negative integer with which to encrpyt your message.

- Next, you'll be prompted for a `plaintext`:

```
./caesar key
plaintext:  HELLO
```
- And the result will be an encrypted version of your message, a `ciphertext`:

```
./caesar key
plaintext:  HELLO
ciphertext: URYYB
```



### Readability
[Readability](/readability.c) is a program that computes the approximate grade level needed to comprehend some text. It is also built completely with C.

#### Project Description

The program uses the [Coleman-Liau index](https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index) to determine the grade for which a text is most appropriate. The
formula for the Coleman-Liau index is:
```
index = 0.0588 * L - 0.296 * S - 15.8
```
where, L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.

This program, readability, takes a text and determines its reading level.

#### Usage

- Compile [Readability](/readability.c) by ruuning:
```
$ make readability
```

- Then, you can run the program by running:
```
$  ./readabilty
```
- You will be promted for a text:
```
$ ./readability
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
```
- The appropriate grade for the text will be shown as such:
```
$ ./readability
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```




