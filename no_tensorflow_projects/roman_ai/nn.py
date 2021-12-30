import numpy as np
import pandas as pd

"""

NEURAL NETWORK SHAPE:
-- INPUT LAYER --
-- HIDDEN LAYERS (1) RELU --
-- OUTPUT LAYER SOFTMAX --

"""


def relu(x):
    """ ReLu activation """
    return np.maximum(0, x)

def softmax(z):
    """ SoftMax activation """
    return np.exp(z) / sum(np.exp(z))


def d_relu(x):
    """ ReLu activation function derivative """
    return x > 0


def get_preds(layer):
    """ Gets the predictions """
    return np.argmax(layer, 0)


def get_accuracy(predictions, y):
    """ Gets the accuracy from predictions with y """
    return np.sum(predictions == y) / y.size


def init_params():
    """ Init random params with the correct shape """
    w1 = np.random.rand(10, 784) - 0.5
    b1 = np.random.rand(10, 1) - 0.5
    w2 = np.random.rand(10, 10) - 0.5
    b2 = np.random.rand(10, 1) - 0.5

    return w1, b1, w2, b2


def forward_prop(w1, b1, w2, b2, x):
    """ Forward propagation """
    # hidden layer
    z1 = w1.dot(x) + b1
    a1 = relu(z1)
    # output layer
    z2 = w2.dot(a1) + b2
    a2 = softmax(z2)

    return z1, a1, z2, a2


def one_hot(y):
    """ One-hot encoding """
    one_y = np.zeros((y.size, y.max()+1))
    one_y[np.arange(y.size), y] = 1
    
    return one_y.T


def back_prop(z1, a1, w2, a2, x, y):
    """ Back propagation """
    # https://i.stack.imgur.com/W6S7Y.png

    # length of vector
    m = len(y)
    # one hot encode
    one_h = one_hot(y)
    dz2 = a2 - one_h
    dw2 = (1/m) * dz2.dot(a1.T)
    db2 = (1/m) * np.sum(dz2)
    dz1 = w2.T.dot(dz2) * d_relu(z1)
    dw1 = (1/m) * dz1.dot(x.T)
    db1 = (1/m) * np.sum(dz1)

    return db1, dw1, db2, dw2


def update_params(w1, dw1, db1, b1, w2, dw2, db2, b2, alpha):
    """ Updates the weights and biases """
    w1 = w1 - alpha * dw1
    w2 = w2 - alpha * dw2
    b1 = b1 - alpha * db1
    b2 = b2 - alpha * db2

    return w1, b1, w2, b2


def gradient_descent(X, y, alpha, epochs):
    """ Gradient descent """
    w1, b1, w2, b2 = init_params()

    for e in range(epochs):
        z1, a1, z2, a2 = forward_prop(w1, b1, w2, b2, X)
        db1, dw1, db2, dw2 = back_prop(z1, a1, w2, a2, X, y)
        w1, b1, w2, b2 = update_params(w1, dw1, db1, b1, w2, dw2, db2, b2, alpha)

        # print some useful data for better process understanding
        if e % 10 == 0:
            print(f"--- Epoch {e} ---")
            predictions = get_preds(a2)
            accuracy = get_accuracy(predictions, y)
            print(f"Accuracy of model so far: {accuracy}")

    return w1, b1, w2, b2


def predict(X, w1, b1, w2, b2):
    """ Predict the result of a picture with a pre-trained nn """
    # forward prop with the pre-trained weights
    print("Forward propagating...")
    _, _, _, a2 = forward_prop(w1, b1, w2, b2, X)

    # get the prediction
    print("Predicting...")
    prediction = get_preds(a2)

    # print the prediction
    print(f"The prediction of the picture is... \n {prediction}")
    # print the labels
    # COMMENTED FOR TESTING PURPOSES
    # print(f"The true value is... \n {y[img]}")

    return prediction[0]


def trainer(X, y):
    """ Calls the nn with the image """
    w1, b1, w2, b2 = gradient_descent(X, y, 0.1, 500)
    return w1, b1, w2, b2