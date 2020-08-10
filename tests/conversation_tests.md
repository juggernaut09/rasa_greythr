## happy path
* greet: Hi
  - action_greet_user
* mood_great: I am fine
  - utter_happy

## sad path 1
* greet: Hi
  - action_greet_user
* mood_unhappy: I am sad
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_great

## sad path 2
* greet: Hi
  - action_greet_user
* mood_unhappy: I am sad
  - utter_cheer_up
  - utter_did_that_help
* deny: No
  - utter_thumbsup
  - utter_goodbye

## say goodbye
* goodbye: Bye
  - utter_goodbye

## bot challenge
* bot_challenge: Are you a bot?
  - utter_iamabot

## greet + out_of_scope
* greet: Hi
  - action_greet_user
* out_of_scope: Order me some pizza?
  - respond_out_of_scope
## just out_of_scope
* out_of_scope: Order me some pizza?
  - respond_out_of_scope

## greet + out_of_scope + goodbye
  * greet: Hi
    - action_greet_user
  * out_of_scope: Order me some pizza?
    - respond_out_of_scope
  * goodbye: Bye
    - utter_goodbye
## just out_of_scope + goodbye
  * out_of_scope: Order me some pizza?
    - respond_out_of_scope
  * goodbye: Bye
    - utter_goodbye

## signout
  * signout: I want to signout.
    - utter_thumbsup
    - action_signout
