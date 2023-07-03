from apps import create_app
from apps.config import Config
from dotenv import load_dotenv

load_dotenv()
app = create_app(Config)


if __name__ == "__main__":
    # Debug mode can be controlled in .env with
    # FLASK_DEBUG variable.
    app.run(port=8000)
