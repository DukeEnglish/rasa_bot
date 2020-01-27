## greet
* greet
  - utter_greet

## general disease 
* disease
  - utter_working_on_it
  - action_report_general_disease
  - utter_bot_ending

## simple path
* disease_address{"address": "上海"}
  - utter_working_on_it
  - action_report_disease
  - utter_report_disease

## bad mood
* mood_unhappy
  - utter_help_heppier

## greet > Disease > address path
* greet
  - utter_greet
* disease_address{"address": "上海"}
  - utter_working_on_it
  - action_report_disease
  - utter_report_disease

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_bot_challenge

## ask advice
* advice
  - utter_advice
