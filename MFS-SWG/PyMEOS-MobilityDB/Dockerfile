FROM python:3.8-bullseye


RUN apt update
RUN apt-get -y install wget ca-certificates lsb-release
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
RUN apt update

RUN apt search postgresql
RUN apt install -y postgresql-client-14
RUN pip install pymeos matplotlib jupyter psycopg2

WORKDIR /pymeos-demo
COPY PyMEOS-MobilityDB.ipynb /pymeos-demo/
COPY trips.csv /pymeos-demo/
COPY load_db.py /pymeos-demo/

COPY demo-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/demo-entrypoint.sh

EXPOSE 8888

ENTRYPOINT ["demo-entrypoint.sh"]