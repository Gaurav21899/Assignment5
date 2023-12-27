import arcpy
import os

gdb_path = r"D:\Programming for GIS-3\Assignment5\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = "MajorAttractions"
fc_path = os.path.join(gdb_path, fc_name)

# Creating a list of fields to be used in search cursor
fields_list = ["Name", "ADDR"]

with arcpy.da.SearchCursor(fc_path, fields_list) as s_cursor:
    for row in s_cursor:
        print("MajorAttraction {}, was {}".format(row[0], row[1]))

print("Process Completed")




