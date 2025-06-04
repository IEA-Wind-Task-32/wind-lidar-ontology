#%% import modules
import urllib, requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os
from typing import Dict
os.environ['no_proxy'] = '*' 

#%% setup the webpage for reading
url = "https://data.windenergy.dtu.dk/ontologies/view/ontolidar/en/index"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
base_url  = soup.base['href']

# finding alternative languages
lang_url = {x['href'] for x in soup.find_all("a", class_="versal")}

# find the terms in the ontology viewers
results = soup.find_all("a")
res_links = {x['href'] for x in results if "ontolidar/en/page" in x['href']}
pages = [(base_url + r) for r in res_links]
pages = sorted(pages)

#%% create a definition for the operation here onwards: here we performed a demo for one ontology definition
def get_definition(page: str) -> Dict:
    
    r1 = requests.get(page)
    s1 = BeautifulSoup(r1.content, "html.parser")
    skos = {}

    # get the identifier
    skos['identifier'] = 'ontolidar:' + str(page).split('/')[-1]
    lang = str(page).split('/')[-3]

    # get the preferred term
    term = s1.title.string.split(': ')
    skos[f'prefLabel@{lang}'] = term[-1]
    
    # get the cfConvention label
    skos['ontolidar:cfConvention'] = None
    

    # get the definitions
    ss = s1.find_all("span", class_="versal col-xs-6")
    str_list = [s.string for s in list(reversed(ss))]
    temp_defs = {str_list[2*i].replace(' ', ''): str_list[2*i+1] for i in range(int(len(str_list)/2))}
    langs_dict = {'English': 'en', 'Italian': 'it', 'Spanish': 'es', 'cn': 'cn', 'German': 'de'}
    for k, v in temp_defs.items():
        skos[f'definition@{langs_dict[k]}'] = v
    
    # get the altLabel
    
    
    # get the broader concept
    s2 = s1.find_all(class_="property-value-wrapper")
    s3 = [s.find('li').find('a', href=True) for s in s2 if s.find('li')!=None]                
    broad_link = s3[0]['href']
    broad_text = s3[0].string.lstrip()

    # get the hierarchy
    s2 = s1.find_all(class_='propertyvalue bread-crumb')
    defs = {}
    for s in s2:
        defs[s.string.lower()] = s['href']

    return defs

for page in pages:
    print(page)
    def1 = get_definition(page)
    break    

#%%
def webpage2dict(page)-> dict:

    import ast
    import requests
    from bs4 import BeautifulSoup
    
    r1 = requests.get(page)
    s1 = BeautifulSoup(r1.content, "html.parser")

    v1 = s1.find_all("script", type="application/ld+json")[0]

    v2 = ast.literal_eval(v1.string.lstrip())

    import json
    d = json.loads(v1.string.lstrip())

    def dict_serialize(d) -> dict:
        for k, v in d.items():
            print(k)
            if isinstance(v, dict):
                dct1 = v
            elif isinstance(v, list):
                if len(v) > 3:
                    # drop other concepts which are the broader and narrower concepts
                    v = [vv for vv  in v if 'skos:definition' in vv]
                # concept keys of importance
                keys = ['scheme', 'concept', 'broader']
                dct2 = {kk: vv for kk, vv in zip(keys, v)}
            else:
                raise ValueError(f"Unexpected value type: {type(v)}, value: {v}")

        dct = {**dct1, **dct2}
        return dct

    dct = dict_serialize(d)
    return dct

def onto2dict(dct) -> dict:
    out = dict()
    
    # not so used elements
    out['ontolidar:cfConvention'] = None
    out['rdf:type'] = None
    out['rdfs:label'] = None
    out['ontolidar:units'] = None
    out['skos:related'] = None
    out['skos:exactMatch'] = None
    out['dct:creator'] = None
    out['dct:contributor'] = None

    # the main identifier
    out['identifier'] = dct['concept']['uri']

    # preferred label
    for v in dct['concept']['prefLabel']:
        out[f'skos:prefLabel@{v['lang']}'] = v['value']

    # definitions
    try:
        for v in dct['concept']['skos:definition']:
            out[f'skos:definition@{v['lang']}'] = v['value']
    except KeyError:
        for v in dct['broader']['skos:definition']:
            out[f'skos:definition@{v['lang']}'] = v['value']
            
    # alternate label
    try:
        out['skos:altLabel'] = dct['concept']['altLabel']['value']
    except TypeError:
        out['skos:altLabel'] = ", ".join([list['value'] for list in dct['concept']['altLabel']])
    except KeyError:
        out['skos:altLabel'] = None
        print(f"KeyError: 'altLabel' not found in {dct['concept']['uri']}")
    try:
        out['skos:broader'] = dct['concept']['broader']['uri']
    except KeyError:
        out['skos:broader'] = None
        print(f"KeyError: 'broader' not found in {dct['concept']['uri']}")

    # editorial notes
    try:
        for v in dct['concept']['skos:editorialNote']:
            out[f'skos:editorialNote@{v['lang']}'] = v['value']
    except KeyError:
        out[f'skos:editorialNote@{v['lang']}'] = None
        print(f"KeyError: 'editorialNote' not found in {dct['concept']['uri']}")

    # notes
    try:
        for v in dct['concept']['skos:note']:
            out[f'skos:note@{v['lang']}'] = v['value']
    except KeyError:
        for v in dct['concept']['prefLabel']:
            out[f'skos:note@{v['lang']}'] = None

    return out

import pandas as pd
df = pd.DataFrame()
for i, page in enumerate(pages):
    dct = webpage2dict(page)
    out = onto2dict(dct)
    df = pd.concat([df, pd.DataFrame(out, index=[i])], axis=1)
    if i == 2:
        break
    
        


# %%
import sys
import json
sys.path.append(r"c:\Users\GiyananiA\OneDrive - Nordex SE\projects\user_modules")
from metadata_helpers import json_serialize, as_dict

for k, v in d.items():
    if isinstance(v, dict):
        dct = v
    elif isinstance(v, list):
        print(f"List found for key {k}, converting to dict")
    else:
        dct = v
        
    json_obj = json.dumps(dct, indent=4, default=lambda x: json_serialize(x))
    print(json_obj)

# %%
