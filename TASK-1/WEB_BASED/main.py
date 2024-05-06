from flask import Flask, render_template, request

app = Flask(__name__)

# Task list (replace with database for persistence)
tasks = []

@app.route("/")
def index():
  return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
  description = request.form.get("description")
  tasks.append({"description": description, "completed": False})
  return render_template("index.html", tasks=tasks)

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
  if 0 <= task_id < len(tasks):
    tasks[task_id]["completed"] = not tasks[task_id]["completed"]
  return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
  if 0 <= task_id < len(tasks):
    del tasks[task_id]
  return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
  app.run(debug=True)
