import  os
files = os.listdir()
print(files)

# os.makedirs('Images')
# os.makedirs('Docs')
# os.makedirs('Media')

#*** follow the above/below method to create a directory to store seaparte files**
def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        
def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}") 

if __name__ == "__main__":
        
    files = os.listdir()
    files.remove("5_Automatic-Folder-Cleaner.py")

    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Others')

    imgExtensions = [".png", ".jpg", ".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExtensions ]

    docExtensions = [".txt", ".docx", "doc", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExtensions]


    mediaExtensions = [".mp4", ".mp3", ".flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExtensions]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExtensions) and (ext not in docExtensions) and (ext not in imgExtensions) and os.path.isfile(file):
            others.append(file)

    move("Images", images)
    move("Docs", docs)
    move("Media", medias)
    move("Others", others)
