from flask import render_template, request, redirect, url_for
from models.base import Session
from models.task import Task
from models.user import User

class TaskController:

    @staticmethod
    def list_tasks():
        session = Session()
        tasks = session.query(Task).all()
        return render_template('tasks.html', tasks=tasks)

    @staticmethod
    def create_task():
        session = Session()
        if request.method == 'POST':
            title = request.form['title']
            description = request.form.get('description')
            user_id = int(request.form['user_id'])

            new_task = Task(title=title, description=description, user_id=user_id)
            session.add(new_task)
            session.commit()
            return redirect(url_for('list_tasks'))

        users = session.query(User).all()
        return render_template('create_task.html', users=users)

    @staticmethod
    def update_task_status(task_id):
        session = Session()
        task = session.query(Task).get(task_id)
        if task:
            task.status = 'Concluído' if task.status == 'Pendente' else 'Pendente'
            session.commit()
        return redirect(url_for('list_tasks'))

    @staticmethod
    def delete_task(task_id):
        session = Session()
        task = session.query(Task).get(task_id)
        if task:
            session.delete(task)
            session.commit()
        return redirect(url_for('list_tasks'))
