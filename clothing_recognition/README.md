# **CLOTHING RECOGNITION**

## **GOALS** 
- Understand and apply the following:
  - Confusion Matrixes
  - Plotting and Certainty 
  - Weights and Biases
- Train a neural network to recognize 10 different clothing items
- Start using Tensorflow in a more advanced level.

## **LIBRARIES**
- TensorFlow
- Matplotlib
- Pandas
- Itertools
- Sklearn
- Numpy

## **OVERVIEW**

1. ### **DATASET**
For this project, "fashion_mnist.load_data" was used, check out here: [fashion_mnist](https://www.tensorflow.org/datasets/catalog/fashion_mnist)
This data incorporates 10 types of clothing listed as follows: *"T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"*. As well as their respective images for neural network training (used 28 by 28 by 1 resolution).

2. ### **NEURAL NETWORK MODELS**
For this proyect, three neural networks were used, chronologically mutating from worst (model_1) to best (model_3).
The ending Neural Network has a shape as follows:

![model_3_shape](https://user-images.githubusercontent.com/66335475/144485473-bfe2a4bc-c444-4a90-aa1d-c0c32005a8f4.png)

3. ### **DATA**
The data used was not normalized in model_1, and normalized in model_2, using Pandas's Dataframe plotting it was possible to observe the change in the model's performance:

![model_performance](https://user-images.githubusercontent.com/66335475/144485911-c9fd434f-f62a-4fe9-b5e0-61aa00e71d58.png)
![model_2_perfomance](https://user-images.githubusercontent.com/66335475/144485989-2e19cac5-bb3c-472e-a846-9890b18f86ea.png)

Changing from high variance to high bias.

4. ### **LEARNING RATE (ADAM)**
Adam function was used, with a learning rate of lr=0.005. Using callbacks the learning rate was determined to be the most proficient one out of all numbers from 0.1 and 0.0001.

![learning_rate](https://user-images.githubusercontent.com/66335475/144486559-5da7a039-4680-4874-bbdb-e13822075c5e.png)

5. ### **CONFUSION MATRIX**
Confusion Matrixes were used to observe the performance of the Neural Network (model_3). Check here for detailed information about Confution Matrixes:[Confusion matrixes explanation](https://www.youtube.com/watch?v=wpp3VfzgNcI)

![cm](https://user-images.githubusercontent.com/66335475/144486966-30f0a127-d61d-46e9-88d0-5429bcc0fdd5.png)

6. ### **PLOT IMAGES WITH USEFUL INFORMATION**
A function was written (plot_random_img) to observe the image, obeserve the neural network's understanding and compare to confusion matrix to understand the desicion taken and upgrade the model.

![plot](https://user-images.githubusercontent.com/66335475/144487367-608a9f88-0dad-4c2b-b33c-43f025930d53.png)

### NEURAL NETWORK TRAINING: SUCCESS

**learned from: "Zero to mastery Tensorflow Developper Certificate in 2022"**
