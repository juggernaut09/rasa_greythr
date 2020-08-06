## greet + signup
* greet
  - action_greet_user
* signup
  - utter_can_do
  - form{"name": "signup_form"}
  - form{"name": null}

## just signup
* signup
  - utter_can_do
  - form{"name": "signup_form"}
  - form{"name": null}

## greet + signup + canthelp + continue
  * greet
    - action_greet_user
  * signup
    - utter_can_do
    - form{"name": "signup_form"}
  * canthelp
    - utter_canthelp
    - utter_ask_continue_signup
  * affirm
    - utter_great
    - signup_form
    - form{"name": null}

## greet + signup + canthelp + deny
  * greet
    - action_greet_user
  * signup
    - utter_can_do
    - form{"name": "signup_form"}
  * canthelp
    - utter_canthelp
    - utter_ask_continue_signup
  * deny
    - utter_great
    - action_deactivate_form
    - form{"name": null}

## just signup + canthelp + continue
  * signup
    - utter_can_do
    - form{"name": "signup_form"}
  * canthelp
    - utter_canthelp
    - utter_ask_continue_signup
  * affirm
    - utter_great
    - signup_form
    - form{"name": null}

## just signup + canthelp + deny
  * signup
    - utter_can_do
    - form{"name": "signup_form"}
  * canthelp
    - utter_canthelp
    - utter_ask_continue_signup
  * deny
    - utter_great
    - action_deactivate_form
    - form{"name": null}


## greet + signup + explain + continue
  * greet
    - action_greet_user
  * signup
    - utter_can_do
    - form{"name": "signup_form"}
  * explain
    - action_explain_signup_form
    - utter_ask_continue_signup
  * affirm
    - utter_great
    - signup_form
    - form{"name": null}

## greet + signup + explain + deny
  * greet
    - action_greet_user
  * signup
    - utter_can_do
    - form{"name": "signup_form"}
  * explain
    - action_explain_signup_form
    - utter_ask_continue_signup
  * deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just signup + explain + continue
  * signup
    - utter_can_do
    - form{"name": "signup_form"}
  * explain
    - action_explain_signup_form
    - utter_ask_continue_signup
  * affirm
    - utter_great
    - signup_form
    - form{"name": null}

## just signup + explain + deny
  * signup
    - utter_can_do
    - form{"name": "signup_form"}
  * explain
    - action_explain_signup_form
    - utter_ask_continue_signup
  * deny
    - utter_great
    - action_deactivate_form
    - form{"name": null}

## greet + signup + out_of_scope + continue
  * greet
    - action_greet_user
  * signup
    - utter_can_do
    - form{"name": "signup_form"}
  * out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_signup
  * affirm
    - utter_great
    - signup_form
    - form{"name": null}

## greet + signup + out_of_scope + deny
  * greet
    - action_greet_user
  * signup
    - utter_can_do
    - form{"name": "signup_form"}
  * out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_signup
  * deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just signup + out_of_scope + continue
  * signup
    - utter_can_do
    - form{"name": "signup_form"}
  * out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_signup
  * affirm
    - utter_great
    - signup_form
    - form{"name": null}

## just signup + out_of_scope + deny
  * signup
    - utter_can_do
    - form{"name": "signup_form"}
  * out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_signup
  * deny
    - utter_great
    - action_deactivate_form
    - form{"name": null}
