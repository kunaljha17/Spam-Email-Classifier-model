from flask import Flask , render_template,request ,jsonify
import pickle

tokenizer = pickle.load(open("models/cv.pkl", "rb"))
model = pickle.load(open("models/clf.pkl", "rb"))

app = Flask(__name__, )
# templates this should be in the templates folder for flask to find it
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    email_text = request.form.get("email-content","")
    tokenized_text = tokenizer.transform([email_text])
    prediction = int(model.predict(tokenized_text)[0])
    return render_template("index.html", prediction=prediction, email_text=email_text)

@app.route("/api/predict", methods=["POST"])
def api_predict():
    data = request.get_json(force=True)
    tokenized_email = tokenizer.transform([data["email-content"]])
    prediction = int(model.predict(tokenized_email)[0])
    return  jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)