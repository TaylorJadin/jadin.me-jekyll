#!/usr/bin/env python

import feedparser

rss_url = "http://feeds.soundcloud.com/users/soundcloud:users:401727513/sounds.rss"

p = feedparser.parse( rss_url )
items = p["items"]
for item in items:
    time = item[ "published_parsed" ]
    title = item[ "title" ].encode('UTF8')
    fileName = str(time.tm_year) + '-' + str(time.tm_mon) + '-' + str(time.tm_mday) + '-' + title + '.md'
    fileName = fileName.replace('/', '')
    f = open(fileName,'w')
    value = item["content"][0]['value'].encode('UTF8')
    link = item["link"]
    f.write('---\nlayout: post\ntitle: "Jadin Approved ' + title + '"\n')
    f.write('''permalink: /jadinapproved/:title/
tags: [JadinApproved,Podcasts]
---
''')
    f.write('[Listen here!]('+ link + ')')
    f.write('\n\n')
    f.write('Show notes:\n\n' + value)
print 'end'
