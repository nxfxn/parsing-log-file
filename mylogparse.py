import sys
new={}

try:
    infile=open(sys.argv[1], "r")
except:
    print("Please include logfile path as a commandline argument.")
    sys.exit(2)

for line in infile:
    line=line.strip()
    
    if (len(line)==0 or line.startswith("Date")):
        continue
    
    date, ip, time, state = line.split()
    key, value=str(date), str(ip)
    
    if key in new and new[key].get(value) == None:
        new[key][value]={'Established':0, 'Failed':0, 'Syn':0}
        
    elif key not in new:
        new[key]={}
        new[key][value]={'Established':0, 'Failed':0, 'Syn':0}
    
    if str(state)=='Established': 
        new[key][value]['Established']+=1
    elif str(state)=='Failed':
        new[key][value]['Failed']+=1
    elif str(state)=='Syn':
        new[key][value]['Syn']+=1


print("\nOutput:\n--------\n")
for i in list(new):
    m=new.pop(i)
    for n,p in m.items():
        for q in p.items():
            if int(q[1])>0:
                print(i+"\t"+n+"\t\t"+str(q[0])+"\t"+str(q[1])+"\n")
