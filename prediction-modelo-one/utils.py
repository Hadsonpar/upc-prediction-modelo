import numpy as np

def load_data():
    data = np.loadtxt("data/MRL01/dataset.txt", delimiter=',')
    #data = np.loadtxt("data/trainingdata.txt", delimiter=',')
    X = data[:,0]
    y = data[:,1]
    return X, y
