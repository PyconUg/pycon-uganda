# [PyCon Africa](https://pycon.africa/)

This is the source code for the https://pycon.africa/ website.

## Running the site locally 

1. Before you can run the site, you will need to install these requirements:

* [Python 3.11](https://python.org)
* [Poetry](https://python-poetry.org/)

Once those are installed, you can do the following:


2. Clone or fork the repo 

Follow the guide on [GitHub Help - Fork a Repo](https://help.github.com/articles/fork-a-repo) to understand how to clone or fork a repo.


3. Use poetry to install all the prerequisite Python packages

```
poetry install 
```

4. Get your database set up 

```
# open a poetry shell. This activates the virtual environment associated with the project 

poetry shell

# look at the shell prompt, it will look a little different. This means that the virtual environment is active

# Then run the migrations 

python manage.py migrate 
```

5. Now everything is set up; you can run the application

```
# If your virtual environment is not active, then activate it

poetry shell

# Run the server 

python manage.py runserver

```

You'll see a whole lot of output in the terminal, it will look something like this:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 12, 2024 - 06:16:26
Django version 5.0.4, using settings 'pyconafrica.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

Now open up a web browser and visit the url that was mentioned. It should be http://127.0.0.1:8000/

That's all. Now the site is running.
