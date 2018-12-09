import pickle
def main():
	count = 0
	f1 = open("file#.txt", "r")
	f2 = open("word_align#.txt", "r")
	f3 = open("file#_sense", "r")
	f4 = open("map.txt")
	#with open('ohpt_dic.pkl' , 'rb') as f:
	#	dictionary = pickle.load(f)
	dictionary = {}
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
			en_word = sense.split("-")[0] + "-" + sense.split("-")[1][0]
		except:
			continue
	
		if en_word not in dictionary:
			dictionary[en_word] = []
			dictionary[en_word].append(sense)
		else:
			if sense not in dictionary[en_word]:
				dictionary[en_word].append(sense)

	numeritor = 0
	denominator = len(dictionary)
	#for i in dictionary:
	#	print i, dictionary[i]

	for i in dictionary:
		print i, dictionary[i]
		if len(dictionary[i]) <= 1:
			numeritor += 1
		#else:
		#	print(dictionary[i])
	print(numeritor, denominator) 
		

main()