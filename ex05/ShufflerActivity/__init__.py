# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

def main(words:list) -> dict: #get input from mapper (words)

    shff = {} #match words with number of times they occure
    for word in words:
        if not shff.get(word[0]) :
            shff[word[0]] = list()
        shff[word[0]].append(word[1])
    return shff
