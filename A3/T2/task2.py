from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import max
import sys

city_path= sys.argv[1]
global_path = sys.argv[2]

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)


dfc=sqlContext.read.format("csv").option("header","true").load(city_path)

dfg=sqlContext.read.format("csv").option("header","true").load(global_path)

dfc2= dfc.select("dt", "Country", "AverageTemperature").withColumn("AverageTemperature",dfc["AverageTemperature"].cast('float'))


dfc3= dfc2.groupBy( "dt", "Country").agg(max("AverageTemperature")).withColumnRenamed("max(AverageTemperature)", "mavgt")
dfc31= dfc3.join(dfg, ["dt"]).withColumn("LandAverageTemperature",dfg["LandAverageTemperature"].cast('float'))
dfc4= dfc31.filter( dfc3.mavgt > dfg.LandAverageTemperature )

dfc5= dfc4.groupby("Country").count().sort('Country', ascending=True)

res= dfc5.collect()


for row in res:
    print(row['Country'] + "\t" +str(row['count']))
