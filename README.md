###Django online store###
This web application creates an online catalog for a pet store where potential customers can browse pets for sale and manage their accounts.

The configuration uses SQLite.

The main features that have currently been implemented are:

    - models for pet, animal type, breeder/supplier. 
    - customers can view list and detail information for pets and breeders.
    - admin users can create and manage models. 
    
![Untitled Diagram](https://user-images.githubusercontent.com/49750572/66017837-c5fdc400-e51f-11e9-90bc-bf65d6d3b13c.png)

###Requirements###
Python3.7.4 

###Installation###
On MacOS
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3.py collectstatic
python3 manage.py createsuperuser #create a superuser
python3 manage.py runserver

Open a browser to http://127.0.0.1:8000/admin/ to admin page and login with superuser details.
Go to http://127.0.0.1:8000 to see the main site.
