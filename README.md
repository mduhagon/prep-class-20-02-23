## Step 1, setup a new repo for this exercise

```
git init
```

'master' is a term with negative connotations.
Many developers and companies are pushing to stop using it in favor
of mmore neutral terms like main

```
git config --global init.defaultBranch main
git branch -m main
```

Creating a .gitignore file is a good idea so we do not commit files
we know we don't want in our repo (and these do not show as pending changes)



## Step 2, create a venv, install Flask

Create and activate a virtual environment called 'venv':
[reference on venvs from Flask documentation]!(https://flask.palletsprojects.com/en/2.1.x/installation/#virtual-environments)

```
python3 -m venv venv
. venv/bin/activate
```

Install Flask in our active virtaul env:
```
pip install flask
```

## Step 3, the 'Hello World' Flask app

https://flask.palletsprojects.com/en/2.2.x/quickstart/

Create a file called `app.py`

```
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    return 'Hello World from Python Flask!'

app.run(host='0.0.0.0', port=5000)
```


- Make a route handler for /

- Run the app in debug mode so you can make changes on the fly:

```
flask run --debug
```