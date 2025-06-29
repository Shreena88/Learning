import os
import shutil
from pathlib import Path

#Define file type category
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt",".pptx",".xlsx"],
    "Videos": [".mp4",".mov",".avi",".mkv"],
    "Audio": [".mp3",".wav",".aac"],
    "Archives": [".zip",".rar",".7z",".tar",".gz"],
    "Scripts": [".py",".js",".html",".css",".java",".c",".cpp"]
}

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("The provided path is not valid")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = Path(file_path).suffix.lower()
            moved = False
            for category, extensions in file_categories.items():
                if ext in extensions:
                    category_folder = os.path.join(folder_path,category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path,os.path.join(category_folder,filename))
                    moved = True
                    print(f"Moved : {filename} -> {category}")
                    break

            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path,os.path.join(other_folder,filename))
                print(f"Moved : {filename} -> Others")

def main():
    folder = input("Enter the path of the folder to organize:").strip()
    organize_files(folder)
    print("Organization Complete!")

if __name__ == "__main__":
    main()