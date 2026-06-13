from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def create_database():

    conn = sqlite3.connect("volunteers.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS volunteers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        skills TEXT,
        city TEXT
    )
    """)

    conn.commit()
    conn.close()



@app.route("/")
def home():

    return render_template("index.html")



@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    skills = request.form["skills"]
    city = request.form["city"]


    conn = sqlite3.connect("volunteers.db")
    cursor = conn.cursor()


    cursor.execute(
    """
    INSERT INTO volunteers
    (name,email,phone,skills,city)
    VALUES (?,?,?,?,?)
    """,
    (name,email,phone,skills,city)
    )


    conn.commit()
    conn.close()


    return render_template("success.html")



create_database()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)