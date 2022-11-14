# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json
import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    
    #run locally 
    #input = []
    #for i in range(1,5):
    #    filename = f'mrinput-{i}.txt'
    #    myfile = open(filename,'r')
    #    data = myfile.read()
    #    input += data.replace('\r', '').split("\n")
    #    print(input[i])
    #    myfile.close()

    #download from blob storage
    input = yield context.call_activity('GetInputDataFn')

    tasks = []
    for line in input:
        tasks.append(context.call_activity("MapperActivity", line))
    mpp = yield context.task_all(tasks)
    
    flat_mpp = [item for sub in mpp for item in sub]

    shff = yield context.call_activity('ShufflerActivity', flat_mpp)
    
    tasks = []
    for word, num in shff.items():
        tasks.append(context.call_activity("ReducerActivity", {word: num}))
    red = yield context.task_all(tasks)
    
    return [red]

main = df.Orchestrator.create(orchestrator_function)