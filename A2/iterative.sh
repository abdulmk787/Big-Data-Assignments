#!/bin/sh
CONVERGE=1
ITER=1
rm v v1 log*

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
hdfs dfs -rm -r /A2/output/task-* 

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
-mapper "'/home/pes1ug19cs007/BD/A2/mapper_t1.py'" \
-reducer "'/home/pes1ug19cs007/BD/A2/reducer_t1.py' '/home/pes1ug19cs007/BD/A2/v'" \
-input /A2/input/dataset-sample.txt \
-output /A2/output/task-1-output

while [ "$CONVERGE" -ne 0 ]
do
	echo "############################# ITERATION $ITER #############################"
	hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
	-mapper "'/home/pes1ug19cs007/BD/A2/mapper_t2.py' '/home/pes1ug19cs007/BD/A2/v' '/home/pes1ug19cs007/BD/A2/embedding-sample.json'" \
	-reducer "'/home/pes1ug19cs007/BD/A2/reducer_t2.py'" \
	-input /A2/output/task-1-output/part-00000 \
	-output /A2/output/task-2-output
	touch v1
	hadoop fs -cat /A2/output/task-2-output/part-00000 > "/home/pes1ug19cs007/BD/A2/v1"
	CONVERGE=$(python3 check_conv.py $ITER>&1)
	ITER=$((ITER+1))
	hdfs dfs -rm -r /A2/output/task-2-output/
	echo $CONVERGE
done
