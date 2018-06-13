import sys
import scipy
from scipy import stats

ktablefh=sys.argv[1]
newfh=sys.argv[2]

ktable=open(ktablefh, 'r')
newfile=open(newfh, 'w')

speardict={}

kdict={}

for line in ktable:
	if line=='': break
	line=line.strip()
	split=line.split()
	if line.startswith("lines"): continue
	kmer=split[0]
	if kmer not in kdict: kdict[kmer]=split[1:]

mykmers=kdict.keys()
for i in sorted(mykmers):
	if i not in speardict: speardict[i]={}
	for j in sorted(mykmers):
		myspear=scipy.stats.spearmanr(kdict[i], kdict[j])
		if j not in speardict[i]:speardict[i][j]=myspear

allks=speardict.keys()
for i in sorted(allks):
	newfile.write('\t'+str(i))
newfile.write('\n')
for i in sorted(allks):
	newfile.write(str(i))
	otherks=speardict[i].keys()
	for j in sorted(otherks):
		mycor=speardict[i][j][0]
		newfile.write('\t'+str(mycor))
	newfile.write('\n')

ktable.close()
newfile.close()