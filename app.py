from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
tasks = []
MAX_TASK_LENGTH = 200


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task', '').strip()
    if task and len(task) <= MAX_TASK_LENGTH:
        tasks.append(task)
    return redirect(url_for('index'))


@app.route('/remove_task/<int:index>', methods=['POST'])
def remove_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
