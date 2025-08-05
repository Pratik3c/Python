from pathlib import Path
import os

def presentFiles():
  path = Path('')
  items = list(path.rglob('*'))
  for i,items in enumerate(items):
    print(f"{i+1} : {items}")


def createFile():
  try:
    presentFiles()
    name = input("Enter the name of file u want to create: ")
    p = Path(name)

    if not p.exists():
      with open(p,"w") as fs:
        data = input("What data u want to insert : ")
        fs.write(data)

        print("FILE CREATED SUCCESSFULLY !!!")
    else:
      print("This named file already exists")

  except Exception as ex:
    print(f"An exception occured : {ex}")


def readFile():
  try:
    presentFiles()
    name = input("Which file u want to read:- ")
    p = Path(name)

    if p.exists() and p.is_file():
      with open(p,"r") as fs:
        data = fs.read()
        print(data)
      
      print("Readed Successfully")
    else:
      print("This file does not exist")
  
  except Exception as ex:
    print(f"An exception occured : {ex}")


def deleteFile():
  try:
    presentFiles()
    name = input("Which file u want to delete : ")
    p = Path(name)

    if p.exists() and p.is_file():
      os.remove(name)
    else:
      print("THis file does not exist")

  except Exception as ex:
    print(f"An exception occured : {ex}")


def updateFile():
  try:
    presentFiles()
    name = input("Which file u want ot update:- ")
    p = Path(name)

    if p.exists() and p.is_file():
      print("Press 1 to rename the file")
      print("Press 2 to overwrite in the file")
      print("Press 3 to append new content in the file")

      response = int(input("Choose the operation : "))

      if response == 1:
        new_name = input("Enter the new name of file: ")
        new_p = Path(new_name)

        p.rename(new_p)

      if response == 2:
        with open(p,"w") as fs:
          data = input("Input the data to over write: ")
          fs.write(data)

      if response == 3:
        with open(p,"a") as fs:
          data = input("Input the data u want to append: ")
          fs.write(" "+data)

  except Exception as ex:
    print(f"An exception occured : {ex}")

check=0
while(check != 5):
  print("Press 1 to creating file")
  print("Press 2 to reading file")
  print("Press 3 to updating file")
  print("Press 4 to delete file")
  print("Press 5 to EXIT")

  check = int(input("Choose the option u want to perform:- "))

  if check == 1:
    createFile()

  if check == 2:
    readFile()

  if check == 3:
    updateFile()

  if check == 4:
    deleteFile()