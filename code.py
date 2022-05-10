import requests
import json
from datetime import datetime
import time



def copy_messages0(channelid1, channelid2, auth, serverTimeFile):
        headers = {
            'authorization': f'{auth}'
        }

        r = requests.get(f'https://discord.com/api/v9/channels/{channelid1}/messages', headers = headers)
        jsonn = json.loads(r.text)
        FMT = '%H:%M:%S'
        currentTime = jsonn[0]['timestamp']
        currentTimeInHourFormat = currentTime[11:19]
        #Read Old Time From File
        file1 = open(f"{serverTimeFile}","r+")
        oldTime = file1.readline()
        file1.close()
        #Find Time Difference
        timeDifference = datetime.strptime(oldTime, FMT) - datetime.strptime(currentTimeInHourFormat, FMT)
        zeroTime = datetime.strptime(currentTimeInHourFormat, FMT) - datetime.strptime(currentTimeInHourFormat, FMT)

        if timeDifference == zeroTime:
           #do nothing
           print("No New Message")
        else:
         file1 = open(f"{serverTimeFile}","w")
         file1.write(f"{currentTimeInHourFormat}")
         file1.close()
         messageToCopy= jsonn[0]['content']
         print(timeDifference)
         payload = {
            'content' : {messageToCopy}
         }
         s = requests.post(f'https://discord.com/api/v9/channels/{channelid2}/messages', data = payload,  headers = headers)


def copy_messages1(channelid1, channelid2, auth, serverTimeFile):
        headers = {
            'authorization': f'{auth}'
        }

        r = requests.get(f'https://discord.com/api/v9/channels/{channelid1}/messages', headers = headers)
        jsonn = json.loads(r.text)
        FMT = '%H:%M:%S'
        currentTime = jsonn[0]['timestamp']
        currentTimeInHourFormat = currentTime[11:19]
        #Read Old Time From File
        file1 = open(f"{serverTimeFile}","r+")
        oldTime = file1.readline()
        file1.close()
        #Find Time Difference
        timeDifference = datetime.strptime(oldTime, FMT) - datetime.strptime(currentTimeInHourFormat, FMT)
        zeroTime = datetime.strptime(currentTimeInHourFormat, FMT) - datetime.strptime(currentTimeInHourFormat, FMT)

        if timeDifference == zeroTime:
           #do nothing
           print("No New Message")
        else:
         file1 = open(f"{serverTimeFile}","w")
         file1.write(f"{currentTimeInHourFormat}")
         file1.close()
         messageToCopy= jsonn[0]['content']
         print(timeDifference)
         payload = {
            'content' : {messageToCopy}
         }
         s = requests.post(f'https://discord.com/api/v9/channels/{channelid2}/messages', data = payload,  headers = headers)



def copy_messages2(channelid1, channelid2, auth, serverTimeFile):
        headers = {
            'authorization': f'{auth}'
        }

        r = requests.get(f'https://discord.com/api/v9/channels/{channelid1}/messages', headers = headers)
        jsonn = json.loads(r.text)
        FMT = '%H:%M:%S'
        currentTime = jsonn[0]['timestamp']
        currentTimeInHourFormat = currentTime[11:19]
        #Read Old Time From File
        file1 = open(f"{serverTimeFile}","r+")
        oldTime = file1.readline()
        file1.close()
        #Find Time Difference
        timeDifference = datetime.strptime(oldTime, FMT) - datetime.strptime(currentTimeInHourFormat, FMT)
        zeroTime = datetime.strptime(currentTimeInHourFormat, FMT) - datetime.strptime(currentTimeInHourFormat, FMT)

        if timeDifference == zeroTime:
           #do nothing
           print("No New Message")
        else:
         file1 = open(f"{serverTimeFile}","w")
         file1.write(f"{currentTimeInHourFormat}")
         file1.close()
         messageToCopy= jsonn[0]['content']
         print(timeDifference)
         payload = {
            'content' : {messageToCopy}
         }
         s = requests.post(f'https://discord.com/api/v9/channels/{channelid2}/messages', data = payload,  headers = headers)




while True:
   autho = '' #Write your authorization key here
   copy_messages0('','', autho, 'server1.txt')
   copy_messages1('','', autho, 'server2.txt')
   copy_messages2('','', autho, 'server3.txt')

   #time.sleep(1)

   #1 is 1 second



