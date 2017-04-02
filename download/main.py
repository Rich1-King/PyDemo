#coding=UTF-8
import video,traceback

def getContent(filename):
    try:
        content = video.video_operate.getMp4(filename)
        return content
    except Exception, e:
        raise e
def writeContent(content,filename):
    try:
        video.video_operate.writeMp4(content, filename)
    except Exception, e:
        raise e
if __name__ == '__main__':
    try:
        read_filename = '/home/rich1/Videos/1.mp4'
        content = getContent(read_filename)
        writeContent(content, '/home/rich1/Videos/1_copy.mp4')
    except Exception, e:
        print('main error')
        traceback.print_exc()