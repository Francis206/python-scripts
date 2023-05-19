# IT 280 - Lab #10: File Compression Instructions by Francis @ 2022

from pathlib import Path
from zipfile import ZipFile


def main():
    files = ['./value1.txt', './value2.txt']
    path = Path('./zip', 'all_files.zip')

    if path.parent.exists() is False:
        path.parent.mkdir()

    with ZipFile(path, 'w') as zip:
        for file in files:
            if Path(file).exists:
                zip.write(file)


main()
