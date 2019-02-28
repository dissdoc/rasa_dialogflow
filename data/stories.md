## story 1
* greeting
    - utter_greeting

## story 1.1 greet & bye
* greeting
    - utter_greeting
* goodbye
    - utter_goodbye
    
## story 1.2 greet & meet
* greeting
    - utter_greeting
* meeting
    - action_person_name
    - utter_meeting
    
## story 3
* changing
    - utter_changing
    - utter_kind_of_guitar
    
## story 5 fender
* kind_of_guitar
    - slot {"kind_guitar": "fender"}
    - utter_answer_about_guitar 
    - action_price_fender
    - utter_no_fenders
    - utter_more
* goodbye
    - utter_goodbye
    
## story 6 gibson
* kind_of_guitar
    - slot {"kind_guitar": "gibson"}
    - utter_answer_about_guitar 
    - action_price_gibson
    - utter_exist_gibson
    - utter_order
* ordering
    - utter_more
* goodbye
    - utter_goodbye

## story 7 ibanez
* kind_of_guitar
    - slot {"kind_guitar": "ibanez"}
    - utter_answer_about_ibanez
    - utter_more
* goodbye
    - utter_goodbye
