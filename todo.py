from bottle import route, error, template, post
from datetime import datetime
import bottle
import pymongo

@route('/')
def index():
    try:
        connect = pymongo.Connection("mongodb://localhost", safe=True)
        db = connect.todo
        doc = db.tasks
        taskscount = doc.count()
        mytasks = doc.find()
    except:
        return 'Cannot establish connection!'
    return template('template', name='Yegor', count=taskscount, tasks=mytasks)

@post('/add')
def add():
    connect = pymongo.Connection("mongodb://localhost", safe=True)
    db = connect.todo
    doc = db.tasks
    task_text = bottle.request.forms.get('task')
    task_date = datetime.now()
    if len(task_text) > 0:
        task = {'task' : task_text, 'date' : task_date}
        doc.insert(task)
    return bottle.redirect('/')


@post('/delete')
def delete():
    return bottle.redirect('/')

@error(404)
def error404(error):
    return '404'

bottle.run(host='localhost', port=8008)
