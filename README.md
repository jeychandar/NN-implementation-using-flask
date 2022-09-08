# Neural Network Implentation using Flask
#Write about any difficult problem that you solved. (According to us difficult - is something which 90% of people would have only 10% probability in getting a similarly good solution). 

when I was working in text extraction in NLP I faced a problem in extracting the overlapping entity for eg: 1Suresh Kumar.In this example 1 as designator but the word embedding split 1suresh as one token. We cannot tag 1 and suresh as separate. I need to fix that to get the better output.As there is no technical lead there was no guidance for me. So I officially sent Email to the co founder of Spacy Ines Montani. She kind enough to help me to the process. Through that guidance I consult with my manager and they helped me in the implementation process.

#Explain back propagation and tell us how you handle a dataset if 4 out of 30 parameters have null values more than 40 percentage
Backpropogation helps to fine tune the weights based on error rate and reduce the loss for every iteration of epoch. I used interpolate method to handle the 40% of null value.

Prerequisites
You must have Scikit Learn, Pandas, matplotlib, tensorflow (for Neural Network Model) and Flask (for API) installed.

Project Structure
This project has four major parts :

1.model.py - This contains code fot our Machine Learning model to predict employee salaries absed on trainign data in 'train_data_evaluation_part_2.csv' file.
2.app.py - This contains Flask APIs that receives Bookings CheckedIn details through GUI or API calls, computes the precited value based on our model and returns it.
3.request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4.templates - This folder contains the HTML template to allow user to enter Customer booking detail and displays the predicted Bookings CheckedIn.

Running the project

Ensure that you are in the project home directory. Create the machine learning model by running below command -

python model.py

This would create a serialized version of our model into a file model.h5

Run app.py using below command to start Flask API

python app.py

By default, flask will run on port 5000.

Navigate to URL http://localhost:5000

Enter valid numerical values in all 29 input boxes and hit Predict.

If everything goes well, you should be able to see the predcited Bookings CheckedIn vaule on the HTML page!

You can also send direct POST requests to FLask API using Python's inbuilt request module Run the beow command to send the request with some pre-popuated values -

python request.py
