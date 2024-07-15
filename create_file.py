def create_file():
    with open("file_to_upload.txt", "w") as file:
        file.write("Hello world!")
    file = "file_to_upload.txt"
    return file