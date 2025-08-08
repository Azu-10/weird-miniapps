from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "crow_secret"  # Required for session management

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/crow_ai", methods=["GET", "POST"])
def crow_ai():
    if "chat" not in session:
        session["chat"] = []

    if request.method == "POST":
        user_input = request.form["user_input"]
        word_count = len(user_input.split())
        crow_response = " ".join(["CAW" for _ in range(word_count)])

        session["chat"].append({"sender": "You", "message": user_input})
        session["chat"].append({"sender": "Crow", "message": crow_response})
        session.modified = True

        return redirect(url_for("crow_ai"))

    return render_template("crow_ai.html", chat=session["chat"])

@app.route("/clear_chat")
def clear_chat():
    session.pop("chat", None)
    return redirect(url_for("crow_ai"))

@app.route("/dino")
def dino_game():
    return render_template("dino.html")

@app.route("/schrodinger")
def schrodinger():
    return render_template("schrodinger.html")


if __name__ == "__main__":
    app.run(debug=True)
