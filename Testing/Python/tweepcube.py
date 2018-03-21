import tweepy
import arduinoserial
from time import sleep
from random import randint


arduino = arduinoserial.SerialPort("/dev/cu.usbmodem141411", 9600)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

	def on_status(self, status):
		print(status.text)
		arduino.write(str(randint(49, 56)) + str(randint(49, 56)) + str(randint(49, 56)))
		# print arduino.read_until('\n')

auth = tweepy.OAuthHandler("gRJLSDn77LlqEw3xauLTipWde", "yq4QeKiAuwHqJtjCZ7bYWFGYxd8x3kzHvyKYjMPQoLGXCwR9K3")
auth.access_token = "1656639696-d62wfIKOtYstSWF35cG4E5GN7cewWCltJsTKM4c"
auth.access_token_secret = "qKTnzcMxeRPCUyqQbkmbsS30lMyXnQ5dZ27e62ezMKy60"

api = tweepy.API(auth)
# api.update_status('tweepy + oauth!')

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['GDC'])


