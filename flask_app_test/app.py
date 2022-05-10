from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request

server = Flask(__name__)
spec = FlaskPydanticSpec("flask", title="Demo API", version="v1.0", path="doc")
spec.register(server)

@server.get('/')
def index():
  return 'ok'

server.run(debug=True)


# def server():
#   app = Flask(__name__)
  
#   app.run(debug=True)

# if __name__ == "__main__":
#   server()