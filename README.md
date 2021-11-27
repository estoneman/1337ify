# 1337ify

## What is 1337ify?
1337ify is an ongoing project to generate a password given a seed. As of this version, it utilizes openssl's SHA3-512 digest. More support to come...

## How to run
Clone the repository
```bash
git clone https://github.com/estoneman/1337ify.git
```
### Compile - 
Compile source code according to your C compiler. I use gcc to compile, however you may replace with a compiler of your choosing
```bash
cd c
make
```
### Run - 

```bash
chmod +x gen-passwd.sh
./gen-passwd.sh <seed>
```

* seed is a string that you would like to obfuscate according to the service you are creating a password for
* e.g. GitHub --> seed = github

> Copyright Ethan Stoneman
