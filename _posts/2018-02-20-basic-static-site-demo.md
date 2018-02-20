---
layout: post
title: Static Site Demo
tags: [Post,DoOO]
---
This is a little post I put together to show students at St. Norbert College how to quickly put a static page up on their domain. In this post I am assuming almost no prior knowledge of HTML, CSS, or cPanel. The only thing you need ahead of time is a domain at [Reclaim Hosting](https://reclaimhosting.com).

When we are finished you will have a page that looks like this: [demo.jadin.me](demo.jadin.me)

If you already have content on your root domain (ex: [jadin.me](jadin.me)), you might want to [make a subdomain first](https://www.jadin.me/2018/02/19/creating-a-subdomain.html). 

## Creating index.html

First we will make an index.html file. The simplest way to do this will be to use cPanel's File Manager tool.

1. From cPanel, click on !cPanel File Manager](https://i.imgur.com/0JXPNAK.png)
2. Select the folder named **public_html**, if you want to put this page on your subdomain (ex: **demo.jadin.me**), click folder named after that subdomain instead.
3. Click ![new file button](https://i.imgur.com/e5cOxXl.png)
4. Name the file index.html and click **Create New File**
5. Next, select the file and click ![edit button](https://i.imgur.com/ucduek5.png)
6. Click **Edit**
7. Paste the html below into your index.html file:
<script src="https://gist.github.com/TaylorJadin/d789db56a7cfc37ebe34af3ed990092f.js"></script>
8. Click **Save Changes**
9. Click **Close**
10. Go to your site and take a look! 

## Creating main.css
We have the basic content there, but it should look a bit off if you compare it to my demo page at [demo.jadin.me](demo.jadin.me). That is because we need to add style information using CSS!

1. Go back to the cPanel file manager
2. Next to 


<script src="https://gist.github.com/TaylorJadin/e912ba2cb1a1edf41f52b2b6da9a78ef.js"></script>