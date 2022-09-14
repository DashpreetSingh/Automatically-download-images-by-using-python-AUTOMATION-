from fileinput import filename
import urllib.request

with open("C:\\Users\\KUNAL SINGH\\OneDrive\\Desktop\\web\\RBtextUrl.txt","r") as a_file:
    for line in a_file:
        stripped_line = 5000
        stripped_line = line.strip()

        filename = stripped_line[52:]
        urllib.request.urlretrieve(stripped_line,"C:\\Users\\KUNAL SINGH\\OneDrive\\Desktop\\web\\UrlImagedata"+filename)


        print(filename)