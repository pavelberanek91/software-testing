from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

db = [
    {
        "name": "Svíčková",
        "recipe": "Přidám maso, zeleninu, koření a zaliju vodou. Vařím 2 hodiny."
    },
    {
        "name": "Guláš",
        "recipe": "Přidám maso, papriku, maďarské koření a zaliju vodou. Vařím 3 hodiny."
    },
    {
        "name": "Rajská",
        "recipe": "Přidám maso, rajčata, zaliju vodou. Vařím 1 hodinu."
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route("/recipes")
def recipes():
    return render_template("recipes.html", recipes=db)

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        recipe_name = request.form.get("name")
        recipe_procedure = request.form.get("recipe")
        db.append({"name": recipe_name, "recipe": recipe_procedure})
        return redirect("/recipes")

if __name__ == "__main__":
    app.run(debug=True, port=5000)