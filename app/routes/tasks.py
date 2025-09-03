from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from app import db
from app.models import Task

tasks_bp=Blueprint('tasks',__name__)#Here tasks is a flask's routine system 

@tasks_bp.route('/')

def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    tasks=Task.query.all()#Here task is python variable name and it is not related to blueprint name
    return render_template('tasks.html',tasks=tasks)

@tasks_bp.route('/add_tasks',methods=["POST"])
def add_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    title=request.form.get('title')
    if title:
        new_task=Task(title=title,status='Pending')
        db.session.add(new_task)
        db.session.commit()
        flash('Task added SuccessFully','success')
    
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>',methods=["POST"])
def toggle_status(task_id):
    task=Task.query.get(task_id)
    if task:
        if task.status=="Pending":
            task.status="Working"
        elif task.status=="Working":
            task.status="Done"
        else:
            task.status="Pending"
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/clear_tasks',methods=["POST"])
def clear_tasks():
    Task.query.delete()
    db.session.commit()
    flash('All tasks Cleared!','info')
    return redirect(url_for('tasks.view_tasks'))    
