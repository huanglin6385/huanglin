import re
import time

name = "238. Product of Array Except Self"

with open("test.py","r") as p:
    code = p.readlines()

filename = "/a/Pycharm/project_leetcode/huanglin" + re.sub(r"[ .]","",name) +".py"
f = open(filename,"w")
f.writelines(code)
f.close()

print "code saved"+time.ctime()+name