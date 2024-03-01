docker build -t IMG_NAME .
DOCKID=$(docker images -q IMG_NAME)
aws ecr-public get-login-password --region REGION_PLACE | docker login --username AWS --password-stdin URI_LINK
docker tag $DOCKID URI_LINK
docker push URI_LINK
