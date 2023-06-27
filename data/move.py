import os
import shutil
import random

def duplicate_files(source_folder, destination_folder, num_duplicates):
    # Daftar file dalam folder asal
    files = os.listdir(source_folder)

    # Memilih 80 file secara acak
    selected_files = random.sample(files, num_duplicates)

    # Membuat folder tujuan jika belum ada
    os.makedirs(destination_folder, exist_ok=True)

    # Menduplikasi dan memindahkan file
    for file_name in selected_files:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.copy2(source_path, destination_path)

    print("Duplikasi dan pemindahan file dari", source_folder, "selesai.")

def iterate_subfolders(parent_folder, subfolder_name, destination_folder, num_duplicates):
    # Iterasi semua subfolder dalam folder induk
    for root, dirs, files in os.walk(parent_folder):
        for dir_name in dirs:
            if subfolder_name in dir_name:
                source_folder = os.path.join(root, dir_name)
                duplicate_files(source_folder, os.path.join(destination_folder, dir_name), num_duplicates)


# Kata yang harus ada dalam nama subfolder
subfolder_name = 'Corn'
type = "train"
# Path ke folder induk
parent_folder = os.path.join("data/Plant Disease/New Plant Diseases Dataset", type)

# Path ke folder tujuan
destination_folder = os.path.join("data/Plant Disease/Subset", subfolder_name, type)

# Jumlah file yang akan diduplikasi
num_duplicates = 10

iterate_subfolders(parent_folder, subfolder_name, destination_folder, num_duplicates)
