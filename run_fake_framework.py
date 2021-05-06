from wsgiref.simple_server import make_server

from Framework.main import FakeApplication
from urls import fronts
from views import routes

# создание приложения
application = FakeApplication(routes, fronts)

# и запуск через wsgiref
with make_server('', 8000, application) as httpd:
    print("Запуск на порту 8000...")
    httpd.serve_forever()