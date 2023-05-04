from fileinput import filename
import urllib.request
import os

with open(r"C:\Users\Lenovo\Desktop\IMAGE_BLUR\imagezydus.txt") as a_file:
    for line in a_file:
        stripped_line = line.strip()

        # extract filename from URL
        filename = os.path.basename(stripped_line)

        # download and save image
        output_path = os.path.join(r"C:\Users\Lenovo\Desktop\IMAGE_BLUR\zydus_images", filename)
        urllib.request.urlretrieve(stripped_line, output_path)

        print(filename)
