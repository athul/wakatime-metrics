import json,sys
if len(sys.argv)<2:
    print("Wakatime's Filename.json")
    sys.exit()
file=' '.join(sys.argv[1:])
with open(file) as f:
    dat=json.load(f)
langs=[]
pcent=[]
for item in dat['data']:
    langs.append(item['name'])
    pcent.append(item['percent'])
l_langs=len(langs)
for i in range(l_langs):
    rnd=round(pcent[i])
    print(langs[i]+'|'+str(pcent[i])+"%|"+'█'*int(rnd/2)+"░"*int(25-int(rnd/2)))
