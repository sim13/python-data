import matplotlib.pyplot as plt
import numpy as np
# match =[]

def extractor(range_start, range_end):
	match_all = []
	entropy_all = []
	entropy_rel_all = []
	for param in xrange(range_start, range_end):
		match = []
		entropy = []
		entropy_rel = []
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
		entropy_all.append(entropy)
		entropy_rel_all.append(entropy_rel)
	return {"match": match_all, "entropy": entropy_all, "entropy_rel": entropy_rel_all}


print extractor(1,4)["entropy_rel"]
# print extractor(4,6)
# print extractor(6,8)

# match_all =[]
# match_all2 =[]
# match_all3=[]
# entropy=[]
# entropy_rel=[]
# entropy2=[]
# entropy_rel2=[]
# entropy3=[]
# entropy_rel3=[]

# for param in xrange(1,8):
# 	match_1=[]
# 	match_2=[]
# 	match_3 =[]
# 	if(param < 4):
# 		for i in xrange(1,11):
# 			path = 'Experiment Params'+ '/Experiment Params ' + str(param) + '/Dataset' + str(i)
# 			file_out = open(str(path) + "/eval.txt" , 'r' )
# 			for m ,line in enumerate(file_out):
# 				if m ==1:
# 					entropy.append(line.strip())
# 				if m ==1:
# 					match_1.append(line.strip())
# 				if m ==2:
# 					entropy_rel.append(line.strip())
# 				# Calculating percentage match
# 			file_out.close()
# 		match_all.append(match_1)
	
# 	elif (param >=4  and param < 6):
# 		for i in xrange(1,11):
# 			path = 'Experiment Params'+ '/Experiment Params ' + str(param) + '/Dataset' + str(i)
# 			file_out = open(str(path) + "/eval.txt" , 'r' )
# 			for m ,line in enumerate(file_out):
# 				if m ==1:
# 					entropy2.append(line.strip())
# 				if m ==1:
# 					match_2.append(line.strip())
# 				if m ==2:
# 					entropy_rel2.append(line.strip())
# 				# Calculating percentage match
# 			file_out.close()
# 		match_all2.append(match_2)

# 	elif(param >5 and param <8):
# 		for i in xrange(1,11):
# 			path = 'Experiment Params'+ '/Experiment Params ' + str(param) + '/Dataset' + str(i)
# 			file_out = open(str(path) + "/eval.txt" , 'r' )
# 			for m ,line in enumerate(file_out):
# 				if m ==1:
# 					entropy3.append(line.strip())
# 				if m ==1:
# 					match_3.append(line.strip())
# 				if m ==2:
# 					entropy_rel3.append(line.strip())
# 				# Calculating percentage match
# 			file_out.close()
# 		match_all3.append(match_3)

snip=[]
snip_mean=[]
snip_std =[]

## 	snip_std.append(np.std(snip))

# print snip_mean
# print snip_std

# plt.plot([0,1,2] , snip_mean ,marker='o',  label='Mean')
# plt.plot([0,1,2] , snip_std , marker='o', color ='r',  linestyle ='--', label='Std Error' )
# plt.axis([-2,4,0,100])
# plt.xlabel('NM Values')
# plt.ylabel('Mean Percentage Matches')
# plt.title('Plot of Match Percentages vs NM')
# plt.legend()
# plt.show()

# ylabel('Mean Percentage Match')



