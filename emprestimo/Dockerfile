FROM python:3.8

ENV DockerHOME=/home/app/microservice

WORKDIR $DockerHOME

RUN pip install --user pipenv
ADD Pipfile.lock Pipfile ./
RUN /root/.local/bin/pipenv install --system

RUN mkdir -p $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . $DockerHOME

EXPOSE 8000

CMD ['python', 'manage.py', 'collectstatic', '--noinput']
CMD ['python', 'manage.py', 'runserver']
