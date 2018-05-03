#!/usr/bin/env python

import feedparser

p = feedparser.parse( "http://feeds.soundcloud.com/users/soundcloud:users:401727513/sounds.rss" )
items = p["items"]
for item in items:
    time = item[ "published_parsed" ]
    title = item[ "title" ].encode('UTF8')
    fileName = str(time.tm_year) + '-' + str(time.tm_mon) + '-' + str(time.tm_mday) + '-' + title + '.md'
    fileName = fileName.replace('/', '')
    f = open(fileName,'w')
    notes = item["content"][0]['value'].encode('UTF8')
    link = item["link"]
    f.write('---\nlayout: post\ntitle: "Jadin Approved Podcast ' + title + '"\n')
    f.write('''permalink: /jadinapproved/:title/
tags: [JadinApproved,Podcasts]
---
''')
    f.write('[Listen here!]('+ link + ')')
    f.write('\n\n')
    f.write(notes)

print("Finished parsing Jadin Approved RSS feed")