import arcpy
import os

gdb_path = r"D:\Programming for GIS-3\Ass\Assignment5\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = "MajorAttractions"
fc_path = os.path.join(gdb_path, fc_name)
fields_list = ["SHAPE@X", "SHAPE@Y"]

with arcpy.da.SearchCursor(fc_path, fields_list) as s_cursor:
    for row in s_cursor:
        x = row[0]
        y = row[1]
        print("X: {}, Y: {}".format(x, y))

print("Process Completed")


