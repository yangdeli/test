import http.client


def my_get(my_host,my_url):
	conn=http.client.HTTPConnection(my_host)
	conn.request("GET",my_url)
	r1=conn.getresponse()
	data1=r1.read()


	data2=data1.decode()
	pos1=data2.find("draw_list")
	pos1=data2.find("<tbody>",pos1)


	while True:
		sep1="<td class=\"td1\">"
		sep2="</td>"
		pos1=data2.find(sep1,pos1)
		if -1==pos1:
			break
		pos2=data2.find(sep2,pos1)
		l_date=data2[(pos1+len(sep1)):pos2]

		pos1=pos2
		sep1="<a";
		pos1=data2.find(sep1,pos1)
		sep1=">";
		pos1=data2.find(sep1,pos1)
		sep2="</a>"
		pos2=data2.find(sep2,pos1)
		l_index=data2[(pos1+len(sep1)):pos2]


		pos1=pos2
		sep1="<span class=\"ball_1\">"
		sep2="</span>"
		pos1=data2.find(sep1,pos1)
		pos2=data2.find(sep2,pos1)
		l_d1=data2[(pos1+len(sep1)):pos2]

		
		pos1=pos2
		sep1="<span class=\"ball_1\">"
		sep2="</span>"
		pos1=data2.find(sep1,pos1)
		pos2=data2.find(sep2,pos1)
		l_d2=data2[(pos1+len(sep1)):pos2]

		
		pos1=pos2
		sep1="<span class=\"ball_1\">"
		sep2="</span>"
		pos1=data2.find(sep1,pos1)
		pos2=data2.find(sep2,pos1)
		l_d3=data2[(pos1+len(sep1)):pos2]

		pos1=pos2
		sep1="<span class=\"ball_1\">"
		sep2="</span>"
		pos1=data2.find(sep1,pos1)
		pos2=data2.find(sep2,pos1)
		l_d4=data2[(pos1+len(sep1)):pos2]

		
		pos1=pos2
		sep1="<span class=\"ball_1\">"
		sep2="</span>"
		pos1=data2.find(sep1,pos1)
		pos2=data2.find(sep2,pos1)
		l_d5=data2[(pos1+len(sep1)):pos2]

		
		pos1=pos2
		sep1="<span class=\"ball_1\">"
		sep2="</span>"
		pos1=data2.find(sep1,pos1)
		pos2=data2.find(sep2,pos1)
		l_d6=data2[(pos1+len(sep1)):pos2]

		
		pos1=pos2
		sep1="<span class=\"ball_2\">"
		sep2="</span>"
		pos1=data2.find(sep1,pos1)
		pos2=data2.find(sep2,pos1)
		l_d7=data2[(pos1+len(sep1)):pos2]

		pos1=pos2

		l=l_date+";"+l_index+";"+l_d1+";"+l_d2+";"+l_d3+";"+l_d4+";"+l_d5+";"+l_d6+";"+l_d7+";"
		print(l)

for i in range(1,48):
	my_url="/lottery/draw/list/50?lottery_type=50&page="+str(i)+"&ds=2000-01-01&de=2012-08-27"
	my_get("baidu.lehecai.com",my_url)

