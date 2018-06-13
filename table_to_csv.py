import sys

infh=sys.argv[1]
newfh=sys.argv[2]

infile=open(infh, 'r')
newfile=open(newfh, 'w')

for line in infile:
	if line=='': break
	line=line.strip()
	split=line.split()
	if line.startswith("Mean") or line.startswith("Median") or line.startswith("SD"): continue
	newfile.write(str(split[0]))
	for i in range(1,len(split)):
		newfile.write(str(',')+str(split[i]))
	newfile.write('\n')

infile.close()
newfile.close()