'''Program to simulate a N X N switch and find the throughput in packets/sec'''
import random as r
#Function to generate random output destination port for a input
def desGenerator(k,n,m):
	if m:
		alpha = [1.0/k]
		alphaSum = [0,1.0/k]
		for i in range(1,n):
			alpha.append(((k-1)/k)*(1.0/(n-1)))
			alphaSum.append(alphaSum[-1]+alpha[i])
	else:
		alpha = [1.0/n]
		alphaSum = [0,1.0/n]
		for i in range(1,n):
			alpha.append(1.0/n)
			alphaSum.append(alphaSum[-1]+alpha[i])
	b = r.random()
	for j in range(0,len(alphaSum)-1):
		if (b > alphaSum[j]) and (b < alphaSum[j+1]):
			return j+1
#Function to get the input ports on which new packet will be received
def nextInput(iDict):
	dip = []
	retList = [n+1 for n in range(0,N)]
	#import pdb;pdb.set_trace()
	if len(iDict.keys()) < N:
		for ip,occ in iDict.items():
			if len(occ) > 1:
				si = [x[0] for x in occ]
				selected = r.choice(si)
				for sitor in si:
					if sitor != selected:
						retList[sitor-1] = 0
				for i,o in enumerate(occ):
					if o[0] == selected:
						del iDict[ip][i]
			else:
				dip.append(ip)
		for ip in dip:
			del iDict[ip]
	else:
		iDict.clear()
	retList = [r for r in retList if r>0]
	return retList
print("Enter 1 For balanced traafic method \nEnter 2 for hot-spot traffic")
met = int(input("Enter the method : ")) - 1
N = int(input("Enter the value of N : "))
for k in range(2,N+1):
	tput = 0
	inputDict={}
	for i in range(0,N):
		outDes = desGenerator(k,int(N),met)
		if outDes not in inputDict.keys():
			inputDict[outDes] = []
		inputDict[outDes].append((i+1,outDes))
	for a in range(0,10**6):
		#print(inputDict)
		tput += len(inputDict.keys())
		nextInp = nextInput(inputDict)
		#print (nextInp)
		#print(inputDict)
		for nip in nextInp:
			outDes = desGenerator(k,int(N),met)
			if outDes not in inputDict.keys():
				inputDict[outDes] = []
			inputDict[outDes].append((nip,outDes))
	print("***** For k=%d *****"%k)
	print("The value of throughput for %dX%d switch is %d packets/sec"%(N,N,tput))
	if not met:
		break