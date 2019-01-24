# Set the base image to Ubuntu
FROM ubuntu:14.04

# File Author / Maintainer
MAINTAINER Kristian Aspevik

# Update the default application repository sources list
RUN apt-get update && apt-get install -y \
    python3-dev \
    python3 \
    python3-pip \
    python3-setuptools \
    build-essential \
    git

# Set variables for project name, and where to place files in container.
ENV PROJECT=kristianaspevik
ENV CONTAINER_HOME=/opt/kristian
ENV CONTAINER_PROJECT=$CONTAINER_HOME/$PROJECT

# Create application subdirectories
WORKDIR $CONTAINER_HOME
RUN mkdir -p /var/log/kristianaspevik

# Copy application source code to $CONTAINER_PROJECT
COPY . $CONTAINER_PROJECT

# Install Python dependencies
RUN pip3 install -r $CONTAINER_PROJECT/requirements.txt
RUN pip3 install gunicorn

# Copy and set entrypoint
WORKDIR $CONTAINER_PROJECT
COPY ./dockerfiles/django/entrypoint.sh $CONTAINER_PROJECT/
RUN chmod +x $CONTAINER_PROJECT/entrypoint.sh
ENTRYPOINT ["bash", "entrypoint.sh"]
