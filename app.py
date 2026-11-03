from flask import Flask , render_template,request ,jsonify
import pickle

tokenizer = pickle.load(open("models/cv.pkl", "rb"))
model = pickle.load(open("models/clf.pkl", "rb"))

app = Flask(__name__, )
# templates this should be in the templates folder for flask to find it
@app.route("/")
def home():
    return render_template("index.html")



# Form submission endpoint for prediction

@app.route("/predict", methods=["POST"])
def predict():

    # 1. Get email content from form
    email_text = request.form.get("email-content", "")

    # 2. Validate email content type
    if not isinstance(email_text, str):
        return render_template(
            "index.html",
            error="Email content must be text",
            email_text=""
        )

    # 3. Validate empty email
    email_text = email_text.strip()

    if not email_text:
        return render_template(
            "index.html",
            error="Please enter email content",
            email_text=email_text
        )

    # 4. Prediction
    tokenized_text = tokenizer.transform([email_text])
    prediction = int(model.predict(tokenized_text)[0])

    # 5. Return result
    return render_template(
        "index.html",
        prediction=prediction,
        email_text=email_text
    )



# API endpoint for prediction

@app.route("/api/predict", methods=["POST"])
def api_predict():

    # 1. Validate JSON request
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON request"}), 400

    # 2. Validate email field
    email = data.get("email-content")

    if not isinstance(email, str):
        return jsonify({"error": "Email content must be a string"}), 400

    # 3. Validate empty email
    email = email.strip()

    if not email:
        return jsonify({"error": "Email content cannot be empty"}), 400

    # 4. Prediction
    tokenized_email = tokenizer.transform([email])
    prediction = int(model.predict(tokenized_email)[0])

    # 5. Return response
    return jsonify({
        "prediction": prediction,
        "label": "Spam" if prediction == 1 else "Not Spam",
        "email": email
    }), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)