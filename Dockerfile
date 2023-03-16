# pull official base image
FROM ubuntu

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get -y update  \
&& apt-get -y install python3 \
&& apt-get -y install python3-pip \
&& apt-get -y install nano
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
RUN apt-get -y install gunicorn \
&& DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install celery \
&& apt install python3.10-gdbm

# copy project
ADD . /app
WORKDIR /app
RUN chmod +x django_start
RUN chmod +x celery_start

EXPOSE 80

ENTRYPOINT [ "./django_start" ]