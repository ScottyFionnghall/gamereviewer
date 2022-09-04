import steam_score
import random
# update game list
steam_score.updateGamesList()
name = input().strip('  ').lower()
# get review score 
score = steam_score.getReviewScore(steam_score.getAppID(name))
# list of reviews
review = {1:'terrible',2:'bad game',3:'meh',4:'good game',5:'masterpiece'}
if score:
    # make review score range from 0 to 10 to 1 to 5
    score = round(score*0.6)
    # 25% of the time script will give out opposite review
    if random.randint(0,100) <= 25:
        if score > 3:
            print(review[1])
        else:
            print(review[5])
    else:
        print(review[score])
