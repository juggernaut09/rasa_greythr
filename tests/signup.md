## greet + signup
* greet: Hi
  - action_greet_user
* signup: I want to signup
  - utter_can_do
  - form{"name": "signup_form"}
  - form{"name": null}

## just signup
* signup: I want to signup
  - utter_can_do
  - form{"name": "signup_form"}
  - form{"name": null}

## greet + signup + canthelp + continue
  * greet: Hi
    - action_greet_user
  * signup: I want to signup
    - utter_can_do
    - form{"name": "signup_form"}
  * canthelp: You can't help me stop this process
    - utter_canthelp
    - utter_ask_continue_signup
  * affirm: Yes
    - utter_great
    - signup_form
    - form{"name": null}

## greet + signup + canthelp + deny
  * greet: Hi
    - action_greet_user
  * signup: I want to signup
    - utter_can_do
    - form{"name": "signup_form"}
  * canthelp: You can't help me stop this process
    - utter_canthelp
    - utter_ask_continue_signup
  * deny: No
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just signup + canthelp + continue
  * signup: I want to signup
    - utter_can_do
    - form{"name": "signup_form"}
  * canthelp: You can't help me stop this process
    - utter_canthelp
    - utter_ask_continue_signup
  * affirm: Yes
    - utter_great
    - signup_form
    - form{"name": null}

## just signup + canthelp + deny
  * signup: I want to signup
    - utter_can_do
    - form{"name": "signup_form"}
  * canthelp: You can't help me stop this process
    - utter_canthelp
    - utter_ask_continue_signup
  * deny: No
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}


## greet + signup + explain + continue
  * greet: Hi
    - action_greet_user
  * signup: I want to signup
    - utter_can_do
    - form{"name": "signup_form"}
  * explain
    - action_explain_signup_form
    - utter_ask_continue_signup
  * affirm: Yes
    - utter_great
    - signup_form
    - form{"name": null}

## greet + signup + explain + deny
  * greet: Hi
    - action_greet_user
  * signup: I want to signup
    - utter_can_do
    - form{"name": "signup_form"}
  * explain
    - action_explain_signup_form
    - utter_ask_continue_signup
  * deny: No
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just signup + explain + continue
  * signup: I want to signup
    - utter_can_do
    - form{"name": "signup_form"}
  * explain
    - action_explain_signup_form
    - utter_ask_continue_signup
  * affirm: Yes
    - utter_great
    - signup_form
    - form{"name": null}

## just signup + explain + deny
  * signup: I want to signup
    - utter_can_do
    - form{"name": "signup_form"}
  * explain
    - action_explain_signup_form
    - utter_ask_continue_signup
  * deny: No
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## greet + signup + out_of_scope + continue
  * greet: Hi
    - action_greet_user
  * signup: I want to signup
    - utter_can_do
    - form{"name": "signup_form"}
  * out_of_scope: Give me some pizza
    - respond_out_of_scope
    - utter_ask_continue_signup
  * affirm: Yes
    - utter_great
    - signup_form
    - form{"name": null}

## greet + signup + out_of_scope + deny
  * greet: Hi
    - action_greet_user
  * signup: I want to signup
    - utter_can_do
    - form{"name": "signup_form"}
  * out_of_scope: Give me some pizza
    - respond_out_of_scope
    - utter_ask_continue_signup
  * deny: No
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just signup + out_of_scope + continue
  * signup: I want to signup
    - utter_can_do
    - form{"name": "signup_form"}
  * out_of_scope: Give me some pizza
    - respond_out_of_scope
    - utter_ask_continue_signup
  * affirm: Yes
    - utter_great
    - signup_form
    - form{"name": null}

## just signup + out_of_scope + deny
  * signup: I want to signup
    - utter_can_do
    - form{"name": "signup_form"}
  * out_of_scope: Give me some pizza
    - respond_out_of_scope
    - utter_ask_continue_signup
  * deny: No
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
