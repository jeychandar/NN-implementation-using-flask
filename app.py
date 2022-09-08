import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, send_file,render_template,Response
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt

app = Flask(__name__)
model = load_model('model2.h5')

data = pd.read_csv('test_data_evaluation_part2.csv')
data.interpolate(inplace=True)
label_encoder = LabelEncoder()
data['Nationality'] = label_encoder.fit_transform(data['Nationality'])
data['DistributionChannel'] = label_encoder.fit_transform(data['DistributionChannel'])
data['MarketSegment'] = label_encoder.fit_transform(data['MarketSegment'])
a = data['Age']
b = data['BookingsCheckedIn']
c = data['LodgingRevenue']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = np.array(float_features)
    prediction = model.predict(final_features.reshape(1,29), batch_size=1)

    output = prediction[0]

    return render_template('index.html', prediction_text='Bookings Checked In {}'.format(output))

@app.route('/visualize')
def visualize():
    plt.style.use('seaborn')
    fig = plt.figure()
    ax1 = fig.add_subplot(121,frameon=False)
    ax2 = fig.add_subplot(122,frameon=False,sharex=ax1)
    ax1.scatter(a, b, c='red')
    ax1.legend()
    ax1.set_xlabel("Age")
    ax1.set_ylabel("CheckedIn")
    ax1.set_title('Age VS CheckedIn')
    ax2.bar(a, c, color='green')
    ax2.legend()
    ax2.set_xlabel("Age")
    ax2.set_ylabel("Revenue")
    ax2.set_title('Age VS Revenue')
    canvas = FigureCanvas(fig)
    img=io.BytesIO()
    fig.savefig(img)
    img.seek(0)

    return send_file(img,mimetype='img/png')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = (prediction[0])
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)