#! /bin/bash

if [ -z "$ec2_IP_ADDRESS" ]
then
    echo "ec2_IP_ADDRESS not defined"
    exit 0
fi

git archive --format tar --output ./project.tar prod

echo "Uploading the project.....:-)...Be Patient!"
rsync -av -e "ssh -i ~/.ssh/MainaEC2KP.pem" ./project.tar ec2-user@$ec2_IP_ADDRESS:/home/ec2-user/project.tar
# rsync -avzhe ssh --progress ./project.tar mwanjau@$ec2_IP_ADDRESS:/home/mwanjau/tracker/project.tar
echo "Upload complete....:-)"


echo "Building the image......."
# ssh -i .ssh/MainaEC2KP.pem ec2-user@$ec2_IP_ADDRESS << 'ENDSSH'
ssh mwanjau@$ec2_IP_ADDRESS << 'ENDSSH'
    mkdir -p /thkisilon_container_nfs/tracker
    rm -rf /thkisilon_container_nfs/tracker/* && tar -xf tracker/project.tar -C /thkisilon_container_nfs/tracker/
    docker-compose -f /thkisilon_container_nfs/tracker/production.yml build
ENDSSH
echo "Build completed successfully.......:-)"