from app._app import app, db
from db.schemas import Todo
from forms.add_todo import AddTodoForm
from flask import render_template, redirect, flash
from flask_login import login_required

@login_required
@app.route("/add-todo/<user_id>", methods=["GET", "POST"])
def add_todo(user_id):
    form: AddTodoForm = AddTodoForm()
    if form.is_submitted():
        flash('ToDo added successfully.')
        user = db.get_user(id=int(user_id))
        todo = Todo(
            user_id=user.id, 
            task_name=form.task_name.data,
            time=form.task_time.data
                    )
        user.todos.append(todo)
        db.update_user(user)
        return redirect(f"/todos/{user.id}")
    return render_template("add-todo.html", action=f"/add-todo/{user_id}",form=form)

@login_required
@app.route("/todos/<user_id>")
def todos(user_id):
    user = db.get_user(id=int(user_id))
    return render_template("todos.html", user=user, todos=user.todos)

@login_required
@app.route("/done/<user_id>/<todo_id>")
def mark_done(user_id, todo_id):
    db.done_todo(user_id, todo_id)
    return redirect(f"/todos/{user_id}")

@login_required
@app.route("/delete/<user_id>/<todo_id>")
def delete_todo(user_id, todo_id):
    db.delete_todo(user_id, todo_id)
    return redirect(f"/todos/{user_id}")