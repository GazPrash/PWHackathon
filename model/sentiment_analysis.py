import pickle

MODEL_PATH = "model/saved_models/model_{id}.pkl"
VECTOR_PATH = "model/saved_models/wordvector_{id}.pkl"

emotions_map = {0 :'sadness', 1 :'anger', 2 : 'love', 3 : 'surprise', 4 :'fear', 5: 'joy'}


def LoadModel():
    with open(MODEL_PATH, "rb") as f:
        clf = pickle.load(f)
    
    with open(VECTOR_PATH, "rb") as v:
        wordvec = pickle.load(v)

    return (clf, wordvec)


def analyze(conversations):
    clf, wordvec = LoadModel()
    emotions = [0 for i in range(6)]
    
    for reply in conversations:
        corpus = wordvec.transform([reply]).toarray()
        output = clf.predict(corpus)
        emotions.append(emotions_map[output[0]])
        # emotions[output[0]] += 1
        
    

