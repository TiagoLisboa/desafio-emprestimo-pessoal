FROM docker.io/python:3.8 AS builder

RUN pip install --user pipenv

# Tell pipenv to create venv in the current directory
ENV PIPENV_VENV_IN_PROJECT=1

# Pipfile contains requests
ADD emprestimo/Pipfile.lock emprestimo/Pipfile /usr/src/

WORKDIR /usr/src

# NOTE: If you install binary packages required for a python module, you need
# to install them again in the runtime. For example, if you need to install pycurl
# you need to have pycurl build dependencies libcurl4-gnutls-dev and libcurl3-gnutls
# In the runtime container you need only libcurl3-gnutls

# RUN apt install -y libcurl3-gnutls libcurl4-gnutls-dev

RUN /root/.local/bin/pipenv sync

FROM python:3.8 AS runtime

# setup environment variable
ENV DockerHOME=/home/app/microservice

# where your code lives
WORKDIR $DockerHOME

RUN mkdir -v $DockerHOME/.venv

COPY --from=builder /usr/src/.venv/ $DockerHOME/.venv/

# set work directory
RUN mkdir -p $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv

# copy whole project to your docker home directory.
COPY ./emprestimo $DockerHOME
# run this command to install all dependencies
RUN pipenv install
# port where the Django app runs
EXPOSE 8000
# start server
CMD pipenv run python manage.py runserver
