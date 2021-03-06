from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
from .settings import CHUNK_SIZE
from .settings import DEFAULT_DICT, CORPUS_FILE, METADATA_FILE
from .settings import MODEL_FILE, MODEL_SIZE, MODEL_WINDOW, MODEL_WORKERS, MODEL_EPOCHS, MODEL_SUBSAMPLE 
import datetime
import json

default_dict = DEFAULT_DICT

def main():

	try:
		open(METADATA_FILE,'r').close()
	except:
		open(METADATA_FILE,'w+').close()
		with open(METADATA_FILE,'w') as handle:
			D = DEFAULT_DICT
			json.dump(D,handle)
	
	with open(METADATA_FILE,'r') as handle:
		D = json.load(handle)

	
	with open(CORPUS_FILE,'rb') as f, open(METADATA_FILE,'r+') as handle:

		print('Preprocessing the next chunk of data...')

		corpus = []
		word_buffer = {}
		i = D['read_counter']
		pos = CHUNK_SIZE * i
		f.seek(pos)
		chunk = f.read(CHUNK_SIZE)
		if bool(chunk):
			chunk = chunk.decode('utf-8').split('\n')
			chunk = chunk[1:-1]
			word_counter = len(chunk)
			for index,item in enumerate(chunk):
				line = item.split('\t')
				isentry = word_buffer.get(line[0], 0)
				if isentry:
					word_buffer[line[0]] += [line[1]] * int(line[2])
				else:
					word_buffer[line[0]] = [line[1]] * int(line[2])
			corpus += word_buffer.values()
			word_buffer = {}
			i += 1
			D['read_counter'] = i
		else:
			print('Reached end of file. Delete the file metadata.json to start all over again.')
			D['read_counter'] = 0
			handle.seek(0)
			json.dump(D,handle)
			handle.truncate()
			return 1
			
		handle.seek(0)
		json.dump(D,handle)
		handle.truncate()

		
	print('Preprocessing is done. Now training word2vec...')

	try:
		open(MODEL_FILE,'r').close()
		model = Word2Vec.load(MODEL_FILE)
		model.train(corpus,total_examples=len(corpus),total_words=word_counter, epochs=MODEL_EPOCHS)
	except Exception as e:
		print(e)
		print('Creating {0}...'.format(MODEL_FILE))
		path = get_tmpfile(MODEL_FILE)
		model = Word2Vec(corpus,size=MODEL_SIZE,window=MODEL_WINDOW,workers=MODEL_WORKERS,sample=MODEL_SUBSAMPLE)
	model.save(MODEL_FILE)
	print('Current position : {0} . Your model was saved at {1}'.format(i, str(datetime.datetime.now())))

	return 0

if __name__ == '__main__':
	while 1:
		status = main()
		if status:
			break
