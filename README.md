# Circuits and Algebra

The library themed mysql-python project for CPSC321.

# Setup: if you're doing this on your machine (as opposed to ada)
1. Install mysql for your computer.
2. Install python2 for your computer.
3. Install the mysql python connector library. From anywhere in you terminal:
```
pip install mysql
pip install mysql-connector-python-rf
pip install tabulate
```
4. Populate the database.
```
mysql -u root -p
create database project;
use database project;
source populate.sql;
quit
```
5. Create a file `config.py` to include the correct password to mysql. This is what to put in your file:
```
mysql = {'host': 'localhost',
         'user': 'root',
         'password': '<my_password>'}
```
6. Run your python project.
```
python main.py
```

# Git
First install git command line tools.

Then, download the project:
```
cd <to-where-I-want-to-clone>
git clone <some-url-from-github>
```

To get the most recent changes from the other person:
```
git pull
```

To add your changes:
```
git add .
git commit -m "<some descriptive message of your work>"
git push
```
When you push, you might get some error saying you need to first `git pull`.
This is because someone else pushed a change and you need to pull down those changes first before your work can be merged.

If you did something really bad and want to discard your changes and revert to the last commit:
```
git reset --hard
```