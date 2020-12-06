#!/usr/bin/python

import re

def isValid(fields):
    if not ('byr' in fields and
        'iyr' in fields and
        'eyr' in fields and
        'hgt' in fields and
        'hcl' in fields and
        'ecl' in fields and
        'pid' in fields):
        return False
    
    p_data = dict(field.split(':', 1) for field in fields.split())

    for k, v in p_data.items():
        if k == 'byr':
            try:
                year = int(v)
                if (year < 1920 or year > 2002):
                    return False
            except:
                return False
        elif k == 'iyr':
            try:
                year = int(v)
                if (year < 2010 or year > 2020):
                    return False
            except:
                return False
        elif k == 'eyr':
            try:
                year = int(v)
                if (year < 2020 or year > 2030):
                    return False
            except:
                return False
        elif k == 'hgt':
            try:
                unit = v[-2:]
                if unit not in ['cm', 'in']:
                    return False
                min = 150
                max = 193
                if unit == 'in':
                    min = 59
                    max = 76

                value = int(v[:-2])
                if (value < min or value > max):
                    return False
            except:
                return False
        elif k == 'hcl':
            if not re.search("#[0-9a-f]{6}", v):
                return False
        elif k == 'ecl':
            if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        elif k == 'pid':
            if not re.search("^[0-9]{9}$", v):
                return False
        elif k == 'cid':
            pass
        else:
            return False

    return True

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
