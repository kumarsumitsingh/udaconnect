#!/bin/sh
 
# update advertised listener so clients can call the container from outside
 #sed -i '1 a listeners=PLAINTEXT://0.0.0.0:9092' 
 #$KAFKA_HOME/config/server.properties
 
#sed -i '1 a advertised.listeners=PLAINTEXT://localhost:9092' 
#$KAFKA_HOME/config/server.properties
 
# start zookeeper
$KAFKA_HOME/bin/zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties &
 
# start kafka broker
$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties &

# create topic "location"
$KAFKA_HOME/bin/kafka-topics.sh --create  --topic producer  --bootstrap-server localhost:9092

# restart kafka broker
$KAFKA_HOME/bin/kafka-server-stop.sh
$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties
