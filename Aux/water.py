import math

def stm(t,p,r):
	print('T in ºC, P in MPa')
	lrho=0
	vs=0
	lvsub=0
	lhsub=0
	lssub=0
	vhsup=0
	#Limits
	if r ==1:
		if t < 92 or t > 357.03:
			print("temperature(ºC) out of range, must be 91.70 and 357.03")
			return
	if r == 2:
		if t < 17.511 or t > 373.253:
			print("temperature(ºC) out of range, must be between 89.965 and 373.253")
			return
		if p < 0.002 or p > 21.5:
			print("pressure(Mpa) out of range, must be between 0.002 and 21.5")
			return
	if r == 3:
		if p < 0.085 or p > 21.5:
			print("pressure(Mpa) out of range, must be between 0.002 and 21.5")
			return
	#Ps
	if t >= 17.511 and t < 56.275:
		a=99.2
		b=270.1210
		c=7.4063605
	if t >= 56.275 and t < 90.880:
		a=78.12
		b=254.5831
		c=6.4058216
	if t >= 90.880 and t < 139.781:
		a=57.0
		b=236.2315
		c=5.6029720
	if t >= 139.781 and t < 203.662:
		a=28.0
		b=207.9248
		c=4.7785040
	if t >= 203.662 and t <= 299.407:
		a=5.0
		b=185.0779
		c=4.3043750
	if t > 299.407 and t < 355.636:
		a=16.0
		b=195.1819
		c=4.4608430
	if t >= 355.636 and t <= 373.000:
		a=50.0
		b=227.2963
		c=4.9607850
	ps = ((t+a)/b)**c
	#Ts
	if p >= 0.002 and p < 0.01672:
		a=270.1210
		b=0.135019
		c=-99.2
	if p >= 0.01672 and p < 0.07250:
		a=254.6831
		b=0.156108
		c=-78.2
	if p >= 0.07250 and p < 0.35900:
		a=236.2315
		b=0.1784767
		c=-57.0
	if p >= 0.35900 and p < 1.67600:
		a=207.9248
		b=0.2092705
		c=-28.0
	if p >= 1.67600 and p < 8.511:
		a=185.0779
		b=0.232317
		c=-5.0
	if p >= 8.511 and p < 17.69:
		a=195.1819
		b=0.2241729
		c=-16.0
	if p >= 17.69 and p <= 21.5:
		a=227.2963
		b=0.2015810
		c=-50.0
	ts=a*p**b+c
	if r == 1:
		#Subcooled liquid volume
		if ps >= 0.075 and ps <= 1:
			a=1.2746977e-4
			b=0.4644338
			c=0.001
		if ps > 1 and ps <= 3.880:
			a=1.0476071e-4
			b=0.5651090
			c=0.001022
		if ps > 3.880 and ps <= 8.840:
			a=3.2836717e-5
			b=1.0
			c=1.12174735e-3
		if ps > 8.840 and ps <= 14.463:
			sublv=(3.3551046e-4*math.exp(5.8403566e-2*ps)+0.00085)**-1+(170/(375-t)-0.2)*(p-ps)
			lvsub=1
		if ps > 14.463 and ps <= 18.052:
			a=3.1014626e-8
			b=3.284754
			c=0.001430
		if ps > 18.052 and ps <= 20.204:
			a=1.5490787e-11
			b=5.7205
			c=0.001605
		if ps > 20.204 and ps <= 21.50:
			a=4.1035988e-24
			b=15.03329
			c=0.00189
		if lvsub != 1:
			sublv=(a*ps**b+c)**-1+(170/(375-t)-0.2)*(p-ps)
		sublv=(sublv*.001)**-1
		#Subcool liquid Enthalpy, sublh
		if ps > 0.075 and ps < 0.942:
			a=912.1779
			b=0.2061637
			c=-150.0
		if ps >= 0.942 and ps < 4.020:
			a=638.0621
			b=0.2963192
			c=125.0
		if ps >= 4.020 and ps < 9.964:
			a=373.7665
			b=0.4235532
			c=415.0
		if ps >= 9.964 and ps < 16.673:
			a=75.38673
			b=0.8282384
			c=900.0
		if ps >= 16.673 and ps < 20.396:
			a=0.1150827
			b=2.711412
			c=1440.0
		if ps >= 20.396 and p <= 21.7:
			sublh=9.1417257e-14*ps**11.47287+1752.0+(1.4-169/(369-t))*(p-ps)
			lhsub=1
		if lhsub != 1:
			sublh=a*ps**b+c+(1.4-169/(369-t))*(p-ps)
		#Subcool liquid Entropy, subls
		if ps >=0.065 and ps < 1.666:
			a=3.340244
			b=0.125474
			c=-1.20
		if ps >= 1.666 and ps < 8.825:
			a=1.748203
			b=0.2275611
			c=0.40
		if ps >= 8.825 and ps < 16.666:
			a=0.2549238
			b=0.6381866
			c=2.25
		if ps >= 16.660 and ps <= 21.250:
			subls=4.3632383e-5*(ps-0.40)**3.153273+3.50+(0.0004-0.325/(370-t))*(p-ps)
			lssub=1
		if lssub != 1:
			subls=a*ps**b+c+(0.0004-0.325/(370-t))*(p-ps)
		print('Subcool Liquid density(cm3/g)      =','%.6e'% sublv)
		print('Subcool Liquid Enthalpy            =','%.6e'% sublh)
		print('Subcool Liquid Enthropy(kJ/(kg k)) =','%.6e'% subls)
	if r == 2:		
		#specific density for liquid phase rhol (kg/m3)
		if p >= 0.002 and p < 0.01468:
			a=1.9118e-4
			b=0.546472
			c=0.0009947
		if p >= 0.01468 and p < 0.275:
			a=1.380934e-4  
			b=0.388715
			c=0.000987
		if p >= 0.275 and p <= 1.000:
			a=1.2746977e-4  
			b=0.4644339
			c=0.001
		if p > 1.000 and p <= 3.880:
			a=1.0476071e-4
			b=0.5651090
			c=0.001022
		if p > 3.880 and p <= 8.840:
			a=3.2836717e-5
			b=1.0
			c=0.00112174735
		if p > 8.840 and p <= 14.463:
			rhol=(3.3551046e-4*math.exp(5.8403566e-2*ps)+0.00085)**-1
			lrho=1
		if p > 14.463 and p < 18.052:
			a=3.1014626e-8
			b=3.2847540
			c=0.00143
		if p >= 18.052 and p < 20.204:
			a=1.5490787e-11
			b=5.7205
			c=0.001605
		if p >= 20.204 and p <= 21.5:
			a=4.1035988e-24
			b=15.03329
			c=0.00189
		if lrho !=1:
			rhol=(a*ps**b+c)**-1
		rhol=(rhol*0.001)**-1
		#specific volume for the vapor phase (m3/kg), vv
		if p >= 0.002 and p < 0.2139:
			a=5.0981616
			b=0.936226
			c=-0.00025
		if p >= 0.2139 and p < 1.112:
			a=5.126076
			b=0.9475862
			c=0.012
		if p >= 1.112 and p < 3.932:
			a=4.630832
			b=1.038819
			c=0.520
		if p >= 3.932 and p < 8.996:
			a=2.868721
			b=1.252148
			c=3.800
		if p >= 8.996 and p < 14.628:
			a=0.5497653
			b=1.831182
			c=18.111
		if p >= 14.628 and p <= 18.210:
			a=8.5791582e-3
			b=3.176484
			c=50.0
		if p > 18.210 and p <= 20.253:
			a=3.5587113e-6
			b=5.660939
			c=88.0
		if p > 20.253 and p <= 21.5:
			a=3.558734e-16
			b=13.03774
			c=138.00
		vv=(a*p**b+c)**-1
		vv=vv*1000
		#specific enthalpy (kj/kg) for liquid phase
		if p >= 0.0020 and p < 0.0173:
			a=1128.7770
			b=0.1351960
			c=-413.72
		if p >= 0.0173 and p < 0.1028:
			a=1050.7085
			b=0.1617970
			c=-306.50
		if p >= 0.1028 and p < 0.9420:
			a=912.1779
			b=0.2061637
			c=-150.00
		if p >= 0.9420 and p < 4.0200:
			a=638.0621
			b=0.2963192
			c=125.00
		if p >= 4.0200 and p < 9.964:
			a=373.7665
			b=0.4235532
			c=415.00
		if p >= 9.964 and p < 16.673:
			a=75.38673
			b=0.8282384
			c=900.00
		if p >= 16.673 and p < 20.396:
			a=0.1150827
			b=2.711412
			c=1440.00
		if p >= 20.396 and p <= 21.500:
			a=9.1417257e-14
			b=11.47287
			c=1752.00
		hl=a*ps**b+c
		#specific enthalpy (kJ/kg) for the vapor phase hv
		if p >= 0.002 and p < 0.1379:
			hv=529.44008*p**0.108652+2263.5
		if p >= 0.1379 and p < 0.348:
			hv=-4.0381938e-6*(3.0-p)**15.72364+2750.0
		if p >= 0.348 and p < 1.248:
			hv=-0.5767304*math.exp(-1.66153*(p-3.2))+2800.0
		if p >= 1.248 and p < 2.955:
			a=-7.835986
			b=-3.001
			c=-2.934312
			d=2803.71
		if p >= 2.955 and p <= 6.522:
			a=-1.347244
			b=-2.999
			c=-2.326913
			d=2803.35
		if p > 6.522 and p < 16.497:
			a=-0.9219176
			b=-9.0
			c=-16.38835
			d=2742.03
		if p >= 16.497 and p < 20.193:
			a=-3.532177
			b=-8.0
			c=29.81305
			d=2565.00
		if p >= 20.193 and p <= 21.5:
			a=-22.92521
			b=-18.0
			c=44.23671
			d=2415.01
		if p >=1.248:
			hv=a*(p+b)**2+c*(p+b)+d
		#specific entropy (kj/(kg*k)) for liquid phase sl
		if p >= 0.0020 and p < 0.0812:
			a=4.5397665
			b=0.0
			c=0.0829772
			d=-2.449
		if p >= 0.0812 and p < 1.6660:
			a=3.340244
			b=0.0
			c=0.125474
			d=-1.200
		if p >= 1.6660 and p < 8.8250:
			a=1.748203
			b=0.0
			c=0.2275611
			d=0.400
		if p >= 0.8250 and p < 16.6600:
			a=0.2549238
			b=0.0
			c=0.6381866
			d=2.250
		if p >= 16.6600 and p <= 21.500:
			a=4.3632383e-5
			b=-0.04
			c=3.153273
			d=3.500
		sl=a*(ps+b)**c+d
		#specific enthropy (kJ/(kg k)) for the vapor phase, sv
		if p >= 0.002 and p < 0.0916:
			a=16.644659
			b=0.0
			c=-0.0192733
			d=-10.039
		if p >= 0.0916 and p < 1.480:
			sv=6.58681-0.335924*math.log(p)
			vs=1
		if p >= 1.480 and p <= 8.050:
			a=1.227544
			b=0
			c=0.2481072
			d=7.80
		if p > 8.050 and p <= 15.640:
			a=-0.084638514
			b=0
			c=0.9082161
			d=6.30
		if p > 15.640 and p <= 20.00:
			a=-3.6897161e-3
			b=-7.8
			c=2.012466
			d=5.50
		if p > 20.0 and p <= 21.5:
			a=-0.042830642
			b=-18.7
			c=1.779526
			d=5.0
		if vs !=1:
			sv=a*(p+b)**c+d
		print('Liquid volume(cm3/g)       =','%.6e'% rhol)
		print('Vapor volume (cm3/g)       =','%.6e'% vv)
		print('Void fraction              =','%.6e'% float(vv/(vv+rhol)))
		print('Liquid Enthalpy            =','%.6e'% hl)
		print('Vapor Enthalpy(kJ/kg)      =','%.6e'% hv)
		print('Liquid Enthropy(kJ/(kg k)) =','%.6e'% sl)
		print('Vapor Enthropy(kJ/(kg k))  =','%.6e'% sv)
		return
	if r == 3:
		#Superheated volume, supvv
		if p > 0.085 and p < 1.112:
			a=5.126076
			b=0.9475862
			c=0.012
		if p >= 1.112 and p < 3.932:
			a=4.630832
			b=1.038819
			c=0.520
		if p >= 3.932 and p < 8.992:
			a=2.868721
			b=1.2521
			c=3.8
		if p >= 8.996 and p < 14.628:
			a=0.5497653
			b=1.831182
			c=18.111
		if p >= 14.628 and p < 18.210:
			a=8.5791582e-3
			b=3.176484
			c=50.0
		if p >= 18.210 and p <= 20.253:
			a=3.5587113e-6
			b=5.660939
			c=88.0
		if p > 20.253 and p <= 21.5:
			a=3.558734e-16
			b=13.03774
			c=138.0
		supvv=(a*p**b+c)**-1+(0.000466/p-(0.12/(t+100)-0.00106)*p**0.1/math.sqrt(1.96e-8*(t+8)**4-p**2))*(t-ts)
		supvv=supvv*1000
		#Superheated ehthalpy, supvh
		if p > 0.075 and p <= 0.348:
			supvh=-4.0381938e-6*(3.0-p)**15.72364+2750.0-(4.5*p/math.sqrt(7.4529e-6*t**3-p**2)+0.28*math.exp(-0.008*(t-162))-100/t-2.225)*(t-ts)
			vhsup=1
		if p >= 0.348 and p < 1.248:
			supvh=-5.767304*math.exp(-1.66153*(p-3.2))+2800.0-(4.5*p/math.sqrt(7.4529e-6*t**3-p**2)+0.28*math.exp(-0.008*(t-162))-100/t-2.225)*(t-ts)
			vhsup=1


		print(ts,supvh)
