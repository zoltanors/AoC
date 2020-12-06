#!/usr/bin/python

def isValid(fields):
    return ('byr' in fields and
        'iyr' in fields and
        'eyr' in fields and
        'hgt' in fields and
        'hcl' in fields and
        'ecl' in fields and
        'pid' in fields)

with open('Input.txt') as input:
    lines = [line.rstrip() for line in input]
    count = 0
    fields = ''
    for line in lines:
        if len(line) == 0:
            if isValid(fields):
                count+=1
            fields = ''
        else:
            fields = fields + ' ' + line
    if isValid(fields):
        count+=1
    print count
