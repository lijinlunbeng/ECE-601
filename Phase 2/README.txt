social media analyzer

ALL computing languages are using python

I use an example to explain what I did for this project. A homework (phase 2) in the class EC 601

1.Define MVP and user stories
2.Translate user stories to a modular design
3.Who is your user?
4.What are the basic user stories?

Introduction:
I designed this one to capture data from certain users on Twitter. What are my specific users? Young people who like KPOP music. A quick introduction to the product is to use Tweepy (which is a twitter API) to track if a user writes a keyword about any KPOP music. Then I will use natural language learning (NPL) to understand each twitter message of this person in a more comprehensive way, and summarize each Twitter message to conclude whether this person is a fan group of KPOP.

1. Define MVP and user stories
The most basic feature (MVP) I want to implement is whether or not this person posts information about any KPOP in their Twitter feed. In other words, it gives a general sense of whether the person is related to KPOP music.
I will give an example to show the codes of user story, which have already uploaded in the codes files. Ex: Assuming I am the customer who used this product >> I am really like Kpop music, and I am one of the fans of a Kpop star. >> I am looking forward to looking for someone who has similar interests to Kpop music. >> I use this product to find. >> I find a Kpop fan. >> From his or her Twitters, I find a lot of common ground. >> I add his or her Twitter account to make a friend.


2.Translate user stories to a modular design
模块化设计主要分为两个部分，第一部分搜索并且手机数据，第二个部分则是处理并且分析数据。在第一个部分中，我们可以用tweepy去抓取用户的数据，并抓取关键词kpop，通过抓取此关键词筛选出我们所想要的用户，这样的用户是曾经发表过关于kpop推特的用户。紧接着，在第二个部分中，我们使用NPL来处理我们已经抓到的用户发表的推特信息。用NPL来识别信息并且根据其判断打出分，如果分是个正数，则我们可以基本判定这个用户是喜欢kpop音乐的。反之，如果这个分是负数，我们也可以大概判定我们所抓取的用户可能并不喜欢kpop。这样就可以大大节省了用户从网站上漫无目的的搜索和自己同样爱好的朋友了。

3.Who is your user?
KPOP fans who have Twitter accounts

4.What are the basic user stories?
As for user stories, I hope that every customer who likes KPOP music can quickly find their favorite KPOP idol, or get to know more fans through this product. The product gives fans a quick way to get to know each other, as well as a chance to get to know each other's users on Twitter.
