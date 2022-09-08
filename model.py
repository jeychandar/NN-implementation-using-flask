import tensorflow as tf
import keras
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from keras.models import load_model

df = pd.read_csv(r"C:\Users\karth\PycharmProjects\pythonProject\train_data_evaluation_part_2.csv")
df.interpolate(inplace=True)

label_encoder = LabelEncoder()
df['Nationality'] = label_encoder.fit_transform(df['Nationality'])
df['DistributionChannel'] = label_encoder.fit_transform(df['DistributionChannel'])
df['MarketSegment'] = label_encoder.fit_transform(df['MarketSegment'])
print(df.head(5))

df.info()

x = df.drop(columns=['BookingsCheckedIn'])
y= df[['BookingsCheckedIn']]

model = tf.keras.Sequential()

model.add(tf.keras.layers.Dense(16, activation='relu',input_shape=(29,)))
model.add(tf.keras.layers.Dense(16,activation='softmax'))
model.add(tf.keras.layers.Dense(1))

model.compile(optimizer='adam',loss='mean_squared_error')

model.fit(tf.expand_dims(x, axis=-1),y,epochs=30, callbacks=[tf.keras.callbacks.EarlyStopping(patience=5)])

# traindata = np.array([0,1,137,51,150,45,371,105.3,1,0,8,5,151,1074,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0])
# print(model.predict(traindata.reshape(1,29),batch_size=1))

# testdata = np.array([82590,82591,57,47,11,0,0,0,0,0,0,0,-1,-1,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0])
# print(model.predict(testdata.reshape(1,29),batch_size=1))

model.save('model2.h5')
