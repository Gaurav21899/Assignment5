import arcpy
import os

gdb_path = r"D:\Programming for GIS-3\Assignment5\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = 'MajorAttractions'
fc_path = os.path.join(gdb_path, fc_name)

fields_list = ["ESTAB", "NAME"]

# Create a list to store the names of Major Attractions established after 1970
major_attractions_after_1970 = []

with arcpy.da.SearchCursor(fc_path, fields_list) as s_cursor:
    for row in s_cursor:
        estab = row[0]
        if estab > 1970:
            major_attractions_after_1970.append(row[1])

for name in major_attractions_after_1970:
    print(name)

print("Process Completed")



