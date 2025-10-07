import <time datetime=""></time>
mag = [1,2,3,4,5,6,7,8,9,10,11,12,13]

while len(mag) > 1:
 time.sleep(0.9) 
 pull = mag.pop()
release = mag.pop()
print(f"(Pull) FA: {pull}")
print(f"(Release) FA: {release}")
If mag:
time.sleep(0.9)
print(f"(Pull) FA: {mag.pop()}")

print("Mag Empty!")
