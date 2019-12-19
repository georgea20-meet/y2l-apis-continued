from flask import Flask, render_template, request
app = Flask(__name__)
import json
import requests

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    
	image_url = request.form['url-input']
    # At this point you have the image_url value from the front end
    # Your job now is to send this information to the Clarifai API
    # and read the result, make sure that you read and understand the
    # example we covered in the slides! 

    # YOUR CODE HERE!
    headers = {'Authorization': '7092d2def87f4d57918a780ce8272369'}
    api_url = "https://portal.clarifai.com/apps/a002583883da4e0ea16593912b69df4a"

    data ={"inputs":[ 
      {
        "data": {
          "image": {
            "url": "image_url"
          }
        }
      }
    ]}

    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    response_dict = json.loads(response.content)
	response_dict["outputs"][0]["data"]["concepts"]

    
    return render_template('home.html', results= parsed_json)

if __name__ == '__main__':
    app.run(debug=True)