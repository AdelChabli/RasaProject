class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)
        try:
            self.ad = None
            # self.ad = ALProxy("ALAudioDevice")
        except Exception as e:
            self.ad = None
            self.logger.error(e)
        self.filepath = ""

    def onLoad(self):
        self.bIsRecording = False
        self.bIsRunning = False

    def onUnload(self):
        self.bIsRunning = False
        if( self.bIsRecording ):
            self.ad.stopMicrophonesRecording()
            self.bIsRecording = False

    def onInput_onStart(self, p):
        if(self.bIsRunning):
            return
        self.bIsRunning = True
        sExtension = self.toExtension( self.getParameter("Microphones used") )
        self.filepath = p + sExtension
        if self.ad:
            self.ad.startMicrophonesRecording( self.filepath )
            self.bIsRecording = True
        else:
            self.logger.warning("No sound recorded")

    def onInput_onStop(self):
        if( self.bIsRunning ):
            self.onUnload()
            self.onStopped(self.filepath)

    def toExtension(self, sMicrophones):
        if( sMicrophones == "Front head microphone only (.ogg)"):
            return ".ogg"
        else:
            return ".wav"