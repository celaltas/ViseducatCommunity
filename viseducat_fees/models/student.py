from odoo import models, fields, api, _
from odoo.exceptions import UserError


class VmStudentFeesDetails(models.Model):
    _name = "vm.student.fees.details"
    _description = "Student Fees Details"

    fees_line_id = fields.Many2one('vm.fees.terms.line', 'Fees Line')
    invoice_id = fields.Many2one('account.move', 'Invoice ID')
    amount = fields.Float('Fees Amount', currency_field='currency_id')
    date = fields.Date('Submit Date')
    product_id = fields.Many2one('product.product', 'Product')
    student_id = fields.Many2one('vm.student', 'Student')
    fees_factor = fields.Float("Fees Factor")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('invoice', 'Invoice Created'),
        ('cancel', 'Cancel')
    ], string='Status', copy=False)
    invoice_state = fields.Selection([
        ('draft', 'Draft'), ('proforma', 'Pro-forma'),
        ('proforma2', 'Pro-forma'), ('open', 'Open'),
        ('paid', 'Paid'), ('cancel', 'Cancelled')], 'Invoice',
        related="invoice_id.state", readonly=True)
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)

    @api.depends('company_id')
    def _compute_currency_id(self):
        main_company = self.env['res.company']._get_main_company()
        for template in self:
            template.currency_id = template.company_id.sudo().currency_id.id or main_company.currency_id.id

    currency_id = fields.Many2one('res.currency', string='Currency', compute='_compute_currency_id',
                                  default=lambda self: self.env.user.company_id.currency_id.id)






    def get_invoice(self):
        print("get invoice methodu çağrıldı")



    def action_get_invoice(self):
        print("action_get_invoice methodu çağrıldı")















class VmStudent(models.Model):
    _inherit = "vm.student"

    fees_detail_ids = fields.One2many('vm.student.fees.details',
                                      'student_id',
                                      string='Fees Collection Details',
                                      track_visibility='onchange')

    def action_view_invoice(self):
        print("action_view_invoice çağrıldı")
        '''
        This function returns an action that
        display existing invoices of given student ids and show a invoice"
        '''
        # result = self.env.ref('account.action_move_out_invoice_type')
        # fees = result and result.id or False
        # result = self.env['ir.actions.act_window'].browse(fees).read()[0]
        # inv_ids = []
        # for student in self:
        #     inv_ids += [invoice.id for invoice in student.invoice_ids]
        #     result['context'] = {'default_partner_id': student.partner_id.id}
        # if len(inv_ids) > 1:
        #     result['domain'] = \
        #         "[('id','in',[" + ','.join(map(str, inv_ids)) + "])]"
        # else:
        #     res = self.env.ref('account.view_move_form')
        #     result['views'] = [(res and res.id or False, 'form')]
        #     result['res_id'] = inv_ids and inv_ids[0] or False
        # return result
