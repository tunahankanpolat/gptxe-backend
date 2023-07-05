#!/bin/bash

DOCKER_IMAGE_NAME="gptxe"
DOCKER_IMAGE_TAG="latest"
DOCKER_CONTANINER_NAME="gptxe-backend"

AWS_ACCOUNT_ID="988414464535"
AWS_REGION="eu-central-1"
ECR_REPOSITORY="${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${DOCKER_IMAGE_NAME}"

check_and_update_image() {
    echo "Checking Docker image: ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}"
    old_image_id=$(docker images --format "{{.ID}}" "${ECR_REPOSITORY}:${DOCKER_IMAGE_TAG}")

    echo "Pulling Docker image..."
    docker pull "${ECR_REPOSITORY}:${DOCKER_IMAGE_TAG}"

    new_image_id=$(docker images --format "{{.ID}}" "${ECR_REPOSITORY}:${DOCKER_IMAGE_TAG}")

    if [[ "$old_image_id" != "$new_image_id" ]]; then
        echo "Updated Docker image. Deleting old container..."
        docker stop ${DOCKER_CONTANINER_NAME}
        docker rm ${DOCKER_CONTANINER_NAME}

        echo "Running new Docker image..."
        docker run -d --name ${DOCKER_CONTANINER_NAME} -p 5000:5000 "${new_image_id}"
    else
        echo "The current Docker image is up to date. No action taken."
    fi
}

check_interval_seconds=3600 
while true; do
    aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
    check_and_update_image
    sleep "$check_interval_seconds"
done
