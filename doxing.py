#!/usr/bin/env	python3
import sys,os

#colors
cyan="\033[1;36m"
green="\033[1;32m"
red="\033[1;31m"
reset="\033[00m"
url="https://www.facebook.com/search/"

def run(user_id, time):
	os.system('clear')

	if user_id != "" and time != "":
		profile="""%s Profile%s
%s Pictures:%s %s%s/photos-by/%s/date/photos/intersect
%s Videos:%s %s%s/videos-by/%s/date/videos/intersect
%s Posts:%s %s%s/stories-by/%s/date/stories/intersect
%s Groups:%s %s%s/groups
%s Future events:%s %s%s/events-joined/
%s Past events:%s %s%s/events-joined/in-past/date/events/intersect/
%s Games:%s %s%s/apps-used/game/apps/intersect
%s Apps:%s %s%s/apps-used/
		"""%(cyan,reset,#title
			green,reset,url,user_id,time,#Pictures
			green,reset,url,user_id,time,#Videos
			green,reset,url,user_id,time,#Posts
			green,reset,url,user_id,#Groups
			green,reset,url,user_id,#Future events
			green,reset,url,user_id,#Past events
			green,reset,url,user_id,#Games
			green,reset,url,user_id)
		print(profile)

		tags="""%s Tags%s
%s Pictures:%s %s%s/photos-of/%s/date/photos/intersect/intersect
%s Video:%s %s%s/videos-of/%s/date/videos/intersect/intersect
%s Posts:%s %s%s/stories-tagged/%s/date/stories/intersect/intersect
		"""%(cyan,reset,#title
			green,reset,url,user_id,time,#Pictures
			green,reset,url,user_id,time,#Videos
			green,reset,url,user_id,time)
		print(tags)

		comments="""%s Comments%s
%s Pictures:%s %s%s/photos-commented/%s/date/photos/intersect/intersect
		"""%(cyan,reset,#title
			green,reset,url,user_id,time)
		print(comments)

		liked="""%s Liked%s
%s Pictures:%s %s%s/photos-liked/%s/date/photos/intersect/intersect
%s Videos:%s %s%s/videos-liked/%s/date/videos/intersect/intersect
%s Posts:%s %s%s/stories-liked/%s/date/stories/intersect/intersect
		"""%(cyan,reset,#title
			green,reset,url,user_id,time,#Pictures
			green,reset,url,user_id,time,#Videos
			green,reset,url,user_id,time)
		print(liked)

		places="""%s Places%s
%s All:%s %s%s/places-visited/
%s Bars:%s %s%s/places-visited/110290705711626/places/intersect/
%s Restaurants:%s %s%s/places-visited/273819889375819/places/intersect/
%s Stores:%s %s%s/places-visited/200600219953504/places/intersect/
%s Outdoors:%s %s%s/places-visited/935165616516865/places/intersect/
%s Hotels:%s %s%s/places-visited/164243073639257/places/intersect/
%s Theaters:%s %s%s/places-visited/192511100766680/places/intersect/
		"""%(cyan,reset,#title
			green,reset,url,user_id,#All
			green,reset,url,user_id,#Bars
			green,reset,url,user_id,#Restaurants
			green,reset,url,user_id,#Stores
			green,reset,url,user_id,#Outdoors
			green,reset,url,user_id,#Hotels
			green,reset,url,user_id)
		print(places)

		people="""%s People%s
%s Family:%s %s%s/relatives/intersect
%s Friends:%s %s%s/friends/intersect
%s Friends of friends:%s %s%s/friends/friends/intersect
%s Co-workers:%s %s%s/employees/intersect/
%s Classmates:%s %s%s/schools-attended/ever-past/intersect/students/intersect/
%s Locals:%s %s%s/current-cities/residents-near/present/intersect
		"""%(cyan,reset,#title
			green,reset,url,user_id,#Family
			green,reset,url,user_id,#Friends
			green,reset,url,user_id,#Friends of friends
			green,reset,url,user_id,#Co-workers
			green,reset,url,user_id,#Classmates
			green,reset,url,user_id)
		print(people)

		intersect="""%s Interests%s
%s Pages:%s %s%s/pages-liked/intersect
%s Political parties:%s %s%s/pages-liked/161431733929266/pages/intersect/
%s Religion:%s %s%s/pages-liked/religion/pages/intersect/
%s Music:%s %s%s/pages-liked/musician/pages/intersect/
%s Movies:%s %s%s/pages-liked/movie/pages/intersect/
%s Books:%s %s%s/pages-liked/book/pages/intersect/
%s Places:%s %s%s/places-liked/
		"""%(cyan,reset,#title
			green,reset,url,user_id,#Pages
			green,reset,url,user_id,#Political
			green,reset,url,user_id,#Religion
			green,reset,url,user_id,#Music
			green,reset,url,user_id,#Movies
			green,reset,url,user_id,#Books
			green,reset,url,user_id)
		print(intersect)

# Solo con ID
	elif user_id != "":
		profile="""%s Profile%s
%s Pictures:%s %s%s/photos-by/
%s Videos:%s %s%s/videos-by/
%s Posts:%s %s%s/stories-by/
%s Groups:%s %s%s/groups
%s Future events:%s %s%s/events-joined/
%s Past events:%s %s%s/events-joined/in-past/date/events/intersect/
%s Games:%s %s%s/apps-used/game/apps/intersect
%s Apps:%s %s%s/apps-used/
		"""%(cyan,reset,#title
			green,reset,url,user_id,#Pictures
			green,reset,url,user_id,#Videos
			green,reset,url,user_id,#Posts
			green,reset,url,user_id,#Groups
			green,reset,url,user_id,#Future events
			green,reset,url,user_id,#Past events
			green,reset,url,user_id,#Games
			green,reset,url,user_id)
		print(profile)

		tags="""%s Tags%s
%s Pictures:%s %s%s/photos-of/intersect
%s Video:%s %s%s/videos-of/intersect
%s Posts:%s %s%s/stories-tagged/intersect
		"""%(cyan,reset,#title
			green,reset,url,user_id,#Pictures
			green,reset,url,user_id,#Videos
			green,reset,url,user_id)
		print(tags)
			
		comments="""%s Comments%s
%s Pictures:%s %s%s/photos-commented/intersect
		"""%(cyan,reset,#title
			green,reset,url,user_id)
		print(comments)

		liked="""%s Liked%s
%s Pictures:%s %s%s/photos-liked/intersect
%s Videos:%s %s%s/videos-liked/intersect
%s Posts:%s %s%s/stories-liked/intersect
		"""%(cyan,reset,#title
			green,reset,url,user_id,#Pictures
			green,reset,url,user_id,#Videos
			green,reset,url,user_id)
		print(liked)

		places="""%s Places%s
%s All:%s %s%s/places-visited/
%s Bars:%s %s%s/places-visited/110290705711626/places/intersect/
%s Restaurants:%s %s%s/places-visited/273819889375819/places/intersect/
%s Stores:%s %s%s/places-visited/200600219953504/places/intersect/
%s Outdoors:%s %s%s/places-visited/935165616516865/places/intersect/
%s Hotels:%s %s%s/places-visited/164243073639257/places/intersect/
%s Theaters:%s %s%s/places-visited/192511100766680/places/intersect/
		"""%(cyan,reset,#title
			green,reset,url,user_id,#All
			green,reset,url,user_id,#Bars
			green,reset,url,user_id,#Restaurants
			green,reset,url,user_id,#Stores
			green,reset,url,user_id,#Outdoors
			green,reset,url,user_id,#Hotels
			green,reset,url,user_id)
		print(places)

		people="""%s People%s
%s Family:%s %s%s/relatives/intersect
%s Friends:%s %s%s/friends/intersect
%s Friends of friends:%s %s%s/friends/friends/intersect
%s Co-workers:%s %s%s/employees/intersect/
%s Classmates:%s %s%s/schools-attended/ever-past/intersect/students/intersect/
%s Locals:%s %s%s/current-cities/residents-near/present/intersect
		"""%(cyan,reset,#title
			green,reset,url,user_id,#Family
			green,reset,url,user_id,#Friends
			green,reset,url,user_id,#Friends of friends
			green,reset,url,user_id,#Co-workers
			green,reset,url,user_id,#Classmates
			green,reset,url,user_id)
		print(people)

		intersect="""%s Interests%s
%s Pages:%s %s%s/pages-liked/intersect
%s Political parties:%s %s%s/pages-liked/161431733929266/pages/intersect/
%s Religion:%s %s%s/pages-liked/religion/pages/intersect/
%s Music:%s %s%s/pages-liked/musician/pages/intersect/
%s Movies:%s %s%s/pages-liked/movie/pages/intersect/
%s Books:%s %s%s/pages-liked/book/pages/intersect/
%s Places:%s %s%s/places-liked/
		"""%(cyan,reset,#title
			green,reset,url,user_id,#Pages
			green,reset,url,user_id,#Political
			green,reset,url,user_id,#Religion
			green,reset,url,user_id,#Music
			green,reset,url,user_id,#Movies
			green,reset,url,user_id,#Books
			green,reset,url,user_id)
		print(intersect)
	else:
		print("\n %sE:%s Please set value of element id: set id=<user_id>"%(red,reset))