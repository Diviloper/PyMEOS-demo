# PyMEOS demo for the MFS SWG

These 3 demos are intended to be run in the corresponding docker containers:
- PyMEOS demo: `pymeos-demo/pymeos`  
  `docker run -it --rm -p 8888:8888 pymeos-demo/pymeos`
- PyMEOS - MobilityDB demo: `pymeos-demo/pymeos-mobilitydb`  
  ```shell
  docker network pymeos-demo-net
  docker run -d -p 5432:5432 --network pymeos-demo-net mobilitydb/mobilitydb:14-3.2-develop
  docker run -it --rm -p 8888:8888 --network pymeos-demo-net pymeos-demo/pymeos-mobilitydb 
  ```
- PyMEOS - MovingPandas demo: `pymeos-demo/pymeos-movingpandas`
  `docker run -it --rm -p 8888:8888 pymeos-demo/pymeos-movingpandas`