#!/usr/bin/python
import zipfile 
import io 
import urllib.request
import json
import zipfile
import shutil

modulesList = {
    'VirtoCommerce.Tax':'https://github.com/VirtoCommerce/vc-module-tax/releases/download/3.0.0-rc.3/VirtoCommerce.Tax_3.0.0-rc.3.zip','VirtoCommerce.Subscription':'https://github.com/VirtoCommerce/vc-module-subscription/releases/download/3.0.0-rc.3/VirtoCommerce.Subscription_3.0.0-rc.3.zip',
    'VirtoCommerce.Sitemaps':'https://github.com/VirtoCommerce/vc-module-sitemaps/releases/download/3.0.0-rc.3/VirtoCommerce.Sitemaps_3.0.0-rc.3.zip',
    'VirtoCommerce.Notifications':'https://github.com/VirtoCommerce/vc-module-notification/releases/download/3.0.0-rc.3/VirtoCommerce.Notifications_3.0.0-rc.3.zip',
    'VirtoCommerce.Marketing':'https://github.com/VirtoCommerce/vc-module-marketing/releases/download/3.0.0-rc.3/VirtoCommerce.Marketing_3.0.0-rc.3.zip',
    'VirtoCommerce.LuceneSearch':'https://github.com/VirtoCommerce/vc-module-lucene-search/releases/download/3.0.0-rc.3/VirtoCommerce.LuceneSearch_3.0.0-rc.3.zip',
    'VirtoCommerce.Inventory':'https://github.com/VirtoCommerce/vc-module-inventory/releases/download/3.0.0-rc.3/VirtoCommerce.Inventory_3.0.0-rc.3.zip',
    'VirtoCommerce.ImageTools':'https://github.com/VirtoCommerce/vc-module-image-tools/releases/download/3.0.0-rc.3/VirtoCommerce.ImageTools_3.0.0-rc.3.zip',
    'VirtoCommerce.ElasticSearch':'https://github.com/VirtoCommerce/vc-module-elastic-search/releases/download/3.0.0-rc.3/VirtoCommerce.ElasticSearch_3.0.0-rc.3.zip',
    'VirtoCommerce.Content':'https://github.com/VirtoCommerce/vc-module-content/releases/download/3.0.0-rc.3/VirtoCommerce.Content_3.0.0-rc.3.zip',
    'VirtoCommerce.Catalog':'https://github.com/VirtoCommerce/vc-module-catalog/releases/download/3.0.0-rc.3/VirtoCommerce.Catalog_3.0.0-rc.3.zip',
    'VirtoCommerce.Export':'https://github.com/VirtoCommerce/vc-module-export/releases/download/3.0.0-rc.3/VirtoCommerce.Export_3.0.0-rc.3.zip',
    'VirtoCommerce.Search':'https://github.com/VirtoCommerce/vc-module-search/releases/download/3.0.0-rc.3/VirtoCommerce.Search_3.0.0-rc.3.zip',
    'VirtoCommerce.AzureSearch':'https://github.com/VirtoCommerce/vc-module-azure-search/releases/download/3.0.0-rc.3/VirtoCommerce.AzureSearch_3.0.0-rc.3.zip',
    'VirtoCommerce.Core':'https://github.com/VirtoCommerce/vc-module-core/releases/download/3.0.0-rc.3/VirtoCommerce.Core_3.0.0-rc.3.zip', 
    'VirtoCommerce.Customer':'https://github.com/VirtoCommerce/vc-module-customer/releases/download/3.0.0-rc.3/VirtoCommerce.Customer_3.0.0-rc.3.zip', 
    'VirtoCommerce.Orders':'https://github.com/VirtoCommerce/vc-module-order/releases/download/3.0.0-rc.3/VirtoCommerce.Orders_3.0.0-rc.3.zip', 
    'VirtoCommerce.Notifications':'https://github.com/VirtoCommerce/vc-module-notification/releases/download/3.0.0-rc.3/VirtoCommerce.Notifications_3.0.0-rc.3.zip', 
    'VirtoCommerce.Cart':'https://github.com/VirtoCommerce/vc-module-cart/releases/download/3.0.0-rc.3/VirtoCommerce.Cart_3.0.0-rc.3.zip', 
    'VirtoCommerce.Shipping':'https://github.com/VirtoCommerce/vc-module-shipping/releases/download/3.0.0-rc.3/VirtoCommerce.Shipping_3.0.0-rc.3.zip', 
    'VirtoCommerce.Payment':'https://github.com/VirtoCommerce/vc-module-payment/releases/download/3.0.0-rc.3/VirtoCommerce.Payment_3.0.0-rc.3.zip', 
    'VirtoCommerce.Store':'https://github.com/VirtoCommerce/vc-module-store/releases/download/3.0.0-rc.3/VirtoCommerce.Store_3.0.0-rc.3.zip', 
    'VirtoCommerce.Pricing':'https://github.com/VirtoCommerce/vc-module-pricing/releases/download/3.0.0-rc.3/VirtoCommerce.Pricing_3.0.0-rc.3.zip'
}

def getZipData(url):
    result = urllib.request.urlopen(url)
    return result.read()

url = 'https://raw.githubusercontent.com/VirtoCommerce/vc-modules/master/modules_v3.json'

response = urllib.request.urlopen(url)
modules = json.load(response)   

#for module in modules:
#    if 'commerce' in map(lambda x:x.lower(), module["Groups"]):
#        moduleId = module["Id"]
#        if moduleId in modulesList:
#            destinationPath = moduleId
#            for version in module["Versions"]:
#                if 'rc.3' == version["VersionTag"]:
#                    packageUrl = version["PackageUrl"]
#                    zipData = getZipData(packageUrl)
#                    zipRef = zipfile.ZipFile(io.BytesIO(zipData))
#                    zipRef.extractall(destinationPath)
#                    print(moduleId, 'installed')
for module in modulesList:
    destinationPath = module
    fileName = module + '.zip'
    
    with urllib.request.urlopen(modulesList[module]) as response, open(fileName, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    
    zipRef = zipfile.ZipFile(fileName, 'r')
    zipRef.extractall(destinationPath)
    zipRef.close()



