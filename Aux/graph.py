from burn_extract import serpent

import matplotlib.pyplot as plt

kinf = []
step = []
for i in range(35):
	k = serpent[str(i)]['Universe-123']['INF_KINF']
	stp = serpent[str(i)]['BURNUP']
	kinf.append(k)
	step.append(stp)

plt.figure(1)
plt.title('K vs Burnup for Universe 123')
plt.xlabel('Burnup Mwd/t')
plt.ylabel('K-inf')
plt.plot(step,kinf)
plt.savefig('k-inf.png')
