from wsgiref.simple_server import make_server

from Framework.main import application


with make_server('', 8080, application) as httpd:
    print("Запуск на порту 8080...")
    httpd.serve_forever()