from pyspark.sql.types import StructType, LongType,StringType, IntegerType, DoubleType

movieSchema = StructType()\
         .add("movieId", IntegerType(), True)\
         .add("title", StringType(), True)\
         .add("genres", StringType(), True)\
         
movieDf = spark.read.format("csv")\
          .option("header", True)\
          .schema(movieSchema)\
          .load("s3://movielens2021/movies.csv")

movieDf.show(2)
