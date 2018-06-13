## takes a file with a list of gzip'ed vcfs, count number of sites that are not N and PASS quality filters

import sys
import gzip

filelistfh=sys.argv[1]
filelist=open(filelistfh, 'r')
newfh=str("vcf_sites_by_chrom.txt")
newfile=open(newfh, 'w')

totalcount=0
chromcount=0

for line in filelist:
	if line=='': break
	chromcount=0
	myfh=line.strip()
	myfile=gzip.open(myfh)
	mychrom=myfh.split('/')[-1]
	mychrom=mychrom.split('.')[0]
	for aline in myfile:
		if aline=='': break
		if aline.startswith("#"): continue
		elif aline.split()[3]=="N": continue
		elif aline.split()[6]!="PASS": continue
		else:
			chromcount+=1
			totalcount+=1
	print(str(mychrom)+'\t'+str(chromcount))
	newfile.write(str(mychrom)+'\t'+str(chromcount)+'\n')
	myfile.close()

print(str("Total")+'\t'+str(totalcount))
filelist.close()

