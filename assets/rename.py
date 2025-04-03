import os

def rename_files():
    directory = os.getcwd()
    files = os.listdir(directory)
    count = 1

    for file in files:
        if os.path.isfile(file) and file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            file_name, file_ext = os.path.splitext(file)
            if file_name.isdigit():
                continue
            new_name = str(count) + file_ext
            new_path = os.path.join(directory, new_name)
            os.rename(file, new_path)
            count += 1

rename_files()