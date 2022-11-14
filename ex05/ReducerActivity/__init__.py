# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

def main(words: dict) -> dict:
   red = {key: sum(value) for key, value in words.items()} #get items of dictionary
   return red #return dictionary with words and number of times they occur

