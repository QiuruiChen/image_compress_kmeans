from PIL import Image
from os import listdir
from os.path import isfile, join
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--width",default=68)
parser.add_argument("--height", default=68)
# the desired number of colors in the compressed image
parser.add_argument("--inputPath",default="/Users/rachelchen/Desktop/father's web/test/")
parser.add_argument("--outputPath",default="/Users/rachelchen/Desktop/father's web/demo/")
parser.add_argument("--crop",default=True)

args = parser.parse_args()

inputPath =args.inputPath
outputPath = args.outputPath

onlyfiles = [f for f in listdir(inputPath) if isfile(join(inputPath, f))]

for fileName in onlyfiles:
    im = Image.open(inputPath+fileName).convert('RGB')
    if(args.crop==True):
        width, height = im.size  # Get dimensions

        left = (width - args.width) / 2
        top = (height - args.height) / 2
        right = (width + args.width) / 2
        bottom = (height + args.height) / 2

        # Crop the center of the image
        im = im.crop((left, top, right, bottom))
    else:
        img = img.resize((args.width, args.height), Image.ANTIALIAS)

    im.save(outputPath+fileName,'webp')




