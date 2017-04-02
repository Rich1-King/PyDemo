#coding=utf-8
import utils

if __name__ == '__main__':
    filename = 'testcsv.csv'
    data = [
        ('name','age','sex'),
        ('张三','23','1'),
        ('李四','22','0')
        ]
    utils.csv_self.write(filename, data)

