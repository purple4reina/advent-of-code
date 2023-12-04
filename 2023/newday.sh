#!/bin/bash

num=$1
if [[ ! "$num" =~ ^[0-9]{2}$ ]]; then
    echo "Enter two digit number!  ex: ./newday.sh 03"
    exit 1
fi

dir="day${num}"
mkdir $dir

cp templates/* $dir
cd $dir

vim -p *
