\# Performance Comparison: Virtual Machine vs Docker Container



\## Introduction

This project evaluates the performance of a simple Flask application running in two different environments:  

1\. A Virtual Machine (VM) using Vagrant and VirtualBox  

2\. A Docker container  



The goal is to compare startup time, CPU usage, memory usage, and request throughput, in order to understand the trade-offs between containers and virtual machines.



---



\## Methodology



\- \*\*Application\*\*: Flask app with `/health`, `/users`, and `/products` endpoints, preloaded data (no database required).  

\- \*\*VM Setup\*\*: Vagrant with VirtualBox (Ubuntu 20.04, 2 CPUs, 1 GB RAM).  

\- \*\*Docker Setup\*\*: Docker image built using the provided `Dockerfile`.  

\- \*\*Tools Used\*\*:

&nbsp; - `Measure-Command` in PowerShell and `time` in Linux to measure startup time.  

&nbsp; - `docker stats` and Docker Desktop for container CPU/memory usage.  

&nbsp; -  VirtualBox resource monitor for VM CPU/memory usage.  

&nbsp; - `ab (ApacheBench)` for throughput (requests/sec) and response times.  



---



\## Results



\### Startup Time

\- Docker: ~0.60 seconds  

\- VM: ~14.12 seconds  



\### CPU Usage

\- Docker: ~0.17%  

\- VM: ~1–2%  



\### Memory Usage

\- Docker: ~45 MB  

\- VM: ~215 MB  



\### Throughput (ApacheBench)

\- Docker: ~214 requests/second, average response time ~233 ms  

\- VM: ~209 requests/second, average response time ~239 ms  



---



\## Comparison Table



| Metric               | Docker (Container)         | VM (Vagrant + VirtualBox)  |

|----------------------|----------------------------|-----------------------------|

| Startup Time         | ~0.60 seconds              | ~14.12 seconds              |

| CPU Usage            | ~0.17%                     | ~1–2%                       |

| Memory Usage         | ~45 MB                     | ~215 MB                     |

| Requests/sec (AB)    | ~214                       | ~209                        |

| Avg. Response Time   | ~233 ms                    | ~239 ms                     |

| Failed Requests      | 0                          | 0                           |



---



\## Screenshots



\### Startup Time

\- Docker (~0.60 s)  

!\[Docker startup](screenshots/docker-startup.png)



\- VM (~14.12 s)  

!\[VM startup](screenshots/vm-startup.png)



\### CPU and Memory Usage

\- Docker stats (~0.17% CPU, ~45 MB RAM)  

!\[docker stats CLI](screenshots/docker-stats-cli.png)  

!\[docker stats desktop](screenshots/docker-stats-desktop.png)



\- VM resource usage (~1–2% CPU, ~215 MB RAM)  

!\[VM resource use](screenshots/vm-resource-use.png)



\### Load Test Results

\- Docker (Requests/sec ≈ 214, Avg ≈ 233 ms)  

!\[ab docker](screenshots/ab-docker.png)



\- VM (Requests/sec ≈ 209, Avg ≈ 239 ms)  

!\[ab vm](screenshots/ab-vm.png)



---



\## Analysis



\- \*\*Startup Time\*\*: Docker containers start significantly faster than VMs.  

\- \*\*Resource Usage\*\*: Docker shows lower CPU and memory overhead compared to VMs.  

\- \*\*Throughput\*\*: Both environments perform well under load, with Docker showing slightly higher requests per second and lower response times.  

\- \*\*Reliability\*\*: No failed requests in either setup, showing both environments are stable for this workload.  



---



\## Conclusion



\- Docker provides faster startup, lower resource usage, and slightly better throughput compared to VMs.  

\- Virtual Machines, however, offer stronger OS-level isolation and are useful for simulating complete hardware or operating system environments.  

\- For lightweight microservices and scalable applications, Docker containers are generally the better choice.  



