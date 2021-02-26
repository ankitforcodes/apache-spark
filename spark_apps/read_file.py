from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

readlines = sc.textFile("../README.md")
num_of_lines = readlines.count()
print(num_of_lines)