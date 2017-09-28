import os
import requests
import sys

from bs4 import BeautifulSoup


base_dir = '/root/flask_project'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def soupify(req):
	try:
		soup = BeautifulSoup(req.text, "html5lib")
		return soup
	except Exception as e:
		print str(e)
	
def getimages(soup):
	image_src = []
	for items in soup.find_all('img'):
		image_src.append(items['src'])
	return image_src

def get_request(website):
	try:
		req = requests.get(website, headers=headers)
		if req.status_code == 200:
			return req.status_code, req
		return req.status_code, None
	except ConnectionError:
		return None, "Connection Error"
	except Exception as e:
		return None, str(e)

def downloader(path='urls.txt'):
	try:
		with open(path, 'r') as f:
			return f.readlines()
	except Exception as e:
		print str(e), " Please check the file path"
		
def check_file_path():
	if not os.path.exists(os.path.join(base_dir, 'downloads')):
		os.mkdir(os.path.join(base_dir, 'downloads'))
	try:
		filepath = sys.argv[1]
		if not os.path.exists(filepath):
			print "File path does not exist"
			sys.exit()
	except IndexError:
		print "Please pass the file path with script"
		sys.exit()
	return filepath
	
def mapper(items):
	link = get_request(items.strip('\n'))
	linktype = items.split(':')[0]
	if link[0] == 200:
		soup = soupify(link[1])
		img_list = getimages(soup)
		for image in img_list:
			img_url = ':'.join([linktype, image])
			filename = img_url.split('/')[-1]
			filepath = os.path.join(base_dir, 'downloads', filename)
			ireq = get_request(img_url)
			if ireq[0] == 200:
				with open(filepath, 'wb') as img:
					img.write(ireq[1].content)
				ireq[1].close()
			else:
				print ireq
	else:
		print link

def main():
	filepath = check_file_path()
	allurls = downloader(filepath)
	map(mapper, allurls)

	
if __name__ == '__main__':
	main()
