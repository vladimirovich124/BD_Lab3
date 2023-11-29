containers=("apache-hadoop-nodemanager-1" "apache-hadoop-datanode-1" "apache-hadoop-resourcemanager-1" "apache-hadoop-namenode-1")

for container in "${containers[@]}"; do
    echo "Installing Python 3 on $container..."

    docker exec -t "$container" sudo yum install -y python3

    docker exec -i "$container" echo "y" | sudo yum install -y python3

    echo "Python 3 installed on $container."
done

echo "Installing mrjob on apache-hadoop-namenode-1..."
docker exec -t "apache-hadoop-namenode-1" sudo pip3 install mrjob
echo "mrjob installed on apache-hadoop-namenode-1."

echo "Copying file to HDFS on apache-hadoop-namenode-1..."
docker exec -t "apache-hadoop-namenode-1" hdfs dfs -put /my_volume/dataset/flights.csv /
echo "File copied to HDFS on apache-hadoop-namenode-1."
