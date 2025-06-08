from flask import Flask, request, render_template
from flask import redirect, url_for


app = Flask(__name__)

class Task():
    def __init__(self, name, id):
        self.name = name
        self.done = False
        self.id = id
    
    def get_name(self):
        return self.name

    def status(self):
        return self.done
    
    def make_done(self):
        self.done = True

class TasksManager():
    def __init__(self):
        self.tasks = {}

    def add_task(self, name):
        id = len(self.tasks)
        self.tasks[id] = Task(name, id)

    def remove_task(self, id):
        del self.tasks[id]

    def make_task_done(self, id):
        self.tasks[id].make_done()

    def get_pending_tasks(self):
        return [t for t in self.tasks.values() if not t.done]

    def get_completed_tasks(self):
        return [t for t in self.tasks.values() if t.done]
    
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
    app.run(debug=True)