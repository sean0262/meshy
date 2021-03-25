import meshtastic
from pubsub import pub

# When a package arrives, get 'from' and 'decoded'.'data'.'text. This is for getting the message and the ID from the package
def onText(packet, interface): # called when a packet arrives
    print(f"\n\n{packet.get('from')}: {packet.get('decoded').get('data').get('text')}\n")

def onConnection(interface, topic=pub.AUTO_TOPIC): # called when we (re)connect to the radio
    # defaults to broadcast, specify a destination ID if you wish
    print("\nConnected to Meshy.\n")

# First defines the serial path then runs a loop for messaging.
def sendMessage(path):
    if (path == ""):
       interface = meshtastic.SerialInterface()
    else:
       interface = meshtastic.SerialInterface(path)
    pub.subscribe(onText, "meshtastic.receive.text")
    pub.subscribe(onConnection, "meshtastic.connection.established")
    print("Send Message: ")
    while(True):
       message = input()
       interface.sendText(message)

# Choice for selecting path and then go into sendMessage fnuction.
def main():
    print("Welcome to Meshy!\n")
    ch = input("Do you wish to specify where the USB is? (/dev/ttyUSB0 - Example for Linux)\nY/n ")
    if (ch == "Y"):
       usbPath = input("\nWrite your path: ")
       sendMessage(usbPath)
    if (ch != "n"):
       print("\nInvalid input, try again.\n")
       main()
    if (ch == "n"):
       sendMessage("")

if __name__ == '__main__':
    main()
