# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from ResimSpatula import app, log_ver
from flask import render_template, request

from scrapper import Scrapper
import os

# DISPLAYING THE DATA THAT USER REQUIRED
@app.route('/displayImages')
def display():
    log_ver(request)
    list_images=os.listdir('ResimSpatula/static/temp')
    list_images = [f'temp/{resim}' for resim in list_images]
    print(list_images)

    try:
        if list_images:
            return render_template('goster.html', list_images=list_images)
        else:
            print('images are not present')

    except Exception as e:
        print('No images found', e)
        return 'please try with other search keyword'
    
    return 'None'

# SEARCH AND DOWNLOAD THE IMAGES INTO THE LOCAL SERVER
@app.route('/searchImages',methods=['POST'])
def search():
    log_ver(request)
    if request.method=='POST':
        keyword=request.form['search_term']
        count=int(request.form['frequency'])

        s=Scrapper()
        list_images = os.listdir('ResimSpatula/static/temp')
        s.delete_images(list_images)

        web_url = s.create_url(keyword)
        html = s.scrap_html(web_url)
        imgs = s.get_imagelist(html)
        s.download_images(imgs[1:],keyword,count)
        print('hii')
    return display()