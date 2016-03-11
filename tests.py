import os

from eve.tests import TestMinimal

clouds_data = [
    {
        "name": "OpenStack-Sam",
        "provider": "OpenStack",
        "credentials": {
            "username": "sam",
            "password": "sam",
            "tenantName": "sam",
            "tenantId": "18bjd8lb",
            "region": "RegionOne"
        }
    },
    {
        "name": "AWS-sam",
        "provider": "AWS",
        "credentials": {
            "aws_access_key": "afub8sfjbla",
            "aws_secret_key": "ibif8bun"
        }
    }
]


class CloudVisionAPITests(TestMinimal):

    def setUp(self):
        self.this_directory = os.path.dirname(os.path.realpath(__file__))
        settings_file = os.path.join(self.this_directory, 'test_settings.py')
        super(CloudVisionAPITests, self).setUp(settings_file=settings_file)

    def test_get_empty_clouds_collection(self):
        v, status = self.get("clouds")
        self.assert200(status)

    def test_post_get_clouds_resource(self):
        # Insert first item
        v, status = self.post("/clouds", clouds_data[0])
        self.assert201(status)
        v, status = self.get("clouds")
        self.assert200(status)
        self.assertEquals(clouds_data[0]['name'], v["_items"][0]['name'])
        self.assertEquals(len(v["_items"]), 1)

        # Insert 2nd item
        v, status = self.post("/clouds", clouds_data[1])
        self.assert201(status)
        v, status = self.get("clouds")
        self.assert200(status)
        self.assertEquals(clouds_data[1]['name'], v["_items"][1]['name'])
        self.assertEquals(len(v["_items"]), 2)
