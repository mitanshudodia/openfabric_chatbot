import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
from chatbot import answer


############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    with open('knowledge','r') as file:
        knowledge = file.read()

    instruction = f'Instruction: given a dialog context, you need to response Scientifically'

    for text in request.text:
        response = answer(instruction, knowledge, [text])
        print(response)
        output.append(response)

    return SimpleText(dict(text=output))
