from instabot import Bot
import time
import os
import random


def login(name, pw):
    choice = int(input("\nDo you want to use the default account where you logged before (1) or login to a new account? (2): "))
    if choice == 1:
        username = name
        passw = pw
    else:
        username = input("\nEnter the new username: ")
        passw = input("\nEnter the password: ")
    return username, passw



class User:

    def __init__(self, user, passw):
        self.user = user
        self.passw = passw


    def like(self):
        print("\nThis function allows you to like every post from a single user. \n")

        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        account = input("\nEnter the account to 'like': ")

        bot = Bot(max_likes_to_like = 0, like_delay = 5)
        bot.login(username = username, password = passw)
        photo = bot.get_user_medias(bot.get_user_id_from_username(account))

        for n in range (len(photo)): 
            print(f"Post number {n + 1} liked. If not, you liked this post before.")        
            bot.like(str(photo[n]))


    def comment(self):
        print("\nThis function allows you to comment every post from a single user.\n")
        
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        account = input("\nEnter the account to 'comment': ")
        comment = input("\nEnter the comment: ")

        bot = Bot (comment_delay = 10, max_comments_per_day= 10000)
        bot.login(username = username, password = passw)
        media = bot.get_total_user_medias(account)

        for n in range (len(media)):
            bot.comment(media[n], comment)
            print(f"\nPost number {n + 1} commented. If not, you commented this post before.")


    def follow(self):
        print("\nThis function allows you to follow every user's follower.\n")
        
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        account = input("\nEnter the account to 'follow' the followers: ")

        bot = Bot(follow_delay = 5, max_follows_per_day = 10000)
        bot.login(username = username, password = passw )
        people = bot.get_user_followers(bot.get_user_id_from_username(account))

        for n in range (len(people)):    
            bot.follow(str(people[n]))
            print(f"People followed: {n + 1}. If not, the person was already followed.")

  
    def direct(self):
        print("\nThis function allows you to send an amount of dm to a single user.\n")
    
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        account = input("\nEnter the recipient account: ")
        num = int(input("\nEnter the amount of dm to send: "))
        message = input("\nEnter the message: ")

        bot = Bot(message_delay = 5)
        bot.login(username = username, password = passw)
        account = bot.get_user_id_from_username(account)

        for n in range(num):     
            bot.send_message(message, account)
            print(f"\nDm number {n + 1} sent.")



class Hashtag:
        
    def __init__(self, user, passw):
        self.user = user
        self.passw = passw


    def like(self):
        print("\nThis function allows you to like every post under a particular hashtag.\n")
    
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        hshtg = input("\nEnter the hashtag: ")

        bot = Bot(max_likes_to_like = 0, like_delay = 5)
        bot.login(username = username, password = passw)

        bot.like_hashtag(hshtg)
        print("All post liked.")


    def comment(self): 
        print("\nThis function allows you to comment every post under a particular hashtag. \n")
    
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        hshtg = input("\nEnter the hashtag: ")
        comment = input("\nEnter the comment: ")

        bot = Bot (comment_delay = 10, max_comments_per_day= 10000)
        bot.login(username = username, password = passw)
        media = bot.get_total_hashtag_medias(hshtg)     

        for n in range (len(media)):
            bot.comment(media[n], comment)
            print(f"\nPost number {n + 1} commented. If not, you commented this post before.")


    def follow(self):
        print("\nThis function allows you to follow every user under a particular hashtag. \n")
      
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        hshtg = input("\nEnter the hashtag: ")

        bot = Bot(follow_delay = 5, max_follows_per_day = 10000)
        bot.login(username = username, password = passw )
        person = bot.get_hashtag_users(hshtg)
        
        for n in range (len(person)):    
            bot.follow(str(person[n]))
            print(f"People followed: {n + 1}. If not, the person was already followed.")


    def direct(self):
        print("\nThis function allows you to send a direct (every 20 seconds to avoid a temporary ban) to every user under a particular hashtag.\n")
    
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        hshtg = input("\nEnter the hashtag: ")
        message = input("\nEnter the message: ")

        bot = Bot(message_delay = 5)
        bot.login(username = username, password = passw)
        accounts = bot.get_hashtag_users(hshtg)

        for n in range(len(accounts)):     
            bot.send_message(message, accounts[n])
            print(f"\nDm number {n + 1} sent.")
            time.sleep(20)



class Post:

    def __init__(self, user, passw):
        self.user = user
        self.passw = passw


    def post(self):
        print("\nThis function allows you to post only a picture in loop every amount of time. The picture will be taken from a folder.\n")
    
        username, passw = login(self.user, self.passw)
        print("\n----------------------------")
        delay = int(input("\nEnter the amount of time from a post to another (seconds): "))
        photo = input("\nEnter the picture's folder path (for example: Desktop/images/): ")
        description = input("\nEnter the caption: ")

        bot = Bot()
        bot.login(username = username, password = passw)

        while(True):
            bot.upload_photo(photo, caption = description)
            print(f"\nPicture posted. If not, the picture doesn't have a correct aspect ratio. Try to resize it.\n\n")
            time.sleep(delay)
            os.rename(f'{photo}.REMOVE_ME', photo)


    def post_more(self):
            print("\nThis function allows you to post more different pictures every amount of time. The pictures will be taken from a folder.\n")
        
            username, passw = login(self.user, self.passw)
            print("\n----------------------------")
            delay = int(input("\nEnter the amount of time from a post to another (seconds):  "))
            path = input("\nEnter the pictures' folder path (for example: Desktop/images/):  ")

            print("\nEnter the captions. These captions will be inserted randomly under the posts. When you have finished, enter 'gg'.\n ")
            comments = []
            while(True):
                description = input("--> ")
                if description == "gg":
                    break 
                else: 
                    comments.append(description)

            print(f"\n***THESE CAPTIONS WILL BE INSERTED: {comments}***\n")

            bot = Bot()
            bot.login(username = username, password = passw)

            os.chdir(path)
            video = os.listdir()

            for n in range(len(video)):
                bot.upload_photo(str(video[n]), caption = random.choice(comments))
                print("Picture posted. If not, the picture doesn't have a correct aspect ratio. Try to resize it..\n\n")
                time.sleep(delay) 



print('''   \n\nSCRIPT MADE WITH INSTABOT, A PYTHON LIBRARY THAT USES OFFICIAL INSTAGRAM APIs. ALL RIGHTS RESERVED. 
    ALL THE ACTIVITIES RELATED TO BOTS ON YOUR ACCOUNT COULD BRING TO THE BAN IF USED IN AN INCORRECT WAY. I DON'T ASSUME ANY RESPONSIBILITY IF THIS MIGHT HAPPEN.''')

user = input("\n\nFirst, enter your account's name (don't worry, i don't care about your data.): ")
password = input("\nEnter the password: ")

print("\n\Welcome! The bot is starting...")
time.sleep(5) # cringe


while(True):
    action = int(input('''




██╗   ██╗ ██████╗ ██╗   ██╗██████╗     ██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗
╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
 ╚████╔╝ ██║   ██║██║   ██║██████╔╝    ██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║
  ╚██╔╝  ██║   ██║██║   ██║██╔══██╗    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
   ██║   ╚██████╔╝╚██████╔╝██║  ██║    ██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
                                                                                                                 
██╗   ██╗ ██████╗ ██╗   ██╗██████╗     ██████╗  ██████╗ ████████╗                                                
╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝                                                
 ╚████╔╝ ██║   ██║██║   ██║██████╔╝    ██████╔╝██║   ██║   ██║                                                   
  ╚██╔╝  ██║   ██║██║   ██║██╔══██╗    ██╔══██╗██║   ██║   ██║                                                   
   ██║   ╚██████╔╝╚██████╔╝██║  ██║    ██████╔╝╚██████╔╝   ██║                                                   
   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝                                                   
                                                                                                                 
                                                                    
                    CHOOSE THE TYPE OF CONTENT TO USE:
                    1 = USER: LIKE OR COMMENT THE POSTS OF A SPECIFIC USER, FOLLOW HIS FOLLOWER OR DM HIM
                    2 = HASHTAG: LIKE, COMMENT, FOLLOW OR DM ALL THE POSTS/USERS UNDER A SPECIFIC HASHTAG
                    3 = POST: UPLOAD ON INSTAGRAM A SINGLE POST OR MORE POST EVERY AMOUNT OF TIME
                    4 = EXIT

                    ---> '''))
    
    if action == 1:
        userData = User(user, password)           
        while(True):        
            action_user = int(input('''
                    
                    USER: 
                    1) LIKE ALL THE POSTS OF A SPECIFIC USER
                    2) COMMENT ALL THE POSTS OF A SPECIFIC USER
                    3) FOLLOW ALL THE FOLLOWERS OF A SPECIFIC USER
                    4) SEND UNLIMITED DMs TO A SPECIFIC USER
                    5) RETURN TO THE MAIN MENU
                    
                    --> '''))
            if action_user == 1:
                userData.like()
            elif action_user == 2:
                userData.comment()
            elif action_user == 3:
                userData.follow()
            elif action_user == 4:
                userData.direct()
            else:
                print("\Aight goodbye...\n")
                break


    elif action == 2:
        hashData = Hashtag(user, password)
        while(True):
            action_hashtag = int(input('''
                    
                    HASHTAG:
                    1) LIKE ALL THE POSTS OF A SPECIFIC HASHTAG
                    2) COMMENT ALL THE POSTS OF A SPECIFIC HASHTAG
                    3) FOLLOW ALL THE FOLLOWERS OF A SPECIFIC HASHTAG
                    4) SEND UNLIMITED DMs TO A SPECIFIC HASHTAG
                    5) RETURN TO THE MAIN MENU            
                    
                    --> '''))
            if action_hashtag == 1:
                hashData.like()
            elif action_hashtag == 2:
                hashData.comment()
            elif action_hashtag == 3:
                hashData.follow()
            elif action_hashtag == 4:
                hashData.direct()
            else:
                print("Aight goodbye...\n")
                break


    elif action == 3:
        postData = Post(user, password)
        while(True):        
            action_post = int(input('''
                
                POST:
                1) POST THE SAME PHOTO EVERY AMOUNT OF TIME
                2) POST DIFFERENT PHOTOS EVERY AMOUNT OF TIME
                3) RETURN TO THE MAIN MENU   
                
                --> '''))
            if action_post == 1:
                postData.post()
            elif action_post == 2:
                postData.post_more()
            else:
                print("\Aight goodbye...\n")
                break


    elif action == 4:
        print("\Aight goodbye...\n")
        time.sleep(5)
        break
   

    else:
        print("Wrong char, aight u funny")
        continue


# version 1.0, published on 10/10/2020
    
