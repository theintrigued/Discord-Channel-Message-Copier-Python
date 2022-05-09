import requests
import json
from datetime import datetime
import time



def copy_messages0(channelid1, channelid2, auth):
        headers = {
            'authorization': f'{auth}'
        }

        r = requests.get(f'https://discord.com/api/v9/channels/{channelid1}/messages', headers = headers)
        jsonn = json.loads(r.text)
        FMT = '%H:%M:%S'
        currentTime = jsonn[0]['timestamp']
        currentTimeInHourFormat = currentTime[11:19]
        #Read Old Time From File
        file1 = open("server1.txt","r+")
        oldTime = file1.readline()
        file1.close()
        #Find Time Difference
        timeDifference = datetime.strptime(oldTime, FMT) - datetime.strptime(currentTimeInHourFormat, FMT)
        zeroTime = datetime.strptime(currentTimeInHourFormat, FMT) - datetime.strptime(currentTimeInHourFormat, FMT)

        if timeDifference == zeroTime:
           #do nothing
           print("No New Message")
        else:
         file1 = open("server1.txt","w")
         file1.write(f"{currentTimeInHourFormat}")
         file1.close()
         messageToCopy= jsonn[0]['content']
         print(timeDifference)
         payload = {
            'content' : {messageToCopy}
         }
         s = requests.post(f'https://discord.com/api/v9/channels/{channelid2}/messages', data = payload,  headers = headers)


def copy_messages1(channelid1, channelid2, auth):
        headers = {
            'authorization': f'{auth}'
        }

        r = requests.get(f'https://discord.com/api/v9/channels/{channelid1}/messages', headers = headers)
        jsonn = json.loads(r.text)
        FMT = '%H:%M:%S'
        currentTime = jsonn[0]['timestamp']
        currentTimeInHourFormat = currentTime[11:19]
        #Read Old Time From File
        file1 = open("server2.txt","r+")
        oldTime = file1.readline()
        file1.close()
        #Find Time Difference
        timeDifference = datetime.strptime(oldTime, FMT) - datetime.strptime(currentTimeInHourFormat, FMT)
        zeroTime = datetime.strptime(currentTimeInHourFormat, FMT) - datetime.strptime(currentTimeInHourFormat, FMT)

        if timeDifference == zeroTime:
           #do nothing
           print("No New Message")
        else:
         file1 = open("server2.txt","w")
         file1.write(f"{currentTimeInHourFormat}")
         file1.close()
         messageToCopy= jsonn[0]['content']
         print(timeDifference)
         payload = {
            'content' : {messageToCopy}
         }
         s = requests.post(f'https://discord.com/api/v9/channels/{channelid2}/messages', data = payload,  headers = headers)



def copy_messages2(channelid1, channelid2, auth):
        headers = {
            'authorization': f'{auth}'
        }

        r = requests.get(f'https://discord.com/api/v9/channels/{channelid1}/messages', headers = headers)
        jsonn = json.loads(r.text)
        FMT = '%H:%M:%S'
        currentTime = jsonn[0]['timestamp']
        currentTimeInHourFormat = currentTime[11:19]
        #Read Old Time From File
        file1 = open("server3.txt","r+")
        oldTime = file1.readline()
        file1.close()
        #Find Time Difference
        timeDifference = datetime.strptime(oldTime, FMT) - datetime.strptime(currentTimeInHourFormat, FMT)
        zeroTime = datetime.strptime(currentTimeInHourFormat, FMT) - datetime.strptime(currentTimeInHourFormat, FMT)

        if timeDifference == zeroTime:
           #do nothing
           print("No New Message")
        else:
         file1 = open("server3.txt","w")
         file1.write(f"{currentTimeInHourFormat}")
         file1.close()
         messageToCopy= jsonn[0]['content']
         print(timeDifference)
         payload = {
            'content' : {messageToCopy}
         }
         s = requests.post(f'https://discord.com/api/v9/channels/{channelid2}/messages', data = payload,  headers = headers)




while True:
   autho = ''
   copy_messages0('239085283616882688','970508551187497061', autho)
   copy_messages1('152855679365939200','973362701394927676', autho)
   copy_messages2('239086088260550657','973363343177945138', autho)

   #time.sleep(1)

   #1 is 1 second



