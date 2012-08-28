import re

f=open("1.dat","rt")

while True:
	l=f.readline()
	if 0==len(l):
		quit()
	
	r=re.compile(r"(.*);(.*);(.*);(.*);(.*);(.*);(.*);(.*);(.*);")
	m=r.match(l)

	my_date=m.group(1)
	r2=re.compile(r"(.*)-(.*)-(.*)")
	m2=r2.match(my_date)
	
	v=""
	my_div=2

	my_day=int(m2.group(2))
	if my_day%my_div:
		v+="1"
	else:
		v+="0"
	v+="      "

	my_sum=0
	for i in range(3,10):
		my_sum+=int(m.group(i))
	
	if my_sum%my_div:
		v+="1"
	else:
		v+="0"
	v+="      "

	if (my_day+my_sum)%2:
		v+="1"
	else:
		v+="0"

	print(v)
	#quit()