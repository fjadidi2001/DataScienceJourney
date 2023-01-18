# Python program to extract text from all the images in a folder
# storing the text in corresponding files in a different folder
from PIL import Image
import pytesseract as pt
import os


def main():
    # path for the folder for getting the raw images
    path = "E:\\GeeksforGeeks\\images"

    # path for the folder for getting the output
    tempPath = "E:\\GeeksforGeeks\\textFiles"

    # iterating the images inside the folder
    for imageName in os.listdir(path):
        inputPath = os.path.join(path, imageName)
        img = Image.open(inputPath)

        # applying ocr using pytesseract for python
        text = pt.image_to_string(img, lang="eng")

        # for removing the .jpg from the imagePath
        imagePath = imagePath[0:-4]

        fullTempPath = os.path.join(tempPath, 'time_' + imageName + ".txt")
        print(text)

        # saving the  text for every image in a separate .txt file
        file1 = open(fullTempPath, "w")
        file1.write(text)
        file1.close()


if __name__ == '__main__':
    main()