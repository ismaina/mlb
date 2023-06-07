#! /bin/bash

if [ -z "$ec2_IP_ADDRESS" ]
then
    echo "ec2_IP_ADDRESS not defined"
    exit 0
fi

git archive --format tar --output ./mlb.tar aws

echo "Uploading the mlb.....:-)...Be Patient!"
rsync -av -e "ssh -i ~/.ssh/Maina.pem" ./mlb.tar ubuntu@$ec2_IP_ADDRESS:/home/ubuntu/Documents/mlb.tar
# rsync -avzhe ssh --progress ./mlb.tar mwanjau@$ec2_IP_ADDRESS:/home/mwanjau/tracker/mlb.tar
echo "Upload complete....:-)"


echo "Building the image......."
# ssh mwanjau@$ec2_IP_ADDRESS << 'ENDSSH'
ssh -i ~/.ssh/Maina.pem ubuntu@$ec2_IP_ADDRESS << 'ENDSSH'
    cd Documents
    mkdir -p mlb
    rm -rf mlb/* && tar -xf mlb.tar -C mlb/
    cd mlb
    docker-compose -f local.yml build
ENDSSH
echo "Build completed successfully.......:-)"