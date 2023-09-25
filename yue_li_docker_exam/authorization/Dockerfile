FROM ubuntu:18.04

ENV LOG=1
# Update package list, upgrade installed packages, and install pip3
RUN apt-get update && apt-get upgrade -y && apt-get install -y python3-pip

RUN mkdir -p /home/yue_li/authorization
RUN mkdir /home/yue_li/logs
# Install the requests library using pip3
RUN pip3 install requests

# Clean up the package cache to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["python3", "/home/yue_li/authorization/authorization.py"]
