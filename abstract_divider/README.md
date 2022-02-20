# Abstract divider
## Introduction
Abstracts are sometimes hard to read when they are not correctly divided, skipping the introduction, methods, ... . Abstract divider gets to know the information and divides the sentences accordingly. Recurrent neural networks are particularly good with sequential problems, problems that involve context to know the answer. For example, this picture:

![ball](https://user-images.githubusercontent.com/66335475/154822508-2bfb0e2e-5d54-4b66-8132-65aece0826dd.jpg)

Now, if I were to ask you: what is the direction of the first ball (the one on the bottom)? The answer should be inconclusive, there is not enough context to answer the question, actually, the answer to that question comes from another one: where was the ball one second ago? then if we would know that answer, we can identify the ball's path, like the ball that's on top of the static one, the direction is to the right.

## Strategy and logic
Behind this problem lies an ocean of possible approaches, the one taken in this set of models is the following: this is a sequential problem, meaning that LSTM, bi-LSTM and GRU will be the core of the best result. Data was taken from [Datasets](https://github.com/Franck-Dernoncourt/pubmed-rct.git), a sample of the data looks like this: `BACKGROUND	It is not clear whether these patients would benefit from antifungal treatment.`, so preprocessing was to be made, converting every sentence to a list of python dictionaries like so ``

- Model 0:
  For the first model, TfIdf was used, as well as naive bayes, using the sklearn pipeline the model was constructed and the overall accuracy result was 72.18%. 
- Model 1:
  For the second model, GRU was used, a single layer with 128 neurons inside, as well as an output layer with 5 output neurons. The overall accuracy 82.01%.
- Model 2:
  For the third model, LSTM was used, a single layer with 128 neurons inside
  
