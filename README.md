# PyMEOS demo for the MFS SWG

These 3 demos are intended to be run in the corresponding docker containers:
- PyMEOS demo: `diviloper/pymeos-demo:pymeos`  
  `docker run -it --rm -p 8888:8888 diviloper/pymeos-demo:pymeos`
- PyMEOS - MobilityDB demo: `diviloper/pymeos-demo:pymeos-mobilitydb`  
  ```shell
  docker network pymeos-demo-net
  docker run -d -p 5432:5432 --network pymeos-demo-net --name pymeos-demo-db mobilitydb/mobilitydb:14-3.2-develop
  docker run -it --rm -p 8888:8888 --network pymeos-demo-net diviloper/pymeos-demo:pymeos-mobilitydb 
  ```
  >To cleanup afterwards:
  >```shell
  >docker rm pymeos-demo-db
  >docker network rm pymeos-demo-net
  >``` 
- PyMEOS - MovingPandas demo: `diviloper/pymeos-demo:pymeos-movingpandas`  
  `docker run -it --rm -p 8888:8888 diviloper/pymeos-demo:pymeos-movingpandas`