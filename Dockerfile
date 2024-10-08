# pull official base image
FROM python:3.9-slim-bullseye
LABEL maintainer="Adeleke Femi"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# install necessary packages
RUN apt-get update && \
    apt-get -y install gcc && \
    rm -rf /var/lib/apt/lists/*
    
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev

# set the working directory
WORKDIR /app

# copy the source code
COPY . /app/

# install pip project dependencies
RUN pip install --upgrade pip && \
    pip install --trusted-host pypi.python.org -r requirements.txt


# expose ports
EXPOSE 3020



# set the command to run when the container starts
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
