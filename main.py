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
    cp=str(pcent[i])
    if(len(cp)!=5):
        cp=cp+((5-len(cp))*" ")    
    rnd=round(pcent[i])
    ln=len(langs[i])
    print(langs[i]+" "*(12-ln)+cp+"% "+'█'*int(rnd/2)+"░"*int(25-int(rnd/2)))
