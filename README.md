# Amity allocation system

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
The project structure is divided into models and logic:
* models.py is the Allocation models for Amity
* amity.py is the Allocation logic for Amity 

For help on running the app
`python amity.py <inputfile.txt> -h --help` 

To run the app
`python amity.py <inputfile.txt>` 

This automatically allocates based on the input text file and prints out a formatted result on your terminal

To save the result in a .txt file (e.g results.txt) instead, run
`python amity.py > result.txt`

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

View the report of the coverage on your terminal
`coverage report`

Produce the html of coverage result
`coverage html`
