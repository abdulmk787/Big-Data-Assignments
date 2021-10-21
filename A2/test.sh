rm v v1 log*

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
hdfs dfs -rm -r /A2/output/task-* 

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
-mapper "'/home/pes1ug19cs007/BD/A2/T1/mapper.py'" \
-reducer "'/home/pes1ug19cs007/BD/A2/T1/reducer.py' '/home/pes1ug19cs007/BD/A2/v'" \
-input /A2/input/dataset-sample2.txt \
-output /A2/output/task-1-output

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
	-mapper "'/home/pes1ug19cs007/BD/A2/T2/mapper.py' '/home/pes1ug19cs007/BD/A2/v' '/home/pes1ug19cs007/BD/A2/embedding-sample2.json'" \
	-reducer "'/home/pes1ug19cs007/BD/A2/T2/reducer.py'" \
	-input /A2/output/task-1-output/part-00000 \
	-output /A2/output/task-2-output
	touch v1
	hadoop fs -cat /A2/output/task-2-output/part-00000 > "/home/pes1ug19cs007/BD/A2/v1"