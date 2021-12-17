### PIZZA OR STEAK RECOGNIZER
## GOALS
- Understanding and apply the following:
  - Convolutional Layers
  - Pooling
  - Computer vision
  - Data augmentation
- Train a neural network to recognize pictures of steak and pizza
- Augment the data and tune learning rates to achieve the best result

## LIBRARIES
- TensorFlow
- Matplotlib
- Numpy

## OVERVIEW
1. DATASET
For this proyect, a minimized version of [Food 101](https://www.kaggle.com/dansbecker/food-101) dataset was used, containing only [pizza and steak](https://storage.googleapis.com/ztm_tf_course/food_vision/pizza_steak.zip). The design of the neural network, yet to be tuned, is as follows:


2. BASELINE MODEL
To start this project, a baseline neural network was created, from that baseline, the goal was to surpass the accuracy on the validation set (in this case the validation set was the test set, not very good practice I know...), the shape of this neural network is shaped as follows:

![base model](https://user-images.githubusercontent.com/66335475/146470488-f938a9c2-5968-4332-a1a2-b6f0de197da8.png)

This model was trained with non-augmented data and performed very well, with a cross-validation accuracy of 99.20% in 10 epochs.

3. FINAL MODEL
Observing the base model, 99.20% is a tough acuuracy value to beat... Yet some tuning was to be made. First, it's better to augment the data by different means, at least some part of the dataset augmented helps improve the accuracy. Second, a learning rate for the Adam function was to be found. Using `lr_scheduler = tf.keras.callbacks.LearningRateScheduler(lambda epoch: 1e-4 * 10**(epoch/20))` and adding callbacks to the model, the best learning rate was discovered, 0.0016.

![learning_rate_graph](https://user-images.githubusercontent.com/66335475/146471235-fc5190aa-b09c-4a59-a72e-f0d332651405.png)

