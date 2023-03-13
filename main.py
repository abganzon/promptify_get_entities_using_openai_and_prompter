#install this first 
#!pip3 install git+https://github.com/promptslab/Promptify.git
#!pip install openai

from promptify import OpenAI
from promptify import Prompter
import json

f = open('/content/2023-02-22-9d17a902-0358-461c-b293-72f56bc5b4eb.txt',)
data = json.load(f)
print(data['text']) 

sentence     =  data['text']
api_key  = "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"
model        = OpenAI(api_key)
nlp_prompter = Prompter(model)


result       = nlp_prompter.fit('ner.jinja',
                          domain      = 'medical',
                          text_input  = sentence, 
                          labels      = ["SYMPTOM", "DISEASE", "PERSON", "ORGANIZATION", "ADDRESS", "LOCATION", "ZIP_CODE", "PHONE_NUMBER"])

#print(result['text'])

# Replace single quotes with double quotes
json_str = result['text'].replace("'", '"')

# Parse the JSON object
json_obj = json.loads(json_str)

results = {}

for entity in json_obj:
    if 'T' in entity:
        if entity['T'] == 'LOCATION':
            if 'Location' in results:
                if entity['E'] not in results['Location']:
                    results['Location'] += ' ' + entity['E']
            else:
                results['Location'] = entity['E']
        elif entity['T'] == 'ZIP_CODE':
            if 'ZipCode' in results:
                if entity['E'] not in results['ZipCode']:
                    results['ZipCode'] += ' ' + entity['E']
            else:
                results['ZipCode'] = entity['E']
        elif entity['T'] == 'ADDRESS':
            if 'Address' in results:
                if entity['E'] not in results['Address']:
                    results['Address'] += ' ' + entity['E']
            else:
                results['Address'] = entity['E']
        elif entity['T'] == 'PHONE_NUMBER':
            if 'Priority Number' in results:
                if entity['E'] not in results['Priority Number']:
                    results['Priority Number'] += ',' + entity['E']
            else:
                results['Priority Number'] = entity['E']
        elif entity['T'] == 'ORGANIZATION':
            if 'Organization' in results:
                if entity['E'] not in results['Organization']:
                    results['Organization'] += ',' + entity['E']
            else:
                results['Organization'] = entity['E']
        elif entity['T'] == 'PERSON':
            if 'Name' in results:
                if entity['E'] not in results['Name']:
                    results['Name'] += ',' + entity['E']
            else:
                results['Name'] = entity['E']
        elif entity['T'] == 'DISEASE':
            if 'Disease' in results:
                if entity['E'] not in results['Disease']:
                    results['Disease'] += ',' + entity['E']
            else:
                results['Disease'] = entity['E']
        elif entity['T'] == 'SYMPTOM':
            if 'Symptom' in results:
                if entity['E'] not in results['Symptom']:
                    results['Symptom'] += ',' + entity['E']
            else:
                results['Symptom'] = entity['E']
print(results)
