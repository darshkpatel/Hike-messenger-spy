import json
import urllib2
import time

user_number = raw_input("Mobile Number: ")
user = "**********"
user = 'user='+str(user)

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', user))
last = opener.open("http://api.im.hike.in/v1/user/lastseen/+91"+str(user_number))
profile = opener.open("http://api.im.hike.in/v1/account/profile/+91"+str(user_number))
last_content = last.read()
profile_content = profile.read()
json_last = json.loads(last_content)
json_profile = json.loads(profile_content)
epoch_join = json_profile['profile']['jointime']
print json_profile['profile']['name']
epoch_last = json_last['d']['ls']
print "Join Time: "+ str(time.strftime("%a, %d %b %Y %I:%M:%S %p", time.localtime(epoch_join))) 
if(epoch_last==0):
    print "Online !"
else:
    
    print "Last Seen: "+ str(time.strftime("%a, %d %b %Y %I:%M:%S %p", time.localtime(epoch_last))) 
