# run.py

from project import app

if __name__ == "__main__":
    print(app.config['BASEDIR'])
    print(app.config['TOP_LEVEL_DIR'])
    app.run()
