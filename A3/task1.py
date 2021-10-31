from pyspark import SparkContext
from pyspark.sql import SQLContext
import sys

country_name= sys.argv[1]
filepath = sys.argv[2]

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)


df=sqlContext.read.format("csv").option("header","true").load(filepath)

df2 = df.withColumn("AverageTemperature",df["AverageTemperature"].cast('float'))

dfp=df2.filter(df2.Country == country_name)

df3=dfp.groupby('City').avg('AverageTemperature').withColumnRenamed("avg(AverageTemperature)", "tavg")

df4= dfp.join(df3, ["City"])

df5 =df4.filter( df4.AverageTemperature > df4.tavg).groupby('City').count().sort('City', ascending=True)
res= df5.select("City", "count").collect()


for row in res:
    print(row['City'] + "\t" +str(row['count']))
