# social media analyzer

ALL computing languages are using python

I use an example to explain what I did for this project. A homework (phase 2) in the class EC 601

1.Define MVP and user stories
2.Translate user stories to a modular design
3.Who is your user?
4.What are the basic user stories?

Introduction:
I designed this one to capture data from certain users on Twitter. What are my specific users? Young people who like KPOP music. A quick introduction to the product is to use Tweepy (which is a twitter API) to track if a user writes a keyword about any KPOP music. Then I will use natural language product (NLP) to understand each twitter message of this person in a more comprehensive way, and summarize each Twitter message to conclude whether this person is a fan group of KPOP.

1. Define MVP and user stories
The most basic feature (MVP) I want to implement is whether or not this person posts information about any KPOP in their Twitter feed. In other words, it gives a general sense of whether the person is related to KPOP music.
I will give an example to show the codes of user story, which have already uploaded in the codes files. Ex: Assuming I am the customer who used this product >> I am really like Kpop music, and I am one of the fans of a Kpop star. >> I am looking forward to looking for someone who has similar interests to Kpop music. >> I use this product to find. >> I find a Kpop fan. >> From his or her Twitters, I find a lot of common ground. >> I add his or her Twitter account to make a friend.


2.Translate user stories to a modular design
A modular design majorly has two parts for user stories. The first part is to search and collect the data from twitter acounts. Besides, the second part is to calculate, test and analyze data. In the first part, I wrote a code about tweepy, then we can use this method to catch the date from twitter acoounts. Then in the data where we colloected, we have to screen someone out who has a keyword "Kpop" in his or her Twitter.Moreover, in the second part, we have to use natural language product to test the data. According to the resules from NLP, we can define someone who likes Kpop music with earning a positive score, vice versa. Hence, it is really helpful to decrease the waste-time to find someone who is also one of the Kpop fans.

3.Who is your user?
KPOP fans who have Twitter accounts

4.What are the basic user stories?
As for user stories, I hope that every customer who likes KPOP music can quickly find their favorite KPOP idol, or get to know more fans through this product. The product gives fans a quick way to get to know each other, as well as a chance to get to know each other's users on Twitter.
