#file system organiser
def group_by_extension(files):
    result = {}              #Turns the values into list
    for file in files:
        file = file.strip()
        name, ext = file.rsplit('.', 1)
        if ext not in result:
            result[ext] = []
        result[ext].append(file)
    return result

files = [" script.py", " notes.txt", " data.csv", " main.py", " image.png", " list.txt"]

output = group_by_extension(files)
print(output)