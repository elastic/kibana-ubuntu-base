FROM phusion/baseimage:latest
MAINTAINER Elastic Docker Team <docker@elastic.co>

RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"
RUN useradd --no-create-home --uid 1000 kibana
