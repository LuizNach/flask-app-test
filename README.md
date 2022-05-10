# Flask-App

Application for education purposes.


## Environment

Environment is set up by the py project.toml, I would recommend using [poetry](https://python-poetry.org/).

## Development

Environment variables are located at .env file. To export them run: `source .env`

If you installed your libraries directly on your python global version or you venv:
`python flask_app_app/app.py`

For the poetry install, use:
`poetry run flask run` or `poetry run python -m flask_app_test`

## Routes

Flask show the routes available using the `flask routes`