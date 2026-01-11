from flask import Flask, render_template, request , url_for , redirect,session
import os
from supabase import create_client, Client
import dotenv

app = Flask(__name__)

app.secret_key = "supersecretkey"

SUPABASE_URL = dotenv.get_key(".env", "SUPABASE_URL")
SUPABASE_KEY = dotenv.get_key(".env", "SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


@app.route('/', methods=["GET","POST"])
def login():
    if session.get("access_token"):
        return redirect(url_for('posts'))
    else:
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            response = supabase.auth.sign_in_with_password({"email": email, "password": password})
            if response.session:
            # Store access token in Flask session
                session["access_token"] = response.session.access_token
                session['email'] = email
                return redirect(url_for('posts'))
    return render_template('login.html')

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")
        response = supabase.auth.sign_up({"email": email, "password": password})
        if response.session:
            supabase.table("users").insert({"name": name, "email": email}).execute()
            session["access_token"] = response.session.access_token
            session['email'] = email
            return redirect(url_for('posts'))
    return render_template('register.html')

@app.route("/posts")
def posts():
    if not session.get("access_token"):
        return redirect(url_for('login'))
    return render_template('posts.html')

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)