# Final Project - GEOG 790
# Megan Ladany

import arcpy
import numpy

arcpy.env.workspace = r"C:\Users\meganladany\PycharmProjects\Final\McCroryGardensProject\McCroryGardensProject.gdb"


def getPlantType(table, field):
    data = arcpy.da.TableToNumPyArray(table, [field])
    return numpy.unique(data[field]).tolist()


plantList = getPlantType("Plant_Name_Shapefile", "TxtMemo")

index = 0
while index < len(plantList):
    try:
        int(plantList[index])
        del plantList[index]
    except ValueError:
        index += 1

print(plantList)
print(len(plantList))
