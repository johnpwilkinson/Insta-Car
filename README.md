# Welcome to InstaCar, our awesome Capstone project for Kenzie Academy

This is our final project for Kenzie Academy, a group effort. We have created an Instagram-like photo-sharing service, geared specifically for car enthusiasts.

# Files

From hot rods to Volkswagens to Teslas -- showcase you garage, current collection, or dream car... and connect with like minded people to grow your network.

![InstaCar]()

# Features

Users can sign up, create their account, and begin sharing faster than a Tesla can run a quarter mile.

You can set your profile up with a bio and a link to your website. Follow others and comment on their uploads.

You are a couple clicks away from sharing your passion for cars with other enthusiasts.

# Get started quickly

![Instacar2](https://photos.google.com/photo/AF1QipNO7_f3qU_m47fzA2oHkbWpEhqrnHM3GpcB2w5q)

## obtain source code

cd into dir you want to clone to and git clone the link from the repo, then cd into the dir that is created

    cd toDir
    git clone https://github.com/johnpwilkinson/Insta-Car.git
    cd Insta-Car

![enter image description here](https://photos.google.com/photo/AF1QipNOBThJQBYoXnJ2YcciM7Mu07L7gh57RzApzvyJ)

## Spin up the app

I have used the Poetry dependency and package manager for Python / Django ([https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation))

To install poetry use this command in your terminal:

     curl -sSL [https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py](https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py) | python -

to launch shell (to install dependencies), while still inside the cloned dir:

    -poetry install -poetry shell

Once shell is spawned, create admin account by running :

    -python manage.py createsuperuser

Then, spin up the app by running:

    -python manage.py runserver

Now the Django server is running locally on localhost:8000. You can use the superuser account you created to access the admin panel at : `localhost:8000/admin` and the app at `localhost:8000/`
