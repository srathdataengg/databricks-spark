# Databricks notebook source
data = [(1,"Soumyakanta"),
        (2,"Sachivji")]
schema = ["id","name"]

df = spark.createDataFrame(data,schema)

df.show()
