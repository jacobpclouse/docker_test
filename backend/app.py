from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import datetime

# --- Function to Defang date time ---
def defang_datetime():
    current_datetime = f"_{datetime.datetime.now()}"

    current_datetime = current_datetime.replace(":","_")
    current_datetime = current_datetime.replace(".","-")
    current_datetime = current_datetime.replace(" ","_")
    
    return current_datetime


app = Flask(__name__)

CORS(app, supports_credentials=True)

# Cors = CORS(app)
# CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
# app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/message', methods=['POST'])
def receive_message():
    message = request.json.get('message')
    title = f'At: {defang_datetime()} you sent this: {message}'
    print(message)
    return title


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)    
#    app.run(debug=True)
