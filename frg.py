from app import app
from app.models import File

@app.shell_context_processor
def make_shell_context():
    return {'File': File}