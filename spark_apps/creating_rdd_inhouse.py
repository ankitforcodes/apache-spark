from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("CreatingInhouseRDD")
sc = SparkContext(conf = conf)

rdd = sc.parallelize(["Ankit", "Sahay"])
print(rdd.count())