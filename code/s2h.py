from __future__ import division
import pickle
def main():
	mappings = {}
	new_dic = {}
	with open('ohpt_dic.pkl' , 'rb') as f:
		dictionary = pickle.load(f)

	with open('clusters_hc_num', 'rb') as f:
		lines = f.readlines()
		for line in lines:
			homonym = []
			lst = line.split()
			for w in lst:
				word, tag, num = w.split('#')
				homonym.append(word+'-'+tag+num)
			if word not in mappings:
				mappings[word] = [homonym]
			else:
				mappings[word].append(homonym)

	for word in dictionary:
		try:
			maps = mappings[word]
		except:
			#senses = dictionary[word]
			#temp_lst = []
			#for s in senses:
			#	temp_lst.append(senses[s])
			#new_dic[word] = temp_lst
			continue
		for m in maps:
			new_lst = []
			for sense in m:
				try:
					new_lst += dictionary[word][sense]
				except:
					continue

			if word not in new_dic:
				new_dic[word] = [new_lst]
			else:
				new_dic[word].append(new_lst)
	
	print(len(new_dic))
	with open('homonym_dic' + '.pkl', 'wb') as f:
		pickle.dump(new_dic, f, pickle.HIGHEST_PROTOCOL)

	
	

main()