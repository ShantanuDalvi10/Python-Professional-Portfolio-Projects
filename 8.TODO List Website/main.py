from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONs"] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    completed = db.Column(db.Boolean,default=False)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        title = request.form.get("title","").strip()

        if title:
            new_task = Task(title=title)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("home"))

    tasks = db.session.execute(
        db.select(Task).order_by(Task.id.desc())
    ).scalars().all()

    total_tasks = len(tasks)
    completed_tasks = sum(task.completed for task in tasks)
    pending_tasks = total_tasks - completed_tasks

    return render_template("index.html",
                           tasks=tasks,
                           total_tasks=total_tasks,
                           completed_tasks=completed_tasks,
                           pending_tasks=pending_tasks)

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    task = db.get_or_404(Task,task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/edit/<int:task_id>",methods=["GET","POST"])
def edit_task(task_id):
    task = db.get_or_404(Task,task_id)

    if request.method == "POST":
        title = request.form.get("title","").strip()

        if title:
            task.title = title
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("edit.html",task=task)

@app.route("/delete/<int:task_id>",methods=["POST"])
def delete_task(task_id):
    task = db.get_or_404(Task,task_id)

    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("home"))



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        app.run(debug=True)