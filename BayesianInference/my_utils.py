from os.path import exists, basename 
from urllib.request import urlretrieve


def file_download(url):
    filename = basename(url)
    if not exists(filename):
        file, _ = urlretrieve(url, filename)
        if not file:
            print(" problem with download, please check the url")
        print('downloaded the file "{}"'.format(file))
    else:
        print('file already exists inside the path')
        
        
        
    

