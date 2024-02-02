from zipfile import ZipFile

# with open("my_journal.txt", "w") as f:
#     f.write('alguns dados')
#
# with ZipFile("archive.zip", mode="w") as archive:
#     archive.write("my_journal.txt")
#     archive.printdir()

# with ZipFile("archive.zip") as archive:
#     with archive.open("output.txt") as f:
#         print(f.read().decode())

with ZipFile("archive.zip") as archive:
    if "logs.txt" not in archive.namelist():
        print("The file 'logs.txt' does not exist in the archive.")
        exit(1)
