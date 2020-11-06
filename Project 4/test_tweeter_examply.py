import unittest
import twitter_example
import os


class MyTestCase(unittest.TestCase):
    def test_fetch_successful(self):
        """
        test
        :return:
        """
        access_token = os.getenv('ACCESS_TOKEN')
        access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
        consumer_key = os.getenv('CONSUMER_KEY')
        consumer_secret = os.getenv('CONSUMER_SECRET')

        res = twitter_example.fecth_random_tweets(ck, cs, at, ats)

        txt = []
        for tweet in res:
            txt.append(tweet.text)
        print(txt)


        self.assertEqual(1, len(txt))




if __name__ == '__main__':
    unittest.main()
