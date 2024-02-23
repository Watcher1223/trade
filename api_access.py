# from ibapi.client import EClient
# from ibapi.wrapper import EWrapper  

# class IBapi(EWrapper, EClient):
#      def __init__(self):
#          EClient.__init__(self, self) 

# app = IBapi()
# app.connect('port', "ClientID", "ClientID")
# app.run()

# '''
# #Uncomment this section if unable to connect
# #and to prevent errors on a reconnect
# import time
# time.sleep(2)
# app.disconnect()
# '''

from ibapi.client import EClient
from ibapi.wrapper import EWrapper  

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self) 

app = IBapi()
app.connect('Port', 'ClientID', 'ClientID')  # Replace '127.0.0.1 or Port Placeholder', "7497, 1, or the CleintID's" with the actual connection details

try:
    app.run()
except KeyboardInterrupt:
    # Disconnect on keyboard interrupt
    app.disconnect()
