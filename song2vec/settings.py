import multiprocessing

CORPUS_FILE = '/home/ruan/train_triplets.txt'
MODEL_FILE = '/home/ruan/cloud2vec_data/word2vec.model'
METADATA_FILE = '/home/ruan/cloud2vec_data/metadata.json'

MSD_FOLDER = '/home/ruan/MSD/'
MSD_CORPUS_FILENAME = 'unique_tracks.txt'
MSD_BUFFER_SIZE = 1024
MSD_METADATA_FILE = '/home/ruan/cloud2vec_data/msd_metadata.json'

CHUNK_SIZE = 1024 * 1024 * 10

MODEL_SIZE = 128
MODEL_WINDOW = 5
MODEL_MIN_COUNT = 1
MODEL_WORKERS = 4

MODEL_EPOCHS = 5

DEFAULT_DICT = {
		'read_counter' : 0,
		'MSD' : None
		}

YOUTUBE_API_KEY = 'AIzaSyBUSXXeNZMRP2fOE80jkLuF7ZB-TsDPcQE'
MAX_HEAP_SIZE = 1024
PROCESSOR_CORES = multiprocessing.cpu_count()
