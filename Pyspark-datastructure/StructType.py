# Databricks notebook source
data = [(1,"Soumyakanta"),
        (2,"Sachivji")]
schema = ["id","name"]

df = spark.createDataFrame(data,schema)

df.show()

# COMMAND ----------

from pyspark.sql.types import *

data = [{'id':1,'name':'Soumyakanta'},{'id':2,'name':'soumyakanta'}]
df = spark.createDataFrame(data)
df.show(truncate=False)
df.printSchema()

# COMMAND ----------

from pyspark.sql.types import StructField,StructType,IntegerType,StringType

data = [{'id':1,'name':'sachivji'},{'id':2,'name':'pradhanji'}]
schema = StructType([
    StructField(name='id',dataType=IntegerType()),
    StructField(name='name',dataType=StringType())
])

df = spark.createDataFrame(data= data,schema=schema)

display(df)

