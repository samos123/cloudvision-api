job_templates_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
        'required': True,
    },
    'type': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
        'allowed': ["PySpark", "Spark"],
    },
    'jobLocation': {
        'type': 'string',
    },
    # e.g. for feature_extraction.py it would be
    # "$feature_type $image_parquet_path $feature_parquet_path $partitions"
    'argumentsTemplate': {
        'type': 'dict',
    },
    'jarFiles': {
        'type': 'list',
    },
    'mainClass': {
        'type': 'string',
    },
}

job_templates = {
    'schema': job_templates_schema
}
