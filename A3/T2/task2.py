from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import max
import sys

city_path= "./city_sample_5percent.csv"
global_path = "./global.csv"

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)


dfc=sqlContext.read.format("csv").option("header","true").load(city_path)

dfg=sqlContext.read.format("csv").option("header","true").load(global_path)

dfc2= dfc.select("dt", "Country", "City", "AverageTemperature")


dfc3= dfc2.groupBy("dt", "Country", "City").agg(max("AverageTemperature")).withColumnRenamed("max(AverageTemperature)", "mavgt")
dfc4= dfc3.join(dfg, ["dt"]).filter( dfc3.mavgt > dfg.LandAverageTemperature )

dfc5= dfc3.join(dfg, ["dt"]).filter( dfc3.mavgt > dfg.LandAverageTemperature ).groupby("Country").count().sort('Country', ascending=True)

res= dfc5.collect()


for row in res:
    print(row['Country'] + "\t" +str(row['count']))
