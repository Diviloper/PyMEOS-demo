FROM python:3.8-bullseye

RUN pip install pymeos matplotlib jupyter

WORKDIR /pymeos-demo
COPY PyMEOS.ipynb /pymeos-demo/
COPY trips.csv /pymeos-demo/

EXPOSE 8888

ENTRYPOINT [ "jupyter", "notebook", "--allow-root", "--ip=0.0.0.0"]