from odoo import models, fields
from datetime import date
import calendar
import json


class VmMediaType(models.Model):
    _name = "vm.media.type"
    _description = "Media Type"

    name = fields.Char('Name', size=64, required=True)
    code = fields.Char('Code', size=64, required=True)
    issued = fields.Integer('Issued', compute='compute_issued_media')
    available = fields.Integer('Available', compute='compute_available_media')
    due_media_today = fields.Integer('Due Course Books of Today', compute='compute_due_media_today')
    due_media_month = fields.Integer('Due Course Books of Month', compute='compute_due_media_month')
    dashboard_graph_data = fields.Text(compute='_compute_dashboard_graph')

    _sql_constraints = [
        ('unique_media_type_code',
         'unique(code)', 'Code should be unique per media type!')]

    def compute_issued_media(self):
        for record in self:
            record.issued = self.env['vm.media.unit'].search_count(
                [('media_type_id.name', '=', record.name), ('state', '=', 'issue')])

    def compute_available_media(self):
        for record in self:
            record.available = self.env['vm.media.unit'].search_count(
                [('media_type_id.name', '=', record.name), ('state', '=', 'available')])

    def compute_due_media_today(self):
        for rec in self:
            rec.due_media_today = self.env['vm.media.movement'].search_count(
                [('media_type_id.name', '=', rec.name), ('return_date', '=', date.today())])

    def compute_due_media_month(self):
        today = date.today()
        last_day = calendar.monthrange(today.year, today.month)[1]
        first_day_of_the_month = today.replace(day=1)
        last_day_of_the_month = today.replace(day=last_day)

        for rec in self:
            rec.due_media_month = self.env['vm.media.movement'].search_count(
                [('media_type_id.name', '=', rec.name), ('return_date', '>=', first_day_of_the_month),
                 ('return_date', '<=', last_day_of_the_month)])

    def _compute_dashboard_graph(self):
        for record in self:
            record.dashboard_graph_data = json.dumps(record._graph_data(record.id))

    def _graph_data(self, record_id):

        month_list = [(i+1) for i in range(12)]
        value_list = [0 for i in range(12)]
        record_data = self.read_total_due_media(record_id)

        for month in record_data:
            value_list[month-1]+=1

        x_field = 'label'
        y_field = 'value'

        values = []
        for month, media_number in zip(month_list, value_list):
            temp_dict = {}
            temp_dict[y_field] = media_number
            temp_dict[x_field] = month
            values.append(temp_dict)


        return [{'values': values, 'area': True, 'title': '', 'key': "Attendance", 'color': '#7c7bad'}]

    def read_total_due_media(self, record_id):
        researches = self.env['vm.media.movement'].search([('media_type_id', '=', record_id)])
        temp_list = []

        for research in researches:
            month = research.return_date.month
            temp_list.append(month)

        return temp_list

    def create_new_media_type(self):
        action = self.env.ref('viseducat_library.act_open_vm_media_view').read()[0]
        action['context'] = {'default_media_type_id': self.id}


        return action

