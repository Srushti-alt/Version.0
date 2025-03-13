from flask import Flask, request, jsonify
from flask_cors import CORS
import rf

import pandas as pd
import base64
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {"home": "hello world"}

@app.route('/api', methods=["POST"]) 
def api():
    try:
        data = request.get_json()
        df = pd.DataFrame(data)
        result = rf.GetTargets(df)
        
        return jsonify({
            'energy': result[0][0],
            'conc': result[0][1],
            'perm': result[0][2],
            'pres': result[0][3],
            'nh4': result[0][4],
            'k': result[0][5],
            'na': result[0][6],
            'mg': result[0][7],
            'ca': result[0][8],
            'sr': result[0][9],
            'ba': result[0][10],
            'co3': result[0][11],
            'hco3': result[0][12],
            'no3': result[0][13],
            'f': result[0][14],
            'cl': result[0][15],
            'br': result[0][16],
            'so4': result[0][17],
            'po4': result[0][18],
            'sio2': result[0][19],
            'actArea': result[0][20]
        }), 200
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
