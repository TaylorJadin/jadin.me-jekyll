#!/usr/bin/env python

import feedparser

p = feedparser.parse( "https://www.edtechmage.com/edtech-mages-podcast?format=rss" )
items = p["items"]
for item in items:
    time = item[ "published_parsed" ]
    title = item[ "title" ].encode('utf8')
    fileName = str(time.tm_year) + '-' + str(time.tm_mon) + '-' + str(time.tm_mday) + '-' + 'mc' + '.md'
    fileName = fileName.replace('/', '')
    f = open(fileName,'w')
    notes = item["content"][0]['value'].encode('utf8')
    link = item["link"]
    f.write('---\nlayout: post\ntitle: "Edtech Magecast ' + title + '"\n')
    f.write('''permalink: /magecast/:title/
tags: [Magecast,Podcasts]
---
''')
    f.write('[Listen here!]('+ link + ')')
    f.write('\n\n')
    f.write(notes)

print("Finished parsing Magecast RSS feed")