# Serpent Extraction
#
# Created: May 28, 2015
# By: Guillermo Ibarra

import os

f_in = 'l3_4g.i_res.m'  #Input File

serpent = {}

for line in open(f_in):
	if line.startswith('GC_UNIVERSE_NAME'):
		uni = line.split("'")[1:][0]
		serpent['Universe-'+uni] = {}
	if line.startswith('MACRO_NG'):
		ng = int(line.split('=')[1].split()[0])
	if line.startswith('INF'):
		idx = int(line.split()[3].strip('])'))
		if (idx == ng) or (idx < ng):
			equal = line.split('=')
			varnam = equal[0].split()[0]
			vardat = equal[1].strip(' [];').split()
			serpent['Universe-'+uni][varnam] = float(vardat[0])
		if idx == 2*ng:
			equal = line.split('=')
			varnam = equal[0].split()[0]
			vardat = equal[1].strip(" [];").split()[:-1]
			for j in range(ng):
				del vardat[j+1]
				vardat[j] = float(vardat[j])
			serpent['Universe-'+uni][varnam] = vardat
		if idx == ng*ng*2:
			equal = line.split('=')
			varnam = equal[0].split()[0]
			vardat = equal[1].strip(" [];").split()[:-1]
			for j in range(ng*ng):
				del vardat[j+1]
				vardat[j] = float(vardat[j])
			serpent['Universe-'+uni][varnam] = vardat
