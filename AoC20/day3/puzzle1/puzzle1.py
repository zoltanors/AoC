#!/usr/bin/python

count=0
col=0

with open("Input.txt") as input:
    lines=input.readlines()
    for line in lines:
        if line[col] == '#':
            count+=1
        col+=3
        if col > len(line)-2:
            col-=len(line)-1

print count
