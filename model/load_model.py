import pickle

def LoadModel(model_path):
    with open(model_path, "rb") as f:
        return pickle.load(f)