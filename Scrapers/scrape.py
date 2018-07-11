from urllib.request import urlopen
for i in range(3, 18):
	with urlopen('https://armorgames.com/community/thread/5246693/best-weapon-in-raze?page=' + str(i)) as response:
	    for line in response:
	        line = line.decode('utf-8')
	        if 'JuiceTin' in line:
	            print(i)

