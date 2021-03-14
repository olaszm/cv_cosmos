# Polls Application


This is a simple polls application where where users can vote for varous poll questions



## How to run locally

Clone project 

    git clone https://github.com/olaszm/cv_cosmos.gitproject

Create and activate venv

    virtualenv my-venv

Install dependencies

    pip install -r requirements.txt

Create superuser

    python manage.py createsuperuser

Then run db migration

    python manage.py migrate

Finally run server

    python manage.py runserver

 
## API end-points
---

**To get list of polls**

    GET /polls/api/list

Response: JSON Object with all the available polls


**To get a specific poll**

    GET /polls/api/poll/:id

Response: One JSON Object with the corresponding poll and related choices