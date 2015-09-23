# Checkpoint 1

## Amity allocation system

### Challenge
Design an automatic allocation system for amity 

### Description:
This app models a room allocation system for Amity.

Amity has been preloaded with ten offices and ten living rooms.
* Each Office has a maximum size of 6 occupants.
* Each Room has a maximum size of 4 occupants and it is gender specific.

Staffs are not allocated rooms while Fellows can opt for being allocated a room or not.

### Getting Started
## Structure of the project
The project structure is divided into models, logic and view following an MVC format where:
* models.py is the models
* amity.py is the controller(logic) 
* view.py is the view

Run the app from the view.py file on your terminal
`python view.py` 

This prints out a formatted result on your terminal

To save the result in a .txt file instead, run
`python view.py > result.txt`

### Tests
Install a virtual environment using
`pip install virtualenv`

Create a virtual environment using
`virtualenv <virtualenvname>`

To use virtualenv wrapper instead

Install a virtual environment using 
* `pip install virtualenv`
* `pip install virtualenvwrapper` for mac
* `pip install virtualenvwrapper-win` for windows

Create a virtual environment using
`mkvirtualenv <virtualenvname>`

Install the necessary requirements within the virtual environment
`pip install -r requirements.txt`

Run coverage
`coverage run test.py`

Produce the html of coverage result
`coverage html`
