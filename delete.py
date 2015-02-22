#!/usr/bin/python

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App:)
sc = SparkContext(conf=conf)

if __name__ == "__main__":
   print 'NICE'

