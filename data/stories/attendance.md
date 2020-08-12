## greet + signin+ just attendance
* greet
  - action_greet_user
* signin
  - utter_can_do
  - signin_form
  - form{"name": "signin_form"}
  - form{"name": null}
* mark_attendance
  - utter_can_do
  - action_mark_attendance
* goodbye
  - utter_thumbsup
  - utter_goodbye

## greet + signup+ just attendance
* greet
  - action_greet_user
* signup
  - utter_can_do
  - signup_form
  - form{"name": "signup_form"}
  - form{"name": null}
* mark_attendance
  - utter_can_do
  - action_mark_attendance
* goodbye
  - utter_thumbsup
  - utter_goodbye


## signin + attendance+goodbye
* signin
  - utter_can_do
  - signin_form
  - form{"name": "signin_form"}
  - form{"name": null}
* mark_attendance
  - utter_can_do
  - action_mark_attendance
* goodbye
  - utter_thumbsup
  - utter_goodbye

## signup + attendance+goodbye
* signup
  - utter_can_do
  - signup_form
  - form{"name": "signup_form"}
  - form{"name": null}
* mark_attendance
  - utter_can_do
  - action_mark_attendance
* goodbye
  - utter_thumbsup
  - utter_goodbye

## signup+ attendace
* signup
  - utter_can_do
  - signup_form
  - form{"name": "signup_form"}
  - form{"name": null}
* mark_attendance
  - utter_can_do
  - action_mark_attendance

## signin + attendance
* signin
  - utter_can_do
  - signin_form
  - form{"name": "signin_form"}
  - form{"name": null}
* mark_attendance
  - utter_can_do
  - action_mark_attendance

## only attendace
* mark_attendance
  - utter_can_do
  - action_mark_attendance

## just analysis
* analysis
  - utter_can_do
  - action_attendance_analysis
