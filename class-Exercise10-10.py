# Exercise - sorting and counting

import codecs
from operator import itemgetter

fp = codecs.open("courses3.txt")
fp.readline()
cis_list = []
for line in fp:
    line = line.strip()
    field = line.split()
    course = field[0]
    instructor = field[1]
    sem = field[2]
    coursedict = {}
    coursedict['course'] = course
    coursedict['instructor'] = instructor
    coursedict['sem'] = sem
    cis_list.append(coursedict)
    fp.close()

