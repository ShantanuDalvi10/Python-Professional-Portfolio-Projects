from flask import Blueprint,render_template,request,flash,current_app,redirect,url_for
from services.services import get_player_data

stats  = Blueprint("stats",__name__)

@stats.route("/player-statistics")
def home():
    return render_template("index.html")


@stats.route("/search",methods=['POST'])
def search_player():

    player_name = request.form.get("player-name")
    try:
        player_data = get_player_data(player_name=player_name)
        flash("Player Found Successfully.","success")
        return render_template("index.html", player_data=player_data)
    except ValueError:
        flash("Player does not found.","error")
        return redirect(url_for("stats.home"))
    except Exception:
        current_app.logger.exception("There is problem in searching player")
        flash("Player couldn't found.","error")
        return redirect(url_for("stats.home"))


