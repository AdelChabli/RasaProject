import urllib2
import json
import random
import time


class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.url_rasa = 'http://169.254.110.253:8082/'  # IP : serveur rasa
        self.url_stt = 'http://169.254.110.253:8082/'  # IP : serveur speech to text
        self.on_starting = True
        self.text = None
        self.user = "user"

    def onInput_onResponseAPI(self, text=None):
        rasa, stt = self.check_servers()
        if not rasa or not stt:
            self.onBye(self.text)
            self.onStopped()
            return

        res = self.send_request(text)
        self.text = self.process_response(res)
        self.onGotResponse(self.text)

    def onLoad(self):
        # put initialization code here
        pass

    def onUnload(self):
        # put clean-up code here
        pass

    def onInput_onStart(self):

        rasa, stt = self.check_servers()
        if not rasa or not stt:
            self.onBye(self.text)
            self.onStopped()
            return

        if self.on_starting:
            self.user += str(random.randint(1000, 9999))
            self.on_starting = False
            self.onGotResponse(self.text, self.on_starting)

    def onInput_onStop(self):
        self.onUnload()  # it is recommended to reuse the clean-up as the box is stopped
        self.onStopped()  # activate the output of the box

    def check_servers(self):

        url_rasa = self.url_rasa + '/webhooks/rest'
        url_stt = self.url_stt + '/status'

        req_rasa = urllib2.Request(url_rasa, data=None)
        f_rasa = urllib2.urlopen(req_rasa)
        res_rasa = f_rasa.read()

        req_stt = urllib2.Request(url_stt, data=None)
        f_stt = urllib2.urlopen(req_stt)
        res_stt = f_stt.read()

        online_rasa, online_stt = False, False
        if res_rasa['status'] == 'OK':
            online_rasa = True
            self.text += "Server RASA available ! "
        else:
            self.text += "Server RASA unreachable ! "
        if res_stt['status'] == 'OK':
            online_stt = True
            self.text += "Server GOOGLE available ! "
        else:
            self.text += "Server GOOGLE unreachable ! "

        return online_rasa, online_stt

    def send_request(self, text):
        url_rasa = self.url_rasa + "/webhooks/rest/webhook"
        data = {
            "sender": self.user,
            "message": text,
        }

        req = urllib2.Request(url_rasa, data=data)
        f = urllib2.urlopen(req)

        response = f.read()
        return response

    def process_response(self, response):
        res = ""
        for row in response:
            res += row['text']

        return res
