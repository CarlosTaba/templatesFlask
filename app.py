from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    nombre = "Carlos Taba"  # 🔹 Reemplaza con tu nombre
    return render_template("index.html", nombre=nombre)

if __name__ == "__main__":
    app.run(debug=True)