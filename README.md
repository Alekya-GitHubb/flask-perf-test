\# Flask Performance Test



This repository contains a simple \*\*Flask application\*\* used to compare performance between two environments:



1\. \*\*Docker container\*\*  

2\. \*\*Virtual Machine (VM)\*\* using Vagrant and VirtualBox  



The goal is to benchmark startup time, CPU usage, memory usage, and throughput to highlight differences between containerization and virtualization.



---





\## Run with Docker

Build and start the container:

```bash

docker build -t flask-perf-test .

docker run -p 5001:5000 flask-perf-test

The application will be available at:

http://127.0.0.1:5001/health





\## Run with Docker

vagrant up

vagrant ssh

cd /vagrant

python3 app.py



The application will be available at:

http://127.0.0.1:5000/health



---



\### Project Structure



flask-perf-test/

│── app.py           # Flask application

│── requirements.txt # Dependencies

│── Dockerfile       # Docker container definition

│── Vagrantfile      # Vagrant VM definition

│── test.sh          # Basic test script for container

│── REPORT.md        # Full performance comparison report

│── screenshots/     # Benchmark screenshots (used in REPORT.md)



----



\#### Report



The full performance comparison (with results, tables, and screenshots) is available here:

 REPORT.md



" " 
