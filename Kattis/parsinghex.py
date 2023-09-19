import sys,re
for x in re.findall("0x[\da-f]+","".join(sys.stdin.readlines()),re.I):
 print(x,int(x,16))