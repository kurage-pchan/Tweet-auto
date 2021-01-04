import tweepy
import schedule
import time

CK =""
CS =""
AT =""
AS =""


auth = tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,AS)

api = tweepy.API(auth)

def tweet():
 api.update_status("おはようございます。")#ツイートしたいテキスト

schedule.every().day.at("17:00").do(tweet)#指定時刻
while True:
            schedule.run_pending()
            time.sleep(1)
import line_10