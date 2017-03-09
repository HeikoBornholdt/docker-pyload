from module.plugins.Hook import Hook, Expose

import httplib, urllib

class PyLoadiOSPush(Hook):
    __name__ = "PyLoadiOSPush"
    __version__ = "1.1"
    __description__ = "Push for pyLoad for iOS App"
    __config__ = [("deviceKey", "str", "Device Keys (comma seperated)", ""),
		  ("pushCaptcha", "bool", "Push Captcha", True),
		  ("pushDlFail", "bool", "Push Download Failed", True),
		  ("pushPackFinish", "bool", "Push Package Finished", True),
		  ("pushAllFinish", "bool", "Push All Packages Finished", True),
		  ("pushUnrarFinish", "bool", "Push Unrar Finished", True),
		  ("activated", "bool", "Activated", True)]
    __author_name__ = ("Mathias Nagler")
   
    PUSH_URL = "95.85.62.143"
    PUSH_REQUEST = "/pyControlPush/push.php"
    
    event_map = {"coreReady" : "initialize",
		 "allDownloadsFinished": "allDlFinished",
                 "unrarFinished": "unrarFinished"}
    
    
    def initialize(self):
        if self.getConfig("deviceKey") == "":
           self.setConfig("activated",False);
    
    def newCaptchaTask(self, task):
	if self.getConfig("pushCaptcha") == True:
		self.sendNotification("captchaAvail", None);

    def downloadFailed(self, pyfile):
	if self.getConfig("pushDlFail") == True:
		self.sendNotification("dlFail", pyfile.name);

    def packageFinished(self, pypack):
	if self.getConfig("pushPackFinish") == True:
		self.sendNotification("pkgFinish", pypack.name);

    def allDlFinished(self):
	if self.getConfig("pushAllFinish") == True:
		self.sendNotification("allFinish", None);

    def unrarFinished(self, folder, fname):
        fnamesplit = fname.split("/");
        name = fnamesplit[-1];
        if self.getConfig("pushUnrarFinish") == True:
                self.sendNotification("unrarFinish", name);

    def sendNotification(self, msg, val):
	deviceKeyString = self.getConfig("deviceKey");
	deviceKeys = deviceKeyString.split(",");
	for deviceKey in deviceKeys:
        	self.logDebug("Pushing notification to device "+deviceKey);
        	params = urllib.urlencode({'deviceKey': deviceKey, 'msg': msg, 'val': val})
        	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        	conn = httplib.HTTPConnection(self.PUSH_URL)
        	conn.request("POST", self.PUSH_REQUEST, params, headers)
        	response = conn.getresponse()
        	data = response.read()
        	conn.close()
        	self.logDebug("Response: "+data);
