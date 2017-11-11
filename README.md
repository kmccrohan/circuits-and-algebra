# Circuits and Algebra

The library themed mysql-python project for CPSC321.

# Setup: if you're doing this on your machine (as opposed to ada)
1. Install mysql for your computer.
2. Install python2 for your computer.
3. Install the mysql python connector library. From anywhere in you terminal:
```
pip install mysql
pip install mysql-connector-python-rf
```
4. Populate the database.
```
mysql -u root -p
create database project;
use database project;
source populate.sql;
quit
```
5. Create a file `config.py` to include the correct password to mysql. This is what to put in your password:
```
mysql = {'host': 'localhost',
         'user': 'root',
         'password': '<my_password>'}
```
6. Run your python project.
```
python main.py
```
