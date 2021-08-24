FROM python:3.8-buster

# create directory for the app user
RUN mkdir -p /home/app

ENV APP_PATH /home/app
WORKDIR ${APP_PATH}


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# Migrate
RUN python ./manage.py migrate

EXPOSE 8000

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]
