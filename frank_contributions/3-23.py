import subprocess
import time
from skpy import SkypeEventLoop, SkypeNewMessageEvent
class SkypePing(SkypeEventLoop):
        def __init__(self):
                super(SkypePing, self).__init__(credentials.username, credentials.password)
        def onEvent(self, event):
                if isinstance(event, SkypeNewMessageEvent):# \
                        f1 = open("s3.txt","a")
                        f2 = open("s3.txt", "r")
                        f1.write(str(event.msg.content) + '\n')
                        f2.seek(0)
                        if(len(f2.readlines()) > 9) :
                                s3 = boto3.client('s3')
                                bucket_name = 'skypedata'
                                file_name = "file{}".format(format(time.time()))
                                os.rename("s3.txt",file_name)  #rename to avoid "file exists error"
                                s3.upload_file(file_name, bucket_name, "dump/"+file_name)
                                subprocess.call(["hdfs", "dfs", "-put", file_name]) #save the file to hdfs
                                os.remove(file_name)
                                print("------------updating s3-----------------")

                        print(event.msg)
