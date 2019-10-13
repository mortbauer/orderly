import maya
from eve import Eve


supplier_schema = {
    'name': {
        'type':'string',
        'required':True,
        'unique':True,
    }
}

def to_datetime(x):
    return maya.when(x).datetime()

order_schema = {
    'supplier':{
        'type': 'string',
        'required':True,
        'data_relation': {
            'resource': 'supplier',
            'field':'name',
            }
        },
    'starttime': {
        'type':'datetime',
        'coerce':to_datetime,
        'required':True,
        },
    'endtime': {
        'type':'datetime',
        'coerce':to_datetime,
        'required':True,
        },
}

supplier = {
    'resource_methods':['GET','POST','DELETE'],
    'item_methods':['GET','PATCH','PUT','DELETE'],
    'schema': supplier_schema,
}

order = {
    'resource_methods':['GET','POST','DELETE'],
    'item_methods':['GET','PATCH','PUT','DELETE'],
    'schema': order_schema,
}

settings = {
    'DOMAIN': {
        'supplier': supplier,
        'order': order,
    },
    'DEBUG':True,
    'X_DOMAINS':'*',
    'X_EXPOSE_HEADERS':[],
    'X_HEADERS':['Content-Type','If-match'],
}

app = Eve(settings=settings)
app.run()
