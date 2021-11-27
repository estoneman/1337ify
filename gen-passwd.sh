#!/bin/bash

if [ -z "$1" ] || [ "$#" -gt 1 ]
then
	echo "Usage: $0 <word-to-be-translated>"
	exit 1
fi

c/translate "$1" | openssl dgst -sha3-512 | cut -d ' ' -f 2 | tail -c 50 | head -c 12 | base64
