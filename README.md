# Neural Network Implentation using Flask
#Write about any difficult problem that you solved. (According to us difficult - is something which 90% of people would have only 10% probability in getting a similarly good solution). 

when I was working in text extraction in NLP I faced a problem in extracting the overlapping entity for eg: 1Suresh Kumar.In this example 1 as designator but the word embedding split 1suresh as one token. We cannot tag 1 and suresh as separate. I need to fix that to get the better output.As there is no technical lead there was no guidance for me. So I officially sent Email to the co founder of Spacy Ines Montani. She kind enough to help me to the process. Through that guidance I consult with my manager and they helped me in the implementation process.

#Explain back propagation and tell us how you handle a dataset if 4 out of 30 parameters have null values more than 40 percentage
Backpropogation helps to fine tune the weights based on error rate and reduce the loss for every iteration of epoch. I used interpolate method to handle the 40% of null value. 