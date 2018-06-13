#takes a file with a list of bam alignments and write a new file with the file name and the number of unique mapping reads in that file
#be sure to run from the directory with the bam files


import sys
import subprocess as sp
import os
import gzip

filefh=sys.argv[1]
newfh=sys.argv[2]

filelist=open(filefh, 'r')
newfile=open(newfh, 'w')

countdict={}

for bam in filelist:
    if bam=='': break
    bam=bam.strip()
    if bam not in countdict: countdict[bam]=0
    proc=sp.Popen(['samtools','view',bam], stdout=sp.PIPE)
    output=proc.stdout
    for line in output:
        if line=='': break
        split=line.split('\t')
        if split[12].startswith("XS:i"): continue
    else:
            countdict[bam]+=1

for bamf in countdict:
    newfile.write(str(bamf)+'\t'+str(countdict[bamf])+'\n')

filelist.close()
newfile.close()
