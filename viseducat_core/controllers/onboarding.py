from odoo import http
from odoo.http import request


class OnboardingController(http.Controller):

    @http.route('/viseducat_core/viseducat_course_onboarding_panel', auth='user', type='json')
    def viseducat_course_onboarding_panel(self):
        course = request.env['vm.course']
        return {
            'html': request.env.ref('viseducat_core.viseducat_course_onboarding_panel').render({
                'state': {'course_onboarding_course_layout_state': 'not_done'}
            })
        }
