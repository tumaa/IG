# clone
#### A python application based on Django framework, 2019
####  **[tumaa]**
## Description
This is a clone of the photo-famous instagram application for posting, sharing comments, and liking pictures.
## Requirements ans Set up Instructions
* Python3.6 and above
* Postgresql for databases
* On this repository,, click on the green 'clone or download' button
* navigate to the week2-instagram folder by `cd clone`
* Create a virtual environment using `virtualenv virtual` command
* Run `source virtual/bin/activate`
* Install Django  using `pip install django= 2.2.7`
* create new file `requirements.txt` and run `pip freeze > requirements.txt`
* run `python3.6 manage.py runserver `
* for quick debugging run `python manage.py check` or  `python manage.py test album`
## Known Bugs
NO known Bugs.
## Behavior Driven Development

| Behaviour| Input | Output |
| ------------- | ----------------- | ------------------ |
| Display all photos on database  | "https://example@li.com"   | Loads all photos  |
| Save uploaded images | Upload image | Saves image |
| Update images as app user | update image at from navbar 'update' option | Updates |
| Show image details below image | Click image | Zooms with deets |
| Search by username| search username 'tumaa'| returns images posted by 'saudahabib' |



## Technologies and Main Languages Used
* Python
* Bootstrap
* WhiteNoise
* Django
* PostgreSQL Database
* JavaScript
* CSS


## Support and contact details
Please reach out to me at ramanfatuu@gmail.com.com' for any queries concerning this or any other code.
### License
MIT LICENSE  tumaa [2019]