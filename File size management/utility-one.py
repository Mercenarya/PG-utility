import os


path = os.path.dirname(os.path.abspath(__file__))
print(path)

target_file = 'TempPath'

def Search(value):
    if os.path.exists(value):
        return os.listdir(value)

    else:
        return False

def List_File(value):

    File_Tubs = []
    try:
        Column = os.listdir(value)
        File_Tubs.append(Column)
        for file in range(len(File_Tubs)):
            return File_Tubs[file]

    except Exception as error:
        return error
    

if __name__ == '__main__':
    print("Search Result: ",Search(path))
    print(List_File(path))