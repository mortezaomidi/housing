from django.shortcuts import render
from django.contrib.gis.geos import Polygon
from django.core.serializers import serialize 
from django.http import HttpResponseRedirect, HttpResponse , JsonResponse, Http404
from django.urls import reverse
#from models import BuildingFootprints,Landmarks,PublicHousing,VacantParcels
from models import Landmarks,PublicHousing,VacantParcels
import json
import requests
#import json

def vacant_parcels_byId(id):
    VacantParcelJson = serialize('json',VacantParcels.objects.get(pk=handel))
    JsonResponse(json.loads(VacantParcelJson))

def homer(minPrice,maxPrice,minSqft,nbrhd,plotChoice):
    #if intention == 'prevBuild':
    #    query = "select geometry,price,address,SqFt,ownername from vacant_parcels limit 10"
    #elif intention == 'currBuild':
    #    query = "select geometry,price,address,SqFt,ownername from vacant_parcels limit 10"
    #elif intention == 'noBuild':
    #    query = "select geometry,price,address,SqFt,ownername from vacant_parcels limit 10"
    userQuery = VacantParcels.objects.filter(vacant_price_gte=min_price,vacant_price_lte=max_price,sqft_gt=minSqft)
    if userQuery:
        resultJson = serialize('geojson',PublicHousing.objects.all(), geometry_field='wkb_geometry',fields=('id','handle',))
        return JsonResponse(json.loads(resultJson))
    else:
        return Http404 

    VacantParcels.objects.filter(vacant_price_gte=min_price,vacant_price_lte=max_price,sqft_gt=minSqft)

def publichousing(request):
    publichousingJson = serialize('geojson',PublicHousing.objects.all(), geometry_field='wkb_geometry',fields=('id','handle',))
    if publichousingJson: 
        result = json.loads(publichousingJson)
        return  JsonResponse(result) 
    else:
        return Http404

def publichousing_byId(id):
    parcelJson = serialize('geojson',PublicHousing.objects.get(pk=id))
    JsonResponse(json.loads(parcelJson))

def landmarks(request):
    landmarksJson = serialize('geojson',Landmarks.objects.all(), geometry_field='wkb_geometry',fields=('ogc_fid','st_louis_field ',))
    if landmarksJson: 
        result = json.loads(landmarksJson)
        return  JsonResponse(result) 
    else:
        return Http404

def landmarks_byId(id):
    parcelJson = serialize('geojson',Landmarks.objects.get(pk=id))
    JsonResponse(json.loads(parcelJson))



def BuildingFootprints(request):
    bldngsJson = serialize('geojson',BuildingFootprints.objects.all(), geometry_field='wkb_geometry',fields=('id','handle',))
    if lraJson: 
        result = json.loads(lraJson)
        return  JsonResponse(result) 
    else:
        return Http404

def lra_byId(id):
    parcelJson = serialize('geojson',Lra.objects.get(pk=id))
    JsonResponse(json.loads(parcelJson))

def getInfo(request,property_id):
    import zillow 
    with open("./bin/config/zillow_key.conf", 'r') as f:
        key = f.readline().replace("\n", "")
    api = zillow.ValuationApi()
    property = get_object_or_404(Property, pk=property_id)
    selected_property = property.property_list.get(pk=request.POST['address'])
    address = selected_property + ', St. Louis, MO'
    data = api.GetDeepSearchResults(key, address, postal_code)
    return HttpResponse(json.dumps({'foo': 'bar'}), mimetype='application/json')
    #return HttpResponseRedirect(reverse('property', args=(property.id,)))

