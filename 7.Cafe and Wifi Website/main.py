from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("cafes.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    conn = get_db_connection()
    cafes = conn.execute("SELECT * FROM cafe").fetchall()
    conn.close()
    return render_template("index.html",cafes=cafes)

@app.route("/add",methods=["GET","POST"])
def add_cafe():
    if request.method == "POST":
        name = request.form["name"]
        map_url = request.form["map_url"]
        img_url = request.form["img_url"]
        lacation = request.form["location"]

        has_sockets = int("has_sockets" in request.form)
        has_toilet = int("has_toilet" in request.form)
        has_wifi = int("has_wifi" in request.form)
        can_take_calls = int("can_take_calls" in request.form)

        seats = request.form.get("seats","")
        coffee_price = request.form.get("coffee_price","")

        try:
            conn = get_db_connection()
            conn.execute("""
            INSERT INTO cafe(
            name,map_url,img_url,location,
            has_sockets,has_toilet,has_wifi,
            can_take_calls,seats,coffee_price)
            VALUES(?,?,?,?,?,?,?,?,?,?)
            """,(
                name,map_url,img_url,lacation,
                has_sockets,has_toilet,has_wifi,
                can_take_calls,seats,coffee_price
            ))

            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return "Cafe with this name already exists",400
        conn.close()

        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/delete/<int:cafe_id>",methods=["GET","POST"])
def delete_cafe(cafe_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM cafe WHERE id=?",(cafe_id,))
    conn.commit()
    conn.close()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)