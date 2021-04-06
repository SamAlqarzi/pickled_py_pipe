import pickle
import json


with open('pipe.pickle', 'rb') as f:
    pipe = pickle.load(f)


with open('test_data.json', 'r') as f:
    test_data = json.load(f)

print(pipe.predict([test_data]))
