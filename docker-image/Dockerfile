FROM python:3.8
RUN apt update
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
ADD . /app
ENV PORT 8080
CMD ["gunicorn", "api:app", "--log-level=debug"]
MAINTAINER Nash Luffman "nashluffman@gmail.com"
