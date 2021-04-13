import requests
import json



# loading test data
with open('test_data.json', 'r') as f:
    test_data = json.load(f)

# posting the test data using post method
r = requests.post('http://127.0.0.1:5000/predict', json={'testdata': test_data})
data = r.json()
prediction = data['prediction']
print(prediction)
