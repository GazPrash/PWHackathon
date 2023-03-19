import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder



def PreProcessing(data_path):
    emotions_map = {category : i for category, i in zip(data.Emotion.unique(), range(0, 6))}

    data = pd.read_csv(data_path, sep=";")
    data["EmoNum"] =  data.Emotion.apply(lambda x : int(emotions_map[x]))
    
    return data

def ModelTraining(data):
    Xtrain, Xtest, ytrain, ytest = train_test_split(data[["Text"]], data["EmoNum"], test_size=0.25)

    vectorizer = CountVectorizer()
    corpus = vectorizer.fit_transform(Xtrain.Text).toarray()
    test_corpus = vectorizer.transform(Xtest.Text).toarray()

    clf = MultinomialNB()
    clf.fit(corpus, ytrain)

    acc = clf.score(test_corpus, ytest)
    print(f"Training completed with a score of {acc:.2f}")

    return (clf, vectorizer)

def Save(clf, wordvec, id):

    with open("model/saved_models/model_{id}.pkl") as f:
        pickle.dump(clf, f)

    with open("model/saved_models/wordvector_{id}.pkl") as v:
        pickle.dump(wordvec, v)


def main():
    path = "data/train.csv"
    data = PreProcessing(path)
    clf, word_vector = ModelTraining(data)
    Save(clf, word_vector, 244)


    

    





