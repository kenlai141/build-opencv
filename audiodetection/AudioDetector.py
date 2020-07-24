import json
import numpy as np
import threading
import time

import requests
from requests.auth import HTTPDigestAuth
from utils.DetTimer import detTimer

'''
Manually set the below two params in the cam's web app
sensitivity = 1
threshold = 95
To understand the data get from API, look into Dahua HTTP API v2.76, section 4.9.17 Subscribe to Event Message 
'''

HEARTBEAT = 3  # seconds
CHUNK_SIZE = 1
DURATION = 8  # seconds


class AudioDetector(threading.Thread):
    """Audio Detection object. To detect whether the sound level reach the threshold.
    """

    def __init__(self, username, password, ip, duration=DURATION):
        """Constructor

        Args:
            username (str): username of ip cam
            password (str): password of ip cam
            ip (str): ip address of IP cam
            duration (int): operating time for this thread in second, if duration=None, this thread runs forever
        """
        super().__init__()
        self.username = username
        self.password = password
        self.ip = ip
        self.auth = HTTPDigestAuth(self.username, self.password)
        self.channelEventHappenedAPI = self.getChannelEventHappenedAPI()
        self.audioMutationSubAPI = self.getAudioMutationSubAPI()
        self.__status = False
        self.__isHeartbeat = False
        self.setDaemon(True)
        self._stop = threading.Event()
        self.timer = None
        self.duration = duration

    def getChannelEventHappenedAPI(self):
        return f"http://{self.ip}/cgi-bin/eventManager.cgi?action=getEventIndexes&code=AudioMutation"

    def getAudioMutationSubAPI(self):
        """Subscrbe to audio mutation event. 

        Returns:
            str: url of the API
        """
        return f"http://{self.ip}/cgi-bin/eventManager.cgi?action=attach&codes=[AudioMutation]&heartbeat={HEARTBEAT}"

    def run(self):
        """Run the detection thread here.
            1. get subscription to audio mutation event
            2. start the timer that kill this thread after `DURATION`
            3. parse data to result(status)
        """

        try:
            r = requests.get(self.audioMutationSubAPI,
                             auth=self.auth, stream=True)
        except Exception as e:
            print(e)
            return

        if r.status_code != 200:
            print(f"Cannot get resource, status code: {r.status_code}")
            return

        self.startTimer()

        for line in r.iter_lines(chunk_size=CHUNK_SIZE):
            # filter out keep-alive new lines
            if line:
                decoded_line = line.decode('utf-8')
                if 'action' in decoded_line:
                    if 'Start' in decoded_line:
                        # print('Loud noise detected')
                        self.status = True
                    elif 'End' in decoded_line:
                        # print('Back to normal')
                        self.status = False
                if 'Heartbeat' in decoded_line:
                    print(f"[{time.asctime()}]" + " heartbeat")
                    self.__isHeartbeat = True

            if self._stop.is_set():
                break

        print(f"End thread at {self.ip}")

    def stop(self):
        """Stop the thread as well as the timer
        """
        self._stop.set()
        if self.timer:
            self.timer.cancel()

    def startTimer(self):
        """Start the timer that limits how long the thread runs
        """
        if self.duration:
            self.timer = detTimer(self.duration, self.stop)
            self.timer.start()

    # TODO: develop API
    def postReq(self):
        pass

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getStatus(self):
        return self.__status

    def getIsHeartbeat(self):
        return self.__isHeartbeat


if __name__ == "__main__":

    audioDetector = AudioDetector('admin', 'cepa5566', '192.168.1.109')
    audioDetector.start()

    time.sleep(15)

    # url_getAudio = "http://192.168.1.109/cgi-bin/audio.cgi?action=getAudio&httptype=singlepart&channel=1"

    # r = requests.get(url_getAudio, auth=auth, stream=True)
    # for line in r.iter_content(12000):
    #     # filter out keep-alive new lines
    #     data = np.frombuffer(line, dtype=np.int16)
    #     print(data[:10])
    #     print(data.shape)
