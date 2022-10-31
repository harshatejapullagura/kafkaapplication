<h2>   <font size="6"
          face="arial"
          color="#008000">Topics In Distributed Computing CECS 574 Final Project
    </font> </h2>
<font size="20"
          face="arial"
          color="#87CEEB"> Team Messengers
    </font>

Steps to Run the project 

1) Install zookeeper (download )
2) Install kafka (download )
3) Run zookeeper and kafka server in local machine

Commands used for step 3 marked with -- (paths according to my installation:

    --start zoo : .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
    --start kafka : .\bin\windows\kafka-server-start.bat .\config\server.properties
    create a topic : >.\bin\windows\kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic TestTopic
    stopzoo keeper server : .\bin\windows\zookeeper-server-stop.bat
    stopkafka server : .\bin\windows\kafka-server-stop.bat
    list_brokers : .\bin\windows\kafka-topics.bat --list --zookeeper localhost:2
4) Start zookeeper (must see logs in cmd)
5) Start kafka 
6) Run producer
7) Run consumer
8) Check logs msgs sent in producer should be visible in consumer