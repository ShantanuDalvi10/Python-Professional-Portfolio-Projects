from flask import render_template,redirect,url_for,request,Blueprint
from PIL import Image,UnidentifiedImageError
from services.color_service import extract_top_colors

color = Blueprint("color",__name__)

@color.route("/",methods=["GET","POST"])
def home():
    colors=[]
    if request.method == "POST":
        image = request.files.get("image")
        if image is None:
            print("Upload the image.")
            return redirect(url_for("color.home"))
        if image.filename == "":
            print("Enter the filename.")
            return redirect(url_for("color.home"))
        elif not image.filename.lower().endswith((".jpg",".png",".jpeg")):
            print("upload valid file.")
            return redirect(url_for("color.home"))
        try:
            img = Image.open(image)
            img.verify()
        except UnidentifiedImageError:
             print("Invalid file type.")
             return redirect(url_for("color.home"))
        except OSError:
            print("OSError is occurring.")
            return redirect(url_for("color.home"))
        image.seek(0)
        image = Image.open(image)
        try:
            colors = extract_top_colors(image=image)
        except Exception as e:
            print("Problem in extracting colors",e)
            return redirect(url_for("color.home"))

    return render_template("index.html",colors=colors)