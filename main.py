import json,sys

if len(sys.argv)<2:
    print("Wakatime's Filename.json")
    sys.exit()
file=' '.join(sys.argv[1:])
"""dat={
        "data": [
        {"name": "JavaScript", "percent": 66.07},
        {"name": "Markdown", "percent": 14.85},
        {"name": "JSON", "percent": 11.99},
        {"name": "Git", "percent": 3.83},
        {"name": "YAML", "percent": 3.26},
        {"name": "Other", "percent": 0},
        {"name": "Python", "percent": 0}
]
}"""
with open(file) as f:
    dat=json.load(f)
langs=[]
pcent=[]
for item in dat['data']:
    langs.append(item['name'])
    pcent.append(item['percent'])
l_langs=len(langs)
for i in range(l_langs):
    print(langs[i]+'   '+'█'*int(pcent[i])+"  "+str(pcent[i])+"%")

