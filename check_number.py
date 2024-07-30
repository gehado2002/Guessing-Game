#!/usr/bin/env python
# coding: utf-8

# # Project 1 Guessing Game 

#  Guessing Game Project Description

# * **`First: You ask the user to set the game level:`**
#   * *(1) Easy*: 
#     * Limits : [1 - 10]  
#     * No. of trials : 3
#   * *(2) Intermediate*: 
#     * Limits : [1 - 100] 
#     * No. of trials : 7
#   * *(3) Hard* :  
#     * Limits : [1 - 1000] 
#     * No. of trials : 15
# 
# * **`Second: set the game settings according to the game level:`**
#   * set the `guess` to a number within the limits using `random` module 
#   * set the number of trials: `n_trials` 
# 
# * **`Finally: Play the game:`**
#   * Ask the user to guess the number:
#     * If he guessed it successfully : `print('Congratulations, you achieved it in {user_trials} trial') `
#     * if he failed:
#       * user_trials < n_trials: till him (Increase) or (Decrease)
#       * user_trials = n_trials: `print('You Lose!')`

# ## Show the game levels

# In[1]:


def show_levels():
  set_game_level=print("""(1) Easy:
\tLimits : [1 - 10]
\tNo. of trials : 3
(2) Intermediate:
\tLimits : [1 - 100]
\tNo. of trials : 7
(3) Hard :
\tLimits : [1 - 1000]
\tNo. of trials : 15
\t""")


# ## Ask the user for the game level

# In[2]:


def game_level_choice():
    game_level=input("""Enter the game level :
    (1) Easy 	 (2) Intermediate 	 (3) Hard 	\t""")
    return game_level 


# ## Set the game settings according to the game level:

# In[3]:


import random
def set_game_settings(game_level):
    if game_level == "1":
        limits=random.randint(1,10)
        n_trials=3
    elif game_level == "2":
        limits=random.randint(1,100)
        n_trials=7
    elif game_level == "3":
        limits=random.randint(1,1000)
        n_trials=15
    else :
        print("invalid level")
    return limits, n_trials


# ## Start Playing

# In[4]:


def start_play(limits, n_trials):
    user_trials=1
    while True:
        guess_number=int(input("I have a hidden number, guess it : "))
        if guess_number == limits :
            print(f'You got it successfully in {user_trials} trials')
            break
        elif guess_number > limits and user_trials<n_trials:
            print("No, decrease!")
        elif guess_number < limits and user_trials<n_trials:
            print("No, Increase!")
        elif user_trials == n_trials:
            print('You Lose!')
            break
        user_trials+=1


# ## Let's Play

# In[ ]:


def play():
  show_levels()
  game_level = game_level_choice()
  limits, n_trials = set_game_settings(game_level)
  start_play(limits, n_trials)


# In[ ]:


play()


# In[ ]:




