import requests

import re

from django.http import HttpResponse
from django.template import loader


def index(request):
	return HttpResponse("Hello Oct Holiday")

def detail(request, page_id):
	r = requests.get('https://hpjav.tv/category/censored/page/'+str(page_id), verify=False)
	pattern = re.compile('<img (.*?) data-original="(.*?)" src="(.*?)" alt="(.*?)">', re.S)
	items = re.findall(pattern, r.text)

	latest_list = []
	for item in items:
		#print(item[1], item[3])
		new_item = {}
		new_item['url'] = "https://www.javbus.com/" + item[3].split()[0]
		new_item['url_watch'] = "https://bejav.net/" + item[3].split()[0]
		new_item['img'] = item[1]
		new_item['img_big'] = item[1].replace("-s", "")
		latest_list.append(new_item)
	template = loader.get_template('ruby/index.html')
	context = {
	    'latest_list': latest_list,
	    'page_id_pre': page_id-1,
	    'page_id_post': page_id+1,
	}
	return HttpResponse(template.render(context, request))
