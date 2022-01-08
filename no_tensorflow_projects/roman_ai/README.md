# INTEGER TO ROMAN AI DIGIT RECOGNIZER

## DESCRIPTION

- ### NEURAL NETWORK ARCHITECTURE
  - *INPUT NEURONS*
    This layer is made out of 784 neurons (which may seem a lot but trust me, not near a lot when working with AI and machine learning). The number is so precise because that number is the square root of 28, and in fact, the input shape (meaning the shape of a matrix aka picture) is 28 by 28 pixels. One example of the input is this:
    
    ![mnist_digit](https://user-images.githubusercontent.com/66335475/147718465-48be9bc5-caee-451b-bc75-49b6c03b3970.jpg)

  - *HIDDEN LAYERS*
    There is only one hidden layer in this neural network, (maybe an upgrade could be adding more layers...). This layer consists of the same ammount of input neurons, meaning that no pooling is done. This layer's activation function is ReLu (Rectified Linear Unit) as shown below:
    
    ![relu](https://user-images.githubusercontent.com/66335475/148663238-d0c99cea-3505-4055-9dcf-0523b31785dc.png)
    
  - *OUTPUT LAYERS*
    This layer consists of only 10 total neurons, the reason behind this number lies in the number of possible answersm, in this case we have each number ranging between 0-9, so 10 in total. This layer uses Softmax function as its activation function, because Softmax outputs possibilities ranging from 0-1, so the neuron with the highest possibility is the answer. The output looks something like this:
    
    ![softmax](https://user-images.githubusercontent.com/66335475/148663444-2267e436-9028-4800-9ad4-a5a0de2da683.jpg)
