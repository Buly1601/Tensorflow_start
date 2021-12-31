from roman import *
from nn import *
import matplotlib.pyplot as plt
from PIL import Image
import random

def train_test_vals():
    """ Return the train and test set of values """
    # get the data from dataset (csv)
    train_data = pd.read_csv("./digit_data/train.csv/train.csv")
    # COMMENTED FOR SPEED PURPOSES
    # test_data = pd.read_csv("./digit_data/train.csv/train.csv")
    # get useful measurements
    m, n= train_data.shape

    # convert to numpy arrays
    train_data = np.array(train_data)

    # test_data = np.array(test_data)

    # shuffle the data for better performance and prevent overfitting
    np.random.shuffle(train_data)
    # np.random.shuffle(test_data)

    # only take 1000 for training, rest for testing
    train_data = train_data.T
    y_train = train_data[0]
    X_train = train_data[1:n]
    X_train = X_train / 255.

    return X_train, y_train


def get_random_choice(X):
    """
    Gets the choice of the user and returns the number to calculate
    """
    # Get a random spot to start showing the user
    random_spot = random.randint(0, 200)
    chosen = False
    chance = X[:, random_spot, None]
    vector = chance
    while not chosen:
        print("I'll show you a new picture")
        chance = X[:, random_spot+1, None]
        vector = chance
        chance = chance.reshape((28,28)) * 255
        img = Image.fromarray(np.uint8(chance))
        img.show()

        print("If that's the one you'll choose, type 'y', 'n' otherwise")
        d = input()
        if d == "y":
            return vector, chance
        random_spot += 1

    return chance

def main(trained=False):
    """
    Main function that runs the program
    """
    X, y = train_test_vals()
    # check if neural network has been trained
    if not trained:
        print("Training Neural Network...")
        print("Please stand by.")
        w1, b1, w2, b2 = trainer(X, y)
        trained = True

    vec, img = get_random_choice(X)
    # add image to neural network and await response
    result = predict(vec, w1, b1, w2, b2)
    
    roman = integer_to_roman(result)

    print(f"Your intger converted to roman string is: {roman}")

    # plot the picture passed to the function
    img = img.reshape((28,28))
    img = Image.fromarray(np.uint8(img))
    img.show()

    return 0

if __name__ == "__main__":
    main()
