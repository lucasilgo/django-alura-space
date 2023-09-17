from django.shortcuts import render

def index(req):
    data = {
        1: {
            "name": "Nebulosa de Carina",
            "caption": "webbtelescope.org / NASA / James Webb"
        },
        2: {
            "name": "Galáxia NGC 1079",
            "caption": "nasa.org / NASA / Hubble"
        }
    }

    return render(req, 'galery/index.html', { "cards": data })

def image(req):
    return render(req, 'galery/image.html')
