import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from gpiozero import LED, Button, Buzzer, PWMLED
from time import sleep

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

led1 = LED(20)
led2 = PWMLED(21)
bz = Buzzer(17)

btn = Button(16)

db = firestore.client()

# CREATE OPERATION
# db.collection('outputDevices').document('digitalLED').set(
#     {
#         'status' : False
#     }
# )
# db.collection('outputDevices').document('pwmLED').set(
#     {
#         'brightness' : 0
#     }
# )
# db.collection('outputDevices').document('buzzer').set(
#     {
#         'alarm' : False
#     }
# )

# db.collection('inputDevices').document('button').set(
#     {
#         'value' : False
#     }

# READ OPERATION
# while True:
#     readStatus = db.collection('outputDevices').document('digitalLED').get()
#     docDict = readStatus.to_dict()
#     LEDstatus = docDict['status']

#     if(LEDstatus):
#         led1.on()
#     else :
#         led1.off()

# UPDATE OPERATION
# while True:
#     if(btn.is_active):
#         db.collection('inputDevices').document('button').update(
#             {
#                 'value' : True
#             }
#         )
#     else:
#         db.collection('inputDevices').document('button').update(
#             {
#                 'value' : False
#             }
#         )

# DELETE OPERATION
# db.collection('outputDevices').document('buzzer').update(
#     {
#         'alarm' : firestore.DELETE_FIELD
#     }
# )

# ALARM (READ OPERATION)
# while True:
#     readStatus = db.collection('outputDevices').document('buzzer').get()
#     docDict = readStatus.to_dict()
#     triggerAlarm = docDict['alarm']

#     if(triggerAlarm):
#         bz.on()
#         sleep(1)
#         bz.off()
#         sleep(1)

# LED-BUTTON Firestore Medium
# while True:
#     if(btn.is_active):
#         db.collection('inputDevices').document('button').update(
#             {
#                 'value' : True
#             }
#         )
#     else:
#         db.collection('inputDevices').document('button').update(
#             {
#                 'value' : False
#             }
#         )
#     readStatus = db.collection('inputDevices').document('button').get()
#     docDict = readStatus.to_dict()
#     Btnstatus = docDict['value']

#     if(Btnstatus):
#         led1.on()
#     else:
#         led1.off()

# PWMLED

while True:
    readBrightness = db.collection('outputDevices').document('pwmLED').get()
    docDict = readBrightness.to_dict()
    brightness = docDict['brightness']

    if(brightness >= 0 and brightness <= 1):
        led2.value = brightness
    else:
        led2.value = 0
