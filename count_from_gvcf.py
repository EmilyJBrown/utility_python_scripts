## takes a gzip gvcf file, outputs the number of genotyped sites

import sys
import gzip

infh=sys.argv[1]
infile=gzip.open(infh, 'r')

count=0

for line in infile:
	if line=='': break
	if line.startswith("#"): continue
	if count%1000000==0: print count
	line=line.strip()
	split=line.split()
	ref=split[3]
	if ref=="N": continue
	if split[7].startswith("END"):
		pos1=int(split[1])
		pos2=int(split[7].split("=")[1])
		for i in range(pos1, pos2): count+=1
	if split[7]==".": count+=1
	if split[10].startswith("0"):
		print "Found one!"
		print line

print "Final count of number of sites:"
print count
infile.close()