from flask import Flask,request,jsonify,render_template
import os
import sentiment_mod as s
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/getnlpscore',methods=['POST'])
def get_score():
    request_data = request.form.get('TextToAnalyse')
    print(request_data)
    if request_data == "":
        request_data = "Python is awesome."
    sentiment_output = s.sentiment(request_data)

    output = {
        "text":request_data,
        "sentiment":sentiment_output[0],
        "confidence":sentiment_output[1]
    }
    return jsonify(output)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')