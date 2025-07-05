# Docker-container-which-runners-MySQL-Server-using-python
Using docker to create a container which runners MySQL server using python.

                                                Overview 

Creating a MSQL server using python on a Docker container 

1) Create a app.py file code using python

2) Create a Dockerfile to create or run the image and writing all the requirment

3) Create a Requirement file for FLASH requirement.

4) To run this image start with build a container (mysql-container)
          1) command - docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=example -e MYSQL_DATABASE=testdb -p 3306:3306 -d mysql:8.0

     To check the log file the container
   1) docker ps
   2) docker logs mysql-container

Command:-
1) After Create the container time to build the Dockert image - docker build -t flask-mysql-app .
2) docker run --name flask-app --network flasknet -p 5000:5000 flask-mysql-app



.....................................................................................Enjoy the code........................................................................................

TO Run http://localhost:5000 
       

