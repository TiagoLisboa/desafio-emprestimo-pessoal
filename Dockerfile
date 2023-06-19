FROM docker.io/python:3.8 AS builder

RUN pip install --user pipenv

ENV PIPENV_VENV_IN_PROJECT=1

ADD emprestimo/Pipfile.lock emprestimo/Pipfile /usr/src/

WORKDIR /usr/src

RUN /root/.local/bin/pipenv sync

FROM python:3.8 AS runtime

ENV DockerHOME=/home/app/microservice

WORKDIR $DockerHOME

RUN mkdir -v $DockerHOME/.venv

COPY --from=builder /usr/src/.venv/ $DockerHOME/.venv/

RUN mkdir -p $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install pipenv

COPY ./emprestimo $DockerHOME
RUN pipenv install
EXPOSE 8000
CMD pipenv run python manage.py runserver
