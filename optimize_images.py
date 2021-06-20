from PIL import Image
import os

def compress_images(directory=False,outputPath="",quality=1):
    # 1. If there is a directory then change into it, else perform the next operations inside of the
    # current working directory:
    if directory:
        os.chdir(directory)

    # 2. Extract all of the .png and .jpeg files:
    files = os.listdir()

    # 3. Extract all of the images:
    images = [file for file in files if file.endswith(('jpg', 'png'))]

    # 4. Loop over every image:
    for image in images:
        print(image)

        # 5. Open every image:
        img = Image.open(image)

        # 5. Compress every image and save it with a new name:
        img.save(outputPath+image, optimize=True, quality=quality)


from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-i", "--inputPath",default="/Users/rachelchen/Desktop/father's web/3rd/")
parser.add_argument("-o", "--outputPath", default="/Users/rachelchen/Desktop/father's web/compressed/")
# the desired number of colors in the compressed image
parser.add_argument("-q", "--quality",default=1)

args = parser.parse_args()

inputPath =args.inputPath
outputPath = args.outputPath
quality =args.quality


compress_images(directory=inputPath, outputPath=outputPath,quality=quality)