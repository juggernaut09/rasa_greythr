## happy path
* greet
  - action_greet_user
* mood_great
  - utter_happy

## sad path 1
* greet
  - action_greet_user
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_great

## sad path 2
* greet
  - action_greet_user
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_thumbsup
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## greet + out_of_scope
* greet
  - action_greet_user
* out_of_scope
  - respond_out_of_scope
## just out_of_scope
* out_of_scope
  - respond_out_of_scope

## greet + out_of_scope + goodbye
  * greet
    - action_greet_user
  * out_of_scope
    - respond_out_of_scope
  * goodbye
    - utter_goodbye
## just out_of_scope + goodbye
  * out_of_scope
    - respond_out_of_scope
  * goodbye
    - utter_goodbye
