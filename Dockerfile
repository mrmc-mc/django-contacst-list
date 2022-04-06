FROM python:3.9

LABEL MAINTAINTER="Mostafa Shahbazi | mostafa.shahbazi.d@gmail.com"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /app
WORKDIR /app

COPY . /app/

ADD requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python /royalgate/manage.py makemigrations
RUN python /royalgate/manage.py migrate

RUN python manage.py collectstatic --no-input

RUN mkdir -pv /var/{log,run}/gunicorn/
RUN chown -cR $USER:$USER /var/{log,run}/gunicorn/

# CMD [ "gunicorn","--bind",":8000","core.wsgi:application" ]

CMD ["python", "manage.py", "runserver"]