from odoo import http
from odoo.http import request


class OnboardingController(http.Controller):

    @http.route('/viseducat_core/viseducat_course_onboarding_panel', auth='user', type='json')
    def viseducat_course_onboarding_panel(self):
        return {
            'html': request.env.ref('viseducat_core.viseducat_course_onboarding_panel').render({
                'course': course,
                'state': course.get_and_update_sale_quotation_onboarding_state()
            })
        }





