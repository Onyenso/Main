##### Table of Contents for this branch

- [Caesar](#caesar)
- [Readability](#readability)

### Caesar
[Caesar](/caesar.c) is a program that encrypts messages using Caesar’s cipher. It is built completely with C.

#### Project Description

This project implements a message encryption. It accepts a user's key and a plaintext to that will be encrypted using the key.

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

<p>Next you'll be prompted for a `plaintext`:</p>

```
./caesar key
plaintext:  HELLO
```
And the result will be an encrypted version of your message, a `ciphertext`:

```
./caesar key
plaintext:  HELLO
ciphertext: URYYB
```



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
