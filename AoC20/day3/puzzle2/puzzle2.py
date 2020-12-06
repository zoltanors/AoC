#!/usr/bin/python

count1=0
count2=0
count3=0
count4=0
count5=0
col1=0
col2=0
col3=0
col4=0
col5=0
even=True

def calc_new_count(line, col, count):
    if line[col] == '#':
        return count+1
    return count

def adj_long_col(col, line_length):
    if col > line_length-2:
        return col-(line_length-1)
    return col
 

with open("Input.txt") as input:
    lines=input.readlines()
    for line in lines:
        count1=calc_new_count(line, col1, count1)
        col1+=1
        col1=adj_long_col(col1, len(line))
        count2=calc_new_count(line, col2, count2)
        col2+=3
        col2=adj_long_col(col2, len(line))
        count3=calc_new_count(line, col3, count3)
        col3+=5
        col3=adj_long_col(col3, len(line))
        count4=calc_new_count(line, col4, count4)
        col4+=7
        col4=adj_long_col(col4, len(line))
        if even:
            count5=calc_new_count(line, col5, count5)
            col5+=1
            col5=adj_long_col(col5, len(line))
        even=not even

print count1*count2*count3*count4*count5
