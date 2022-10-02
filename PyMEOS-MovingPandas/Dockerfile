FROM python:3.8-bullseye

RUN apt update
RUN apt install -y libgeos-dev


RUN git clone --branch demo https://github.com/MobilityDB/MobilityPandas.git

RUN pip install pymeos matplotlib jupyter movingpandas rtree
RUN pip uninstall -y movingpandas

WORKDIR /pymeos-demo
COPY PyMEOS-MovingPandas.ipynb /pymeos-demo/
COPY aisinput.csv /pymeos-demo/

EXPOSE 8888

ENTRYPOINT [ "jupyter", "notebook", "--allow-root", "--ip=0.0.0.0"]