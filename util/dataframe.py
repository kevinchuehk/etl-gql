import pyspark
import json
from os import getenv
from nanoid import generate
from graphene import ObjectType, String

class DataFrame(ObjectType):
    __master = getenv('SPARK_MASTER', 'local')

    def __init__(self):
        self.__spark = SparkSession.builder
            .master(__master)
            .appName(generate())
            .getOrCreate()

    def __del__(self):
        self.__spark.stop()