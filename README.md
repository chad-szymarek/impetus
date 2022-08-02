# Tabletop Character Profiles

A minimalistic website to help keep track of the more narrative aspects of a tabletop rpg character.

# Technologies Used

**Setup and Configuration**: Git, Pypi  
**Back-end Development**: Python, Django  
**Front-end Development**: HTML, CSS

# Building and running the project

In your terminal, clone down the repository
`git clone <clone url here>`

Once the project is cloned down, cd into the project directory that you just made, and activate a python virtual environment.
`python -m venv .venv`
`source .venv/bin/activate`

Update pip once you have activated the virtual environment.
`python -m pip install --upgrade pip`

Install the requirements for the project.
`pip install -r requirements.txt`

Run the Django migrations.
`python manage.py migrate`

Run the server.
`python manage.py runserver`

Create a super user if you want to access the Django admin page for the site.
`python manage.py createsuperuser`

Access the site through the browser.
`http://localhost:8000`
