from .models import Post , Followers
from django.shortcuts import render , redirect , get_object_or_404,HttpResponseRedirect

def count_lames(user):
	qs = Post.objects.filter(user = user )
	count = 0
	for post in qs:
		lames = post.lames.all().count()
		count += lames
	return (count)

def count_likes(user):
	qs = Post.objects.filter(user = user )
	count = 0
	for post in qs:
		likes = post.likes.all().count()
		count += likes
	return (count)

def count_result(n,result):
	return result[:n]

def get_followers(user):
	if Followers.objects.all():
		object_all = get_object_or_404(Followers,user=user)
		howis = object_all.followers.all().order_by("username")
		return howis

def get_rank(points):
	if 0<= points<10000:
		rank = 1
	elif 10000<=points<30000:
		rank = 2
	elif 30000<=points<90000:
		rank = 3
	elif 90000<=points<180000:
		rank = 4
	elif points>=180000:
		rank = 5	
	elif -10000<points<0:
		rank = 1
	elif -30000<points<-10000:
		rank = -1
	elif -90000<points<-30000:
		rank = -2
	elif -180000<points<-90000:
		rank = -3
	elif -360000<points<-180000:
		rank = -4
	elif -360000>points:
		rank = -5

	return rank



def post_exit(id,step,check):
	int_id = int(id)
	search_id = int_id+step
	search_kw = str(search_id)
	qsn = Post.objects.filter(id=search_kw)
	current = get_object_or_404(Post,id=id)
	first = Post.objects.first() 
	last = Post.objects.last()
	if current == last and check == "p":
		return None
	elif current == first and check == "n":
		return None
	else:
		while not qsn:
			step += step
			search_id= int_id + step
			search_kw = str(search_id)
			qsn = Post.objects.filter(id=search_kw)
	
	if qsn:
		for i in qsn:
			return i.id

def set_vedio(a):
		url = a
		youtube,name = url.split("watch?v=")
		if "&" in name:
			name2,rub = name.split("&")
			vedio_url = "https://www.youtube.com/embed/"+name2+"?ecver=2"
		else:
			vedio_url = "https://www.youtube.com/embed/"+name+"?ecver=2"
		return vedio_url


	