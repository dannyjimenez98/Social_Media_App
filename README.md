# Twitter Clone Made using Django
Django project replicating various functions of Twitter.
Users can create an account, log in and out, edit their profile, retweet, like, save and comment on other tweets, create and delete tweets, and follow/unfollow other users.
This is a personal project to help me get familiar with Django.

## How to Run the Project
1.  Clone repository by entering the following into your terminal: 
```bash
git clone https://github.com/dannyjimenez98/Social_Media_App.git
```
2. Change into the project's directory
```bash
cd Social_Media_App
```
3. Create and activate a python virtual environment
```bash
python3 -m venv venv
```
#### Activating Virtual Environment (Mac)
```bash
source ./venv/bin/activate
```
#### Activating Virtual Environment (Windows)
```bash
venv/Scripts/activate
```
4. Install project's required dependencies
```bash
pip install -r requirements.txt
```
5. Make migrations and migrate
```bash
./manage.py makemigrations
```
```bash
./manage.py migrate
```
5. Finally, run the server using the following command
```bash
./manage.py runserver
```