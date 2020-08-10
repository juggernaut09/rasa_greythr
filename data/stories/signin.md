## greet + signin
* greet
  - action_greet_user
* signin
  - utter_can_do
  - signin_form
  - form{"name": "signin_form"}
  - form{"name": null}

## just signin
* signin
  - utter_can_do
  - signin_form
  - form{"name": "signin_form"}
  - form{"name": null}

## greet + signin + canthelp + continue
  * greet
    - action_greet_user
  * signin
    - utter_can_do
    - signin_form
    - form{"name": "signin_form"}
  * canthelp
    - utter_canthelp
    - utter_ask_continue_signin
  * affirm
    - utter_great
    - signin_form
    - form{"name": null}

## greet + signin + canthelp + deny
  * greet
    - action_greet_user
  * signin
    - utter_can_do
    - signin_form
    - form{"name": "signin_form"}
  * canthelp
    - utter_canthelp
    - utter_ask_continue_signin
  * deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just signin + canthelp + continue
  * signin
    - utter_can_do
    - signin_form
    - form{"name": "signin_form"}
  * canthelp
    - utter_canthelp
    - utter_ask_continue_signin
  * affirm
    - utter_great
    - signin_form
    - form{"name": null}

## just signin + canthelp + deny
  * signin
    - utter_can_do
    - signin_form
    - form{"name": "signin_form"}
  * canthelp
    - utter_canthelp
    - utter_ask_continue_signin
  * deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}


## greet + signin + explain + continue
  * greet
    - action_greet_user
  * signin
    - utter_can_do
    - signin_form
    - form{"name": "signin_form"}
  * explain
    - action_explain_signin_form
    - utter_ask_continue_signin
  * affirm
    - utter_great
    - signin_form
    - form{"name": null}

## greet + signin + explain + deny
  * greet
    - action_greet_user
  * signin
    - utter_can_do
    - signin_form
    - form{"name": "signin_form"}
  * explain
    - action_explain_signin_form
    - utter_ask_continue_signin
  * deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just signin + explain + continue
  * signin
    - utter_can_do
    - signin_form
    - form{"name": "signin_form"}
  * explain
    - action_explain_signin_form
    - utter_ask_continue_signin
  * affirm
    - utter_great
    - signin_form
    - form{"name": null}

## just signin + explain + deny
  * signin
    - utter_can_do
    - signin_form
    - form{"name": "signin_form"}
  * explain
    - action_explain_signin_form
    - utter_ask_continue_signin
  * deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## greet + signin + out_of_scope + continue
  * greet
    - action_greet_user
  * signin
    - utter_can_do
    - signin_form
    - form{"name": "signin_form"}
  * out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_signin
  * affirm
    - utter_great
    - signin_form
    - form{"name": null}

## greet + signin + out_of_scope + deny
  * greet
    - action_greet_user
  * signin
    - utter_can_do
    - signin_form
    - form{"name": "signin_form"}
  * out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_signin
  * deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just signin + out_of_scope + continue
  * signin
    - utter_can_do
    - signin_form
    - form{"name": "signin_form"}
  * out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_signin
  * affirm
    - utter_great
    - signin_form
    - form{"name": null}

## just signin + out_of_scope + deny
  * signin
    - utter_can_do
    - signin_form
    - form{"name": "signin_form"}
  * out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_signin
  * deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
