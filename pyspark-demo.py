from pyspark import SparkConf
from pyspark import SparkContext
import os

conf = SparkConf()
conf.setAppName('spark-wordcount_from172.16.2.118')
sc.stop()
sc = SparkContext(conf=conf)
distFile = sc.textFile('hdfs://hacluster/tmp/airlines.csv')
nonempty_lines = distFile.filter(lambda x: len(x) > 0)
print 'Nonempty lines', nonempty_lines.count()
words = nonempty_lines.flatMap(lambda x: x.split(' '))
wordcounts = words.map(lambda x: (x, 1)) \
.reduceByKey(lambda x, y: x+y) \
.map(lambda x: (x[1], x[0])).sortByKey(False)
print 'Top 100 words:'
print wordcounts.take(100)
