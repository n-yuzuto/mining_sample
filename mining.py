import hashlib

dat = "sample_minig20210429RANDOM" 
hs = hashlib.sha256(dat.encode()).hexdigest()
l = ["0","1","2","3"]
n = 0
while (hs[:8] != "00000000" and hs[:8] != "00000001" and hs[:8] != "00000002" and hs[:8] != "00000003"):
    dat = "sample_mining20210429RANDOM" 
    dat = dat + str(n)
    hs = hashlib.sha256(dat.encode()).hexdigest()
    n += 1

print(dat)
print(hs)