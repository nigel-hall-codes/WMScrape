from models import *
import json
import urllib.request



def download_dispensaries():
    url1 = "https://api-g.weedmaps.com/wm/v2/listings?filter%5Bbounding_box%5D=37.76786513360663,-122.48150825500488,37.81127577036112,-122.39001274108888&filter%5Bplural_types%5D%5B%5D=doctors&filter%5Bplural_types%5D%5B%5D=dispensaries&filter%5Bplural_types%5D%5B%5D=deliveries&page_size=100&size=100"
    url2 = "https://api-g.weedmaps.com/wm/v2/listings?filter%5Bbounding_box%5D=37.67376658565116,-122.64484405517578,37.86130199456176,-122.36743927001952&filter%5Bplural_types%5D%5B%5D=doctors&filter%5Bplural_types%5D%5B%5D=dispensaries&filter%5Bplural_types%5D%5B%5D=deliveries&page_size=100&size=100"
    url3 = "https://api-g.weedmaps.com/wm/v2/listings?filter%5Bbounding_box%5D=37.68803162408617,-122.57600784301756,37.781840715520495,-122.40726470947266&filter%5Bplural_types%5D%5B%5D=doctors&filter%5Bplural_types%5D%5B%5D=dispensaries&filter%5Bplural_types%5D%5B%5D=deliveries&page_size=100&size=100"
    url4 = "https://api-g.weedmaps.com/wm/v2/listings?filter%5Bbounding_box%5D=37.62483706088789,-122.56605148315428,37.71180059181106,-122.37464904785155&filter%5Bplural_types%5D%5B%5D=doctors&filter%5Bplural_types%5D%5B%5D=dispensaries&filter%5Bplural_types%5D%5B%5D=deliveries&page_size=100&size=100"
    urls = [url1, url2, url3, url4]

    for url in urls:
        req = urllib.request.urlopen(url)
        data = json.loads(req.read().decode('utf-8'))['data']
        listings = data['listings']
        for l in listings:
            l_dict = {}
            l_dict['name'] = l['name']
            l_dict['_type'] = l['type']
            l_dict['slug'] = l['slug']
            l_dict['state'] = l['state']
            l_dict['city'] = l['city']
            l_dict['wmid'] = l['wmid']
            l_dict['license_type'] = l['license_type']
            print(l_dict)
            d = Dispensary.get_or_create(**l_dict)



