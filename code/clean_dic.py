import pickle
def main():
	with open('ohpt_dic' + '.pkl', 'wb') as f:
		pickle.dump({}, f, pickle.HIGHEST_PROTOCOL)

main()