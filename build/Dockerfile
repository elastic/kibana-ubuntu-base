FROM phusion/baseimage:latest
MAINTAINER Elastic Docker Team <docker@elastic.co>

RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \
    apt-get install -y --no-install-recommends moreutils net-tools patch libfontconfig libfreetype6 && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN useradd --no-create-home --uid 1000 kibana
