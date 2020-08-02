import os


files = [f for f in os.listdir("face_mask/valid/images")]

# for f in files :
#     splitted = f.split("_")
#     os.rename(r'face_mask/valid/images/' + f, r'face_mask/valid/images/' + splitted[0] + '.png')

for f in files :
    print(f)

print(len(files))