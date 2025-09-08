from flask import Flask
from controllers.task_controller import TaskController
from models.base import init_db
import os

template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

init_db()

app.add_url_rule('/tasks', view_func=TaskController.list_tasks, methods=['GET'], endpoint='list_tasks')
app.add_url_rule('/tasks/new', view_func=TaskController.create_task, methods=['GET', 'POST'], endpoint='create_task')
app.add_url_rule('/tasks/update/<int:task_id>', view_func=TaskController.update_task_status, methods=['POST'], endpoint='update_task_status')
app.add_url_rule('/tasks/delete/<int:task_id>', view_func=TaskController.delete_task, methods=['POST'], endpoint='delete_task')

if __name__ == '__main__':
    app.run(debug=True)

