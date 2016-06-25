# Hike-messenger-spy
A small python script which lets you:
..* View Last Seen
..* View Join Date
..* View Profile name 
 of the people who have added the victim to their favourites. (You need their phone numbers though)

#Grabbing The Cookie
*We need a user identification cookie , which helps us make requests to the Hike API server. One can use any packet capture utility and find the following request -
```GET /v1/account/profile/<Phone NUmber> HTTP/1.1
retry-header: 1
User-Agent: android-4.2.7.83
Cookie: user=***********; UID=*****-***
Cache-Control: no-transform
Host: api.im.hike.in
Connection: Keep-Alive
Accept-Encoding: gzip```

* we need the 'User' Cookie

#Configuring the Program
* Replace the cookie we captured in place of the asteriks on line 6 in the PoC.py

#Using the program 
* `Python PoC.py'
* Enter Phone Number 
* Magic !
