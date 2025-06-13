from flask import Flask, request, render_template
from flask import redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database config
db = SQLAlchemy()

class Config():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app_todo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app.config.from_object(Config)
db.init_app(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)
    
    def get_name(self):
        return self.name

    def status(self):
        return self.done
    
    def make_done(self):
        self.done = True
        db.session.commit()

class TasksManager():
    def add_task(self, name):
        task = Task(name=name)
        db.session.add(task)
        db.session.commit()

    def remove_task(self, id):
        task = Task.query.get(id)
        if task:
            db.session.delete(task)
            db.session.commit()

    def make_task_done(self, id):
        task = Task.query.get(id)
        if task:
            task.done = True
            db.session.commit()

    def get_pending_tasks(self):
        return Task.query.filter_by(done=False).all()

    def get_completed_tasks(self):
        return Task.query.filter_by(done=True).all()
    
tasks_manager = TasksManager()





# Generujemy potrzebne podstrony (widoki)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == "POST":
        new_task_name = request.form.get("task_name")
        tasks_manager.add_task(new_task_name)
        
    pending_tasks = tasks_manager.get_pending_tasks()
    completed_tasks = tasks_manager.get_completed_tasks()
    return render_template("form.html", pending_tasks=pending_tasks, completed_tasks=completed_tasks)

@app.route("/tasks/delete/<int:id>")
def delete_task(id):
    tasks_manager.remove_task(id)
    return redirect(url_for("tasks"))

@app.route("/tasks/done/<int:id>")
def make_task_done(id):
    tasks_manager.make_task_done(id)
    return redirect(url_for("tasks"))

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)