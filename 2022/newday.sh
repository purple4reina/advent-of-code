#!/bin/bash

echo -n "Enter day number: "
read num

[[ "$num" =~ ^[0-9]{2}$ ]] || (echo "  Must enter two digit number!" && exit 1)

dir="day${num}"
mkdir $dir

cp templates/* $dir
cd $dir

vim -p *
