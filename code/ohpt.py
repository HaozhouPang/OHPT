import pickle
def main():
	count = 0
	f1 = open("file#.txt", "r")
	f2 = open("word_align#.txt", "r")
	f3 = open("file#_sense", "r")
	f4 = open("map.txt")
	with open('ohpt_dic.pkl' , 'rb') as f:
		dictionary = pickle.load(f)

	sentence = f1.readlines()
	alignment = f2.readlines()
	sense_file = f3.readlines()
	Map = f4.readlines()

	sentence_map = {}
	for line in Map:
		line = line.strip()
		old,new = line.split()
		old = int(old)
		new = int(new)
		if old not in sentence_map:
			sentence_map[old] = [new]
		else:
			sentence_map[old].append(new)

	align_list = []
	for a in alignment:
		temp_dic = {}
		a = a.split()
		for i in a:
			old ,new = i.split("-")
			old = int(old)
			new = int(new)
			if old not in temp_dic:
				temp_dic[old] = [new]
			else:
				temp_dic[old].append(new)
		align_list.append(temp_dic)

	sentence_list = []
	for s in sentence:
		en, ch = s.split(" ||| ")
		en = en.split()
		ch = ch.split()
		sentence_list.append( (en,ch) )


	for line in sense_file:
		line_idx = int(line.split()[1])
		line_idx = sentence_map[line_idx]
		word_idx = int(line.split()[2])
		sense = line.split()[3] + line.split()[-1]

		try:
			en_word = sense.split("-")[0]
		except:
			continue
		ch_idx = []
		for i in line_idx:
			try:
				ch_idx.append(align_list[i][word_idx])
			except:
				continue

		ch_word = []
		for i in range(len(line_idx)):
			idx_l = line_idx[i]	
			try:
				idx_w = ch_idx[i]
				for j in idx_w:
					ch_word.append(sentence_list[idx_l][1][j])
			except:
				continue


		if en_word not in dictionary:
			dictionary[en_word] = {}
			dictionary[en_word][sense] = ch_word
		else:
			if sense not in dictionary[en_word]:
				dictionary[en_word][sense] = ch_word
			else:
				dictionary[en_word][sense] += ch_word
	for i in dictionary:
		print(i, dictionary[i])
	with open('../ohpt_dic' + '.pkl', 'wb') as f:
		pickle.dump(dictionary, f, pickle.HIGHEST_PROTOCOL)

main()