# [PyCon Uganda](https://ug.pycon.org/)

This is the source code for the https://ug.pycon.org/ website.

This Repository was bootstraped from a [PyconUg/pycon-africa@ca86f37](https://github.com/PyconUg/pycon-africa/commit/ca86f37ab7092d911581fa372dd054f9e72163b3)

## Running the site locally 

1. Before you can run the site, you will need to install these requirements:

* [Python 3.11](https://python.org)
* [uv](https://docs.astral.sh/uv/)

Once those are installed, you can do the following:


2. Clone or fork the repo 

Follow the guide on [GitHub Help - Fork a Repo](https://help.github.com/articles/fork-a-repo) to understand how to clone or fork a repo.


3. Use uv to install all the prerequisite Python packages. 

```
uv sync
```

This will also create the virtual environment with the project name, in which you will run the project. This is under the .venv folder

4. Activate the virtual environment.

For Linux/MacOS
```
source .venv/bin/activate
```

For Windows
```
.venv\Scripts\activate.bat
```

5. Create and populate the environment variables file
```
cp .env.example .env
```

6. Get your database set up 

```
# run the migrations 

python manage.py migrate 
```

7. Run the seeder script to add some tables to the database
```
python manage.py runscript -v2 seeder.py
```

8. Now everything is set up; you can run the application

```
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
