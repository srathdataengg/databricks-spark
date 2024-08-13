# Databricks notebook source
# DBTITLE 1,Union
americans = spark.createDataFrame([("bob",42),("lisa",38)],["firstname","age"])
columbians = spark.createDataFrame([("maria",20),("camilo",31)],["firstname","age"])
res = americans.union(columbians)
res.show()
