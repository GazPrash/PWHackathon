import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder



def PreProcessing(data_paths):
    data = pd.read_csv(data_paths[0], sep=";")
    test_data = pd.read_csv(data_paths[1], sep=";")

    emotions_map = {category : i for category, i in zip(data.Emotion.unique(), range(0, 6))}
    data["EmoNum"] =  data.Emotion.apply(lambda x : int(emotions_map[x]))
    test_data["EmoNum"] =  test_data.Emotion.apply(lambda x : int(emotions_map[x]))
    
    return data.Text, test_data.Text, data.EmoNum, test_data.EmoNum

def ModelTraining(paths):
    Xtrain, Xtest, ytrain, ytest = PreProcessing(paths)

    vectorizer = CountVectorizer()
    corpus = vectorizer.fit_transform(Xtrain).toarray()
    test_corpus = vectorizer.transform(Xtest).toarray()

    clf = MultinomialNB()
    clf.fit(corpus, ytrain)

    acc = clf.score(test_corpus, ytest)
    print(f"Training completed with a score of {acc:.2f}")

    return (clf, vectorizer)

def Save(clf, wordvec, id):

    with open(f"model/saved_models/model_{id}.pkl", "wb") as f:
        pickle.dump(clf, f)

    with open(f"model/saved_models/wordvector_{id}.pkl", "wb") as v:
        pickle.dump(wordvec, v)


def main():
    paths = ["data/train.csv", "data/test.csv"]
    clf, word_vector = ModelTraining(paths)
    Save(clf, word_vector, 244)

main()
    

    





