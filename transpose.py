import sys

infh=sys.argv[1]
outfh=sys.argv[2]

infile=open(infh, 'r')
outfile=open(outfh, 'w')

indict={}

for line in infile:
    if line=='': break
    line=line.strip()
    split=line.split('\t')
    for i in range(len(split)):
        if i in indict:
            indict[i].append(split[i])
        if i not in indict:
            indict[i]=[split[i]]

myindex=indict.keys()
for index in sorted(myindex):
    for j in indict[index]:
        outfile.write('\t'+str(j))
    outfile.write('\n')

infile.close()
outfile.close()
