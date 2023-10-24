import shutil
import os, os.path

# Find the number of files in the directory PetImages/Cat and PetImages/Dog and print them
print("Number of files in PetImages/Cat:", len(os.listdir('PetImages/Cat')))
print("Number of files in PetImages/Dog:", len(os.listdir('PetImages/Dog')))

number_cat = len(os.listdir('PetImages/Cat'))
number_dog = len(os.listdir('PetImages/Dog'))

# take a random 100 images from each folder and move them to the data folder
for i in range(100):
    shutil.copy('PetImages/Cat/' + str(i+900) + '.jpg', 'data')
    shutil.copy('PetImages/Dog/' + str(i) + '.jpg', 'data')


# Find the number of files in the directory data and print it
print("Number of files in data:", len(os.listdir('data')))
