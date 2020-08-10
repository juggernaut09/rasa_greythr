## greet: Hi + signin
* greet: Hi
  - action_greet
* signin: I want to signin
  - utter_can_do
  - form{"name": "signin_form"}
  - form{"name": null}

## just signin
* signin: I want to signin
  - utter_can_do
  - form{"name": "signin_form"}
  - form{"name": null}

## greet: Hi + signin + canthelp + continue
  * greet: Hi
    - action_greet
  * signin: I want to signin
    - utter_can_do
    - form{"name": "signin_form"}
  * canthelp: You cannot help me.
    - utter_canthelp
    - utter_ask_continue_signin
  * affirm: Yes, Continue
    - utter_great
    - signin_form
    - form{"name": null}

## greet: Hi + signin + canthelp + deny
  * greet: Hi
    - action_greet
  * signin: I want to signin
    - utter_can_do
    - form{"name": "signin_form"}
  * canthelp: You cannot help me.
    - utter_canthelp
    - utter_ask_continue_signin
  * deny: No
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just signin + canthelp + continue
  * signin: I want to signin
    - utter_can_do
    - form{"name": "signin_form"}
  * canthelp: You cannot help me.
    - utter_canthelp
    - utter_ask_continue_signin
  * affirm: Yes, Continue
    - utter_great
    - signin_form
    - form{"name": null}

## just signin + canthelp + deny
  * signin: I want to signin
    - utter_can_do
    - form{"name": "signin_form"}
  * canthelp: You cannot help me.
    - utter_canthelp
    - utter_ask_continue_signin
  * deny: No
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}


## greet: Hi + signin + explain + continue
  * greet: Hi
    - action_greet
  * signin: I want to signin
    - utter_can_do
    - form{"name": "signin_form"}
  * explain: Why you need this?
    - action_explain_signin_form
    - utter_ask_continue_signin
  * affirm: Yes, Continue
    - utter_great
    - signin_form
    - form{"name": null}

## greet: Hi + signin + explain + deny
  * greet: Hi
    - action_greet
  * signin: I want to signin
    - utter_can_do
    - form{"name": "signin_form"}
  * explain: Why you need this?
    - action_explain_signin_form
    - utter_ask_continue_signin
  * deny: No
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just signin + explain + continue
  * signin: I want to signin
    - utter_can_do
    - form{"name": "signin_form"}
  * explain: Why you need this?
    - action_explain_signin_form
    - utter_ask_continue_signin
  * affirm: Yes, Continue
    - utter_great
    - signin_form
    - form{"name": null}

## just signin + explain + deny
  * signin: I want to signin
    - utter_can_do
    - form{"name": "signin_form"}
  * explain: Why you need this?
    - action_explain_signin_form
    - utter_ask_continue_signin
  * deny: No
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## greet: Hi + signin + out_of_scope + continue
  * greet: Hi
    - action_greet
  * signin: I want to signin
    - utter_can_do
    - form{"name": "signin_form"}
  * out_of_scope: Give me some pizza
    - respond_out_of_scope
    - utter_ask_continue_signin
  * affirm: Yes, Continue
    - utter_great
    - signin_form
    - form{"name": null}

## greet: Hi + signin + out_of_scope + deny
  * greet: Hi
    - action_greet
  * signin: I want to signin
    - utter_can_do
    - form{"name": "signin_form"}
  * out_of_scope: Give me some pizza
    - respond_out_of_scope
    - utter_ask_continue_signin
  * deny: No
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just signin + out_of_scope + continue
  * signin: I want to signin
    - utter_can_do
    - form{"name": "signin_form"}
  * out_of_scope: Give me some pizza
    - respond_out_of_scope
    - utter_ask_continue_signin
  * affirm: Yes, Continue
    - utter_great
    - signin_form
    - form{"name": null}

## just signin + out_of_scope + deny
  * signin: I want to signin
    - utter_can_do
    - form{"name": "signin_form"}
  * out_of_scope: Give me some pizza
    - respond_out_of_scope
    - utter_ask_continue_signin
  * deny: No
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
