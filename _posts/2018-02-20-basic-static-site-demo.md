---
layout: post
title: Static HTML Demo
tags: [Post,DoOO]
---
## Directions using Reclaim Hosting

For the purposes of this demo, we will make a subdomain to upload to so we do not mess up whatever is on your root domain.

### Making a subdomain
1. Visit reclaimhosting.com
2. Click **Client Area Login**
3. From the menu, choose **cPanel** and the name of your domain
4. Click **Subdomains**
5. Under _Create a Subdomain_, in the _Subdomain_ field, write **demo**
![cPanel Subdomains screenshot](https://i.imgur.com/WSgJUTC.png)
6. Click **Create**

### Creating the files on your domain / subdomain

Next we will make an index.html file, a css folder, and a main.css file inside the folder in the correct place. The simplest way to do this will be to use cPanel's File Manager tool.

1. From cPanel, click on **File Manager**
![Picture of the cPanel File Manager](https://i.imgur.com/0JXPNAK.png)
2. Select the folder named after your subdomain (ex: **demo.jadin.me**), if you want to put this page on your root domain (ex: jadin.me) you would select the public_html folder instead
3. Click the new file button ![picture of new file button](https://i.imgur.com/e5cOxXl.png)
4. Name the file index.html and click **Create New File**
5. Next, select the file and click the edit button ![picture of edit button](https://i.imgur.com/ucduek5.png)
6. Click **Edit**
7. Paste in the contents of the index.html file from this repository.