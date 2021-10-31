from pyspark import SparkContext
from pyspark.sql import SQLContext
import sys

country_name= sys.argv[1]
filepath = sys.argv[2]

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)


df=sqlContext.read.format("csv").option("header","true").load(filepath)

df2 = df.withColumn("AverageTemperature",df["AverageTemperature"].cast('float'))

df3=df2[df2.Country.isin(country_name)].groupby('City').mean('AverageTemperature').withColumnRenamed("avg(AverageTemperature)", "tavg")

df4= df2.join(df3, ["City"])

df5 =df4.filter( df4.AverageTemperature > df4.tavg).groupby('City').count().sort('City', ascending=True)
res= df5.select("City", "count").collect()


for row in res:
    print(row['City'] + "\t" +str(row['count']))

