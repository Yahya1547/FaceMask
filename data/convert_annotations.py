import json
import os

a_file = open("face_mask/valid/_annotations.coco.json", "r")
json_object = json.load(a_file)
a_file.close()

for image in json_object["images"] :
    filename = json_object["images"][image["id"]]["file_name"]
    split_name = filename.split("_")
    json_object["images"][image["id"]]["file_name"] = "images/" + split_name[0] + ".png"

a_file = open("face_mask/valid/_annotations.coco.json", "w")
json.dump(json_object, a_file)
a_file.close()