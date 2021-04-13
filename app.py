from flask import Flask, request
import pickle


app = Flask(__name__)

with open('pipe.pickle', 'rb') as f:
    pipe = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        the_data = request.get_json(force = True)
        testdata = the_data['testdata']
        prediction = pipe.predict([testdata])
        return{'prediction':prediction.tolist()}
