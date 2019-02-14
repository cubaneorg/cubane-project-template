FROM python:2.7

# install initial requirements
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y apt-utils
RUN apt-get install -y openjdk-8-jre
RUN apt-get install -y python-psycopg2
RUN apt-get install -y libmagickwand-dev
RUN apt-get install -y ghostscript
RUN apt-get install -y libjpeg-turbo-progs
RUN apt-get install -y optipng
RUN apt-get install -y net-tools
RUN apt-get install -y git
RUN apt-get install -y vim
RUN apt-get install -y postgresql
RUN apt-get install -y rsync

# setup locales
RUN sed -i -e 's/# en_GB.UTF-8 UTF-8/en_GB.UTF-8 UTF-8/' /etc/locale.gen && locale-gen
ENV LANG en_GB.UTF-8
ENV LANGUAGE en_GB:en
ENV LC_ALL en_GB.UTF-8

# create app folder
RUN mkdir /app
WORKDIR /app
COPY . /app/

# create cubane folder
WORKDIR /
RUN git clone https://github.com/cubaneorg/cubane.git
RUN git checkout develop

# switch working folder
WORKDIR /app

# install python dependencies
RUN pip install -r /cubane/cubane/requirements/dev.txt
RUN pip install -r /app/requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
