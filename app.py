from flask import Flask, render_template, request, redirect, session, flash
import sqlite3
import pandas as pd
import joblib
import os

app = Flask(__name__)
app.secret_key = "disease_prediction_secret"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "database", "users.db")
MODEL_PATH = os.path.join(BASE_DIR, "model", "disease_model.pkl")
FEATURE_PATH = os.path.join(BASE_DIR, "model", "feature_names.pkl")
DISEASE_INFO_PATH = os.path.join(BASE_DIR, "dataset", "disease_info.csv")

model = joblib.load(MODEL_PATH)
features = joblib.load(FEATURE_PATH)


# HOME
# ----------------------------
@app.route("/")
def home():
    return render_template("home.html")

# ----------------------------
# ABOUT
# ----------------------------
@app.route("/about")
def about():
    return render_template("about.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            session["user"] = user[1]
            return redirect("/dashboard")

        flash("Invalid Email or Password")

    return render_template("login.html")


# ---------------- SIGNUP ----------------

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        try:

            cursor.execute(
                "INSERT INTO users(name,email,password) VALUES(?,?,?)",
                (name, email, password)
            )

            conn.commit()

            flash("Registration Successful")
            return redirect("/")

        except:
            flash("Email Already Exists")

        finally:
            conn.close()

    return render_template("signup.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    return render_template(
        "dashboard.html",
        username=session["user"],
        symptoms=features
    )


# ---------------- PREDICT ----------------

@app.route("/predict", methods=["POST"])
def predict():

    if "user" not in session:
        return redirect("/")

    selected_symptoms = request.form.getlist("symptoms")

    input_data = {}

    for symptom in features:

        if symptom in selected_symptoms:
            input_data[symptom] = 1
        else:
            input_data[symptom] = 0

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)[0]

    confidence = round(
        max(model.predict_proba(df)[0]) * 100,
        2
    )

    disease_df = pd.read_csv(DISEASE_INFO_PATH)

    disease_row = disease_df[
        disease_df["Disease"] == prediction
    ]

    medicines = disease_row.iloc[0]["Medicines"]
    recommendation = disease_row.iloc[0]["Recommendation"]
    critical = disease_row.iloc[0]["Critical"]

    return render_template(
        "result.html",
        disease=prediction,
        confidence=confidence,
        medicines=medicines,
        recommendation=recommendation,
        critical=critical
    )


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)