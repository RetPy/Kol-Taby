# from datetime import datetime
#
# from core.celery import app
# from apps.todos.models import Todo
#
#
# @app.task()
# def auto_delete():
#     for todo in Todo.objects.filter(status='4'):
#         res = todo.deadline.date() - datetime.date(datetime.today())
#         if res.days <= -8:
#             todo.delete()
