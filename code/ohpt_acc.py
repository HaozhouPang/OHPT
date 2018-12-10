from __future__ import division
import pickle
def main():
	with open('homonym_dic.pkl' , 'rb') as f:
		dictionary = pickle.load(f)
	denominator = len(dictionary)
	numeritor = 0
	for word in dictionary:
		senses = dictionary[word]
		if check_disjoint(senses) == 0:
			with open('violation.txt', 'a') as f:
				f.write(word)
				for i in senses:
					for j in i:
						print j
						f.write(j+" ")
					f.write("\n")
					print '\n'
		numeritor += check_disjoint(senses)
	print(numeritor , denominator)
	#with open('acc.txt' , 'a') as f:
	#	f.write(str(numeritor / denominator) + "\n")

def check_disjoint(lst):
	for l in lst:
		new_lst = lst[:]
		new_lst.remove(l)
		for i in l:
			for j in new_lst:
				if i in j:
					return 0
	return 1


main()