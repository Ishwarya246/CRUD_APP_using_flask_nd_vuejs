CRUD APP

# Flask 
# Creating virtual environment 
python3 -m venv env

# Activating virtual environment 
./env/Scripts/activate

# To run flask app
flask run

# To create tables using sqlalchemy
flask shell
from app import db
db.create_all()

# Vue js
npm run serve 

# To create requirements.txt file
pip freeze > requirements.txt

# To install necessary packages in requirements.txt file
pip install -r requirements.txt