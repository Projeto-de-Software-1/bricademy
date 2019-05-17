from django.shortcuts import render


def home(request):
    # TODO
    # tirar daqui e colocar ou no settings ou num .env
    mapbox_access_token = "pk.eyJ1IjoiZG95bGVzbSIsImEiOiJjanZzZWx5bjgzNTE3M3lvajFxMmlyM3diIn0.RImU51Sa3cQqh50ZtCGBkA"
    return render(request, 'home.html',  {'mapbox_access_token': mapbox_access_token})
