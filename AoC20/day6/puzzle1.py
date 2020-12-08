#!/usr/bin/python

with open('Input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
    count = 0
    questions = set()
    for line in lines:
        if len(line) == 0:
            count += len(questions)
            questions = set()
        else:
            for c in line:
                questions.add(c)
    count += len(questions)
    print count