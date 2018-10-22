from operator import itemgetter
import datetime
import time
import praw

import pyrebase

config = {
    "apiKey": "AIzaSyDxElF7AUfRx5sNRJo60gm_vb-Igwu610g",
    "authDomain": "no-sleepers.firebaseapp.com",
    "databaseURL": "https://no-sleepers.firebaseio.com",
    "storageBucket": "no-sleepers.appspot.com",
    "serviceAccount": "No Sleepers-ebb792698a82.json"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
# authenticate a user
user = auth.sign_in_with_email_and_password("doughantke@gmail.com", "Advantage#1")
db = firebase.database()
print('Logging in...')
r = praw.Reddit(client_id='wVSz3FI-YtZIFQ', client_secret='HPHGrIJnfMGst9fbE4tKBOyMpW8',
                password='rapper304', user_agent='Collecting stories from /r/NoSleep and linking hidden gems',
                username='NoSleeper_Bot')
print(r.user.me())
print('Logged in')
# Searches NoSleep for underrated stories
while True:
    top5 = []
    subr = r.subreddit("nosleep")
    posts = subr.new(limit=100)
    print('Searching Subreddit...')
    for post in posts:
        liked = (post.upvote_ratio * 100)
        score = post.score
        if liked > 85 and score > 10 and score < 80:
            top5.append((post.title, post.author.name, post.url, (post.upvote_ratio * 100) + post.score, post.id))
            print(post.title, post.author.name, post.url, (post.upvote_ratio * 100) + post.score, post.id)
    # Sorts the Top 5 by Score
    newTop5 = sorted(top5, key=itemgetter(3))
    print('Posting to Subreddit...')
    now = datetime.datetime.now()
    print(now.strftime("%m-%d-%Y"))
    # Creates the Subreddit Post and Submits
    text = ('[' + newTop5[-1][0] + '](' + newTop5[-1][2] + ') - by /u/' + newTop5[-1][1] + '\n\n Bot Score: ' + str(
      newTop5[-1][3]) + '\n\n' +
          '[' + newTop5[-2][0] + '](' + newTop5[-2][2] + ') - by /u/' + newTop5[-2][1] + '\n\n Bot Score: ' + str(
      newTop5[-1][3]) + '\n\n' +
          '[' + newTop5[-3][0] + '](' + newTop5[-3][2] + ') - by /u/' + newTop5[-3][1] + '\n\n Bot Score: ' + str(
      newTop5[-3][3]) + '\n\n' +
          '[' + newTop5[-4][0] + '](' + newTop5[-4][2] + ') - by /u/' + newTop5[-4][1] + '\n\n Bot Score: ' + str(
      newTop5[-4][3]) + '\n\n' +
          '[' + newTop5[-5][0] + '](' + newTop5[-5][2] + ') - by /u/' + newTop5[-5][1] + '\n\n Bot Score: ' + str(
      newTop5[-5][3]) + '\n\n' +
          'Thank you for reading!')
    r.subreddit('NoSleepers').submit(title='NoSleepers for ' + now.strftime("%m-%d-%Y"), selftext=text)
    # Creates the database entries for each post and adds them
    story1 = {"title": newTop5[-1][0], "score": newTop5[-1][3], "author": newTop5[-1][1], "url": newTop5[-1][2],
              "certified": "false", "date": now.strftime("%m-%d-%Y")}
    db.child("Authors").push(story1, user['idToken'])

    story2 = {"title": newTop5[-2][0], "score": newTop5[-2][3], "author": newTop5[-2][1], "url": newTop5[-2][2],
              "certified": "false", "date": now.strftime("%m-%d-%Y")}
    db.child("Authors").push(story2, user['idToken'])

    story3 = {"title": newTop5[-3][0], "score": newTop5[-3][3], "author": newTop5[-3][1], "url": newTop5[-3][2],
              "certified": "false", "date": now.strftime("%m-%d-%Y")}
    db.child("Authors").push(story3, user['idToken'])

    story4 = {"title": newTop5[-4][0], "score": newTop5[-4][3], "author": newTop5[-4][1], "url": newTop5[-4][2],
              "certified": "false", "date": now.strftime("%m-%d-%Y")}
    db.child("Authors").push(story4, user['idToken'])

    story5 = {"title": newTop5[-5][0], "score": newTop5[-5][3], "author": newTop5[-5][1], "url": newTop5[-5][2],
              "certified": "false", "date": now.strftime("%m-%d-%Y")}
    db.child("Authors").push(story5, user['idToken'])

    print('Sending Private Messages...')
    #Creates the private messages to each author and sends them
    msgtext1 = ('Congratulations! Your story, [' + newTop5[-1][0] + '](' + newTop5[-1][2] + '), has been ' +
                'selected with a Bot Score of ' + str(newTop5[-1][3]) + ', to the NoSleepers subreddit.\n\n This ' +
                'subreddit is designed to find the hidden gems on NoSleep. You can visit the subreddit at /r/NoSleepers')

    msgtext2 = ('Congratulations! Your story, [' + newTop5[-2][0] + '](' + newTop5[-2][2] + '), has been ' +
                'selected with a Bot Score of ' + str(newTop5[-2][3]) + ', to the NoSleepers subreddit.\n\n This ' +
                'subreddit is designed to find the hidden gems on NoSleep. You can visit the subreddit at /r/NoSleepers')

    msgtext3 = ('Congratulations! Your story, [' + newTop5[-3][0] + '](' + newTop5[-3][2] + '), has been ' +
                'selected with a Bot Score of ' + str(newTop5[-3][3]) + ', to the NoSleepers subreddit.\n\n This ' +
                'subreddit is designed to find the hidden gems on NoSleep. You can visit the subreddit at /r/NoSleepers')

    msgtext4 = ('Congratulations! Your story, [' + newTop5[-4][0] + '](' + newTop5[-4][2] + '), has been ' +
                'selected with a Bot Score of ' + str(newTop5[-4][3]) + ', to the NoSleepers subreddit.\n\n This ' +
                'subreddit is designed to find the hidden gems on NoSleep. You can visit the subreddit at /r/NoSleepers')

    msgtext5 = ('Congratulations! Your story, [' + newTop5[-5][0] + '](' + newTop5[-5][2] + '), has been ' +
                'selected with a Bot Score of ' + str(newTop5[-5][3]) + ', to the NoSleepers subreddit.\n\n This ' +
                'subreddit is designed to find the hidden gems on NoSleep. You can visit the subreddit at /r/NoSleepers')
    r.redditor(newTop5[-1][1]).message('Your story has been selected by NoSleepers!', msgtext1)
    r.redditor(newTop5[-2][1]).message('Your story has been selected by NoSleepers!', msgtext2)
    r.redditor(newTop5[-3][1]).message('Your story has been selected by NoSleepers!', msgtext3)
    r.redditor(newTop5[-4][1]).message('Your story has been selected by NoSleepers!', msgtext4)
    r.redditor(newTop5[-5][1]).message('Your story has been selected by NoSleepers!', msgtext5)
    print('Bot Complete... Restarting...')
    print('Bot Completed...')
    print("Restarting Bot...")
    time.sleep(86400)

