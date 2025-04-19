FROM amazonlinux:2023
RUN mkdir /srv1
WORKDIR /srv1
RUN echo {"server_port":80} > /srv1/config.json
COPY server.zip /srv1
RUN yum install -y unzip
RUN unzip /srv1/server.zip
RUN chmod +x /srv1/server1
CMD ["/srv1/server1"]
