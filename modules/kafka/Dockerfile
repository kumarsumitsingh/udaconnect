FROM openjdk:8-jdk-alpine3.9
 
ENV KAFKA_HOME /usr/local/kafka
ADD ./start-kafka.sh /scripts/
RUN chmod u+x -R /scripts/
RUN chmod u+x -R /usr/
#RUN chmod u+x -R /usr/local/kafka/

WORKDIR .
# install utils
RUN apk add wget --no-cache curl tar bash procps

# install kafka
RUN wget https://ftp.wayne.edu/apache/kafka/3.2.3/kafka_2.13-3.2.3.tgz && \
tar -xzf kafka_2.13-3.2.3.tgz && \
mv kafka_2.13-3.2.3 $KAFKA_HOME
RUN chmod u+x -R /usr/local/kafka/
EXPOSE 9092
ENTRYPOINT ["/scripts/start-kafka.sh"]