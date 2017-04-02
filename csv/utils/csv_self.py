import csv,os

def write(path, data):
    filer = file(path, 'wb')
    writer = csv.writer(filer)
    writer.writerows(data)
    filer.close()