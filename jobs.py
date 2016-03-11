jobs_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'cluster': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'clusters',
            'field': '_id',
            'embeddable': True,
        },
        'required': True,
    },
    'template': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'job-templates',
            'field': '_id',
            'embeddable': True,
        },
        'required': True,
    },


    'arguments': {
        'type': 'dict',
    },

    'status': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
        'allowed': ["Scheduled", "Error", "Running", "Finished"],
        'default': "Scheduled",
    },

}

jobs = {
    'schema': jobs_schema
}
