from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("ReadFIleAndFilter")
sc = SparkContext(conf = conf)

readlines = sc.textFile("../README.md")
lines_with_python = readlines.filter(lambda line: "Spark" in line)
first_line = lines_with_python.first()
print(first_line)