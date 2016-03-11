clusters_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
    },
    'cloud': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'clouds',
            'field': '_id',
            'embeddable': True,
        },
    },
    'params': {
        'type': 'dict',
    },
    'status': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
        'allowed': ["Scheduled", "Error",
                    "Deploying", "Available"],
        'default': "Scheduled",
    },

}

clusters = {
    'schema': clusters_schema
}
