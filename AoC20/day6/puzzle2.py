#!/usr/bin/python

with open('Input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
    count = 0
    answer_count = 0
    questions = {}
    for line in lines:
        if len(line) == 0:
            for v in questions.values():
                if v == answer_count:
                    count += 1
            answer_count = 0
            questions = {}
        else:
            answer_count += 1
            for c in line:
                if c in questions.keys():
                    questions[c] += 1
                else:
                    questions[c] = 1
    for v in questions.values():
        if v == answer_count:
            count += 1
    print count