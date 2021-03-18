from odoo.tests import common


class TestClassroomCommon(common.SavepointCase):
    def setUp(self):
        super(TestClassroomCommon, self).setUp()
        self.op_classroom = self.env['vm.classroom']
        self.op_asset = self.env['vm.asset']
