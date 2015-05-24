import matplotlib.pyplot as plt
import numpy as np
# match =[]
match_all =[]
entropy=[]
entropy_rel=[]
snip=[]
snip_mean=[]
snip_std =[]
for param in xrange(1,11):
	match=[]
	for i in xrange(1,11):
		path = 'Experiment Params'+ '/Experiment Params ' + str(param) + '/Dataset' + str(i)
		file_out = open(str(path) + "/eval.txt" , 'r' )
		for m ,line in enumerate(file_out):
			if m ==1:
				entropy.append(line.strip())
			if m ==1:
				match.append(line.strip())
			if m ==2:
				entropy_rel.append(line.strip())
			# Calculating percentage match
		file_out.close()
	
	match_all.append(match)
print match_all
for i in xrange(0,3):
	snip = match_all[i][:]
	snip[:] = [int(i) for i in snip]
	# print snip
	snip =[10*(i) for i in snip]
	# Mean % matches
	snip_mean.append(np.mean(snip))
	snip_std.append(np.std(snip))

print snip_mean
print snip_std

plt.plot([0,1,2] , snip_mean ,marker='o',  label='Mean')
plt.plot([0,1,2] , snip_std , marker='o', color ='r',  linestyle ='--', label='Std Error' )
plt.axis([-2,4,0,100])
plt.xlabel('NM Values')
plt.ylabel('Mean Percentage Matches')
plt.title('Plot of Match Percentages vs NM')
plt.legend()
plt.show()

# ylabel('Mean Percentage Match')

