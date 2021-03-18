
from .test_facility_common import TestFacilityCommon


class TestFacilityLine(TestFacilityCommon):

    def setUp(self):
        super(TestFacilityLine, self).setUp()

    def test_case_facility_line(self):

        types = self.vm_facility_line.create({
            'facility_id': self.env.ref
            ('viseducat_facility.vm_facility_1').id,
            'quantity': '1.0',
        })
        for facility in types:
            facility.check_quantity()
