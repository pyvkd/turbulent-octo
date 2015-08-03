from werkzeug.serving import run_simple
from main import app

if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, app, use_reloader=True)
