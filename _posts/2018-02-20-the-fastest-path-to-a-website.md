---
layout: post
title: The fastest path to a website
tags: [domains]
---
This is a little post I put together to show students at St. Norbert College how to quickly put a static page up on their domain. In this post I am assuming almost no prior knowledge of HTML, CSS, or cPanel. The only thing you need ahead of time is a domain at [Reclaim Hosting](https://reclaimhosting.com).

When we are finished you will have a page that looks like this: [demo.jadin.me](https://demo.jadin.me)

If you already have content on your root domain (ex: [jadin.me](https://jadin.me)), you might want to [make a subdomain first](https://www.jadin.me/2018/02/19/creating-a-subdomain.html). 

## Creating index.html

First we will make an index.html file. The simplest way to do this will be to use cPanel's File Manager tool.

1. Log in to cPanel, and click on ![cPanel File Manager](https://i.imgur.com/0JXPNAK.png)
2. Select the folder named **public_html**, if you want to put this page on your subdomain (ex: **demo.jadin.me**), click folder named after that subdomain instead.
3. Click ![new file button](https://i.imgur.com/e5cOxXl.png)
4. Name the file **index.html** (case matters!) and click **Create New File**
5. Next, select the file and click ![edit button](https://i.imgur.com/ucduek5.png)
6. Click **Edit**
7. Paste the html below into your index.html file:
<script src="https://gist.github.com/TaylorJadin/d789db56a7cfc37ebe34af3ed990092f.js"></script>
8. Click **Save Changes**
9. Click **Close**
10. Go to your site and take a look! 

## Creating main.css
We have the basic content there, but it should look a bit off if you compare it to my demo page at [demo.jadin.me](https://demo.jadin.me). It looks strange because it is missing style information, we can fix that by adding a main.css file!

1. Go back to the cPanel file manager
2. In the same folder where you have index.html, click ![new folder button](https://i.imgur.com/5vseFrE.png)
3. Name the folder **css** (case matters!) and click **Create New Folder**
4. Select the css folder you just created, and create a new file in this folder called **main.css**
5. You should now have an index.html file, a css folder, and a main.css folder inside it:
```
├── css
│   └── main.css
└── index.html
```
6. Edit **main.css** and Paste the code below into the file:
<script src="https://gist.github.com/TaylorJadin/e912ba2cb1a1edf41f52b2b6da9a78ef.js"></script>
7. Click **Save Changes** and **Close**
8. Check out your site again and see how it looks!