#from extract_serpent import serpent
from xtract_v1.py import serpent

uni = ['1','3']

outfile = open('salidas.txt','w')

for i in range(len(uni)):
	k = serpent['Universe']['uni_'+uni[i]]['INF_KINF']	
	fis = serpent['Universe']['uni_'+uni[i]]['INF_FISS']
	dif = serpent['Universe']['uni_'+uni[i]]['INF_DIFFCOEF']
	rem = serpent['Universe']['uni_'+uni[i]]['INF_REMXS']
	chi = serpent['Universe']['uni_'+uni[i]]['INF_CHIP']
	s0 = serpent['Universe']['uni_'+uni[i]]['INF_S0']
	nsf = serpent['Universe']['uni_'+uni[i]]['INF_NSF']
	print('Universo: '+uni[i],file=outfile)
	print('k:'+' '*5,k,file=outfile)
	print('fis:'+' '*3,fis,file=outfile)
	print('rem:'+' '*3,rem,file=outfile)
	print('chi:'+' '*3,chi,file=outfile)
	print('s0:'+' '*4,s0,file=outfile)
	print('nsf:'+' '*3,nsf,file=outfile)
	print('dif:'+' '*3,dif,file=outfile)
outfile.close
