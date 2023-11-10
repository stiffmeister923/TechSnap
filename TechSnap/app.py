from flask import Flask, request, jsonify, render_template, url_for
import requests
import json

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect_objects():
    try:
        # Get the image file from the user's request
        image = request.files['image']

        # Prepare the data to send to the Ultralytics API
        url = "https://api.ultralytics.com/v1/predict/XZIqtRL285JJK2oEv7Bn"
        headers = {"x-api-key": "33d5eac220b7ee4405eabfd1402d07232b0af928bc"}
        data = {"size": 640, "confidence": 0.25, "iou": 0.45}

        # Make a request to the Ultralytics API
        response = requests.post(url, headers=headers, data=data, files={"image": image})

        # Check for a successful response
        response.raise_for_status()

        # Return the API response to the user
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
