# SDA final project - pharmacy system app

##  Table of Contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)

## General info

The Pharmacy System consists in handling three accounts (doctor, patient and pharmacist) with different functionalities for every single type of account.
The System helps us with shopping and choosing medicines the best for us and it helps doctors and pharmacists make easy to issue prescriptions, also pharmacist can control stock status.
The Project is the result of 280 hours intensive learning on bootcamp training at [the Softwere Development Academy](https://sdacademy.pl). 
Created by: 
- Łukasz Okoń (trainer)
- Karolina Daniel
- Patrycja Szwaba
- Rafał Kalawski
- Wojciech Puchalski 

## Technologies

*  Python 3.10.2
*  Django 4.0
*  HTML 5
*  CSS 4
*  Bootstrap 4.2.1


## Setup

How you can run the project by steps:

1. Create local repository and clone it:

```
$ git init SDA_project
$ git clone https://github.com/KarolinaKDaniel/SDA_project
```

2. Install and create a virtual environment, then run it:

```
$ pip install virtualenv
```

*  linux/mac

```
$ python3 -m virtualenv sda_env
$ source sda_env/bin/activate
```

*  windows

```
$ python -m virtualenv sda_env
$ sda_env/Scripts/activate.bat
```

3. Install all necessary packeages:

```
$ pip install -r final_project/requirements.txt
```

4. Change directory and make migrations to create database.

```
$ cd final_project
$ python manage.py migrate
$ python manage.py makemigrations
$ python mnage.py migrate
```

5. Create superuser (set your username and password) and runserver:

```
$ python manage.py createsuperuser
$ python manage.py runserver
```

 Starting development server at [SDA_project](http://127.0.0.1:8000/)

## Status

Actually project is in progress!
