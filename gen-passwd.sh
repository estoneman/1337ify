#!/bin/zsh

SEED="$1"
LEN_ARGS="$#"

# test if command line argument is invalid (exists and size)
#if [ -z "$SEED" ] || [ "$LEN_ARGS" -gt 1 ]
#then
#	echo "Usage: gen-passwd.sh <word-to-be-translated>"
#	exit 1
#fi

OUT=~/Programming/projects/fun/1337ify/build/translate

PASSWD=$($OUT "$SEED" | openssl dgst -sha3-512 | cut -d ' ' -f 2 | base64 | tail -c 50 | head -c 12 ; echo)
echo "Your new password: "$PASSWD
