sudo docker image pull datascientest/fastapi:1.0.0

sudo docker image build ./authentication -t authentication_test_image:latest

sudo docker image build ./authorization -t authorization_test_image:latest 
 
sudo docker image build ./score -t score_test_image:latest 

docker network create --subnet 172.50.0.0/16 --gateway 172.50.0.1 my_network

sudo docker-compose up 
