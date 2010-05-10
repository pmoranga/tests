from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from shorturl.surl.models import URL
import datetime
import hashlib

def create_or_get_hash(url):
  '''Cria hash nao existente, e caso ja exista hash para essa url retorna ela.'''
  m = hashlib.md5()
  m.update(url)
  fullhash = m.hexdigest()
  # Vou pegando os 6 primeiros caracteres do hash, ate achar um ainda nao existente
  for i in range(m.digest_size-6):
    hash = fullhash[i:i+6]
    try:
      u = URL.objects.get(short_url = hash)
      if (u.full_url == url):
      # Se ja existir essa url retorno o objeto existente
        return u;
    except(KeyError, URL.DoesNotExist):
      break
  u = URL( full_url=url, short_url=hash, pub_date=datetime.datetime.now() )
  u.save()
  return u

def index(request):
  if request.method == 'GET':
    return render_to_response('surl/index.html')
  else:  
    url = request.POST['full_url']
    u = create_or_get_hash(url)
    burl = "http://" + request.get_host() 
    return render_to_response('surl/index.html',{'u':u, "burl": burl, })


def open_surl(request, url_id):
  u = get_object_or_404(URL, short_url = url_id)
  return HttpResponseRedirect(u.full_url)
