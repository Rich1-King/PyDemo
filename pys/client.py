import os
print(os.system('ls'))
print(os.system('netstat -ano|grep mysql'))
print(os.system('ps -ef|grep mysql'))
#print(os.system('ssh root@115.159.159.108'))
#print(os.system('sc700609'))
#str = os.system('curl -H -l https://www.tmall.com/?ali_trackid=2:mm_26632258_3504122_48284354:1489816401_2k1_1638651257&upsid=6cfb754f76b7e237f5823e8d5358502b&clk1=6cfb754f76b7e237f5823e8d5358502b');
#print(str + 'hello')
print('over')
ls = os.system('ls')