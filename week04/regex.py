import re


def find_names(line):
    pattern = r"\w[\w\-'. ]*(?=[\n,]|)"
    result = re.findall(pattern,line)
    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_names(line)
    if (len(result)>0):
        print(result)