config = {
    "AZURE_BYGG_POSTGRESQL_PSW": "Vvo23oLk!@12cDsd629s0,,2uocCas",
    "NK_WMS_API_KEY": "36d8500a-3a2d-40fa-86b1-2af2b3ad1409",
    "AZURE_STORAGE_CONNECTION_STRING": "DefaultEndpointsProtocol=https;AccountName=buildingdetectionmodels;AccountKey=KAfv7yYGkvNqPA1mctxPv0aXOHJ3B2CICiPCNQzWLu5IxwmqN/ROyoEZ4XpX6d6MPTeu+0yZKFC5CRk8e85P2A==;EndpointSuffix=core.windows.net",
    "NK_POSTGRESQL_PWD": "",
}

def get_env_secret(variable):
    return config[variable]


    