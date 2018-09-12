#! /usr/bin/python
import tweepy
from keys import keys
import sys
 
SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
    
followers = api.followers_ids(SCREEN_NAME) #get list of people who follow me
friends = api.friends_ids(SCREEN_NAME) #get list of people i follow

print "#Followers: ", len(followers)
print "#Following: ", len(friends)

good_boys = []
bad_boys = []
try:
	for f in friends:
		if f in followers:
			good_boys.append(f)
		else:
			bad_boys.append(f)
			print "Sorry, the user ", api.get_user(f).screen_name, " did not follow you..."
			var = raw_input("Want to unfollow them? (y/n)\n")
			print "you entered", var
			if var == 'y':
				print "Destroying friendship...\n"
				#api.destroy_friendship(f)
			else: # var == 'n':
				print "We will keep this friend for you.\n"
			if api.get_user(f).default_profile_image == True:
				print "Sorry, the user ", api.get_user(f).screen_name, " dont have a real photo..."
				var = raw_input("Want to unfollow them? (y/n)\n")
				print "you entered", var
				if var == 'y':
					print "Destroying friendship...\n"
					api.destroy_friendship(f)
				else: # var == 'n':
					print "We will keep this friend for you.\n"
			# else:
			# 	sys.stdout.write("Please respond with 'y' to keep the friend or 'n' to unfollow them.\n")
except tweepy.TweepError, e:
    if e == "[{u'message': u'Rate limit exceeded', u'code': 88}]":
        time.sleep(60*5) #Sleep for 5 minutes
    else:
        print e

print "I follow and they follow back :)", len(good_boys)
print "I follow and they ignored me :(", len(bad_boys)