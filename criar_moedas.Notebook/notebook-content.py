# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "e503449a-6ef8-4ab1-a386-0520fdbd8e9a",
# META       "default_lakehouse_name": "lake",
# META       "default_lakehouse_workspace_id": "ec2b121d-1b95-42ed-a21c-c5f4ec9dc2db",
# META       "known_lakehouses": [
# META         {
# META           "id": "e503449a-6ef8-4ab1-a386-0520fdbd8e9a"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Importação de bibliiotecas
from pyspark.sql.types import StructType, StructField, StringType

# Criação do schema do dataframe
schema = StructType([
    StructField("Moeda", StringType(), True),
    StructField("Nome", StringType(), True),
    StructField("Formato", StringType(), True)
])

# Dados das moedas
data = [
    ("BRL", "Real brasileiro",          "R$ #,##0.00;R$ #,##0.00;-" ),
    ("AUD", "Dólar australiano",        "$ #,##0.00;$ #,##0.00;-"   ),
    ("CAD", "Dólar canadense",          "$ #,##0.00;$ #,##0.00;-"   ),
    ("CHF", "Franco suíço",             "Fr #,##0.00;Fr #,##0.00;-" ),
    ("DKK", "Coroa dinamarquesa",       "kr #,##0.00;kr #,##0.00;-" ),
    ("EUR", "Euro",                     "€ #,##0.00;€ #,##0.00;-"   ),
    ("GBP", "Libra Esterlina",          "£ #,##0.00;£ #,##0.00;-"   ),
    ("JPY", "Iene",                     "¥ #,##0;¥ #,##0;-"         ),
    ("NOK", "Coroa norueguesa",         "kr #,##0.00;kr #,##0.00;-" ),
    ("SEK", "Coroa sueca",              "kr #,##0.00;kr #,##0.00;-" ),
    ("USD", "Dólar dos Estados Unidos", "$ #,##0.00;$ #,##0.00;-"   )
]

# Criando o DataFrame
df = spark.createDataFrame(data, schema=schema)

# Exibindo o dataframe
# df.show()
# df.printSchema()

# Escrevendo no lakehouse
df.write.format("delta").mode("overwrite").saveAsTable("moedas")

# Exibindo o dataframe do lakehouse
df_lake = spark.sql("SELECT * FROM lake.moedas")
display(df_lake)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
