clouds_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'provider': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
        'allowed': ["AWS", "OpenStack"],
        'required': True,
    },
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
        'required': True,
    },
    'credentials': {
        'type': 'dict',
        'required': True,
    }
}


clouds = {
    'schema': clouds_schema
}
