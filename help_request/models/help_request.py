# -*- coding: utf-8 -*-

import base64
from odoo import models, fields, api, tools
from odoo.modules.module import get_module_resource
from datetime import datetime


class HelpRequest(models.Model):
    _name = 'help_request.model'
    _description = 'Help request model'
    _inherit = 'mail.thread'
    _order = 'id desc'

    @api.model
    def _default_image(self):
        image_path = get_module_resource('help_request', 'static/src/img', 'question.png')
        return tools.image_resize_image_big(base64.b64encode(open(image_path, 'rb').read()))

    @api.model
    def _get_current_user(self):
        cur_user = self.env['hr.employee'].search([('user_id', '=', self.env.uid)])
        return cur_user

    name = fields.Char(string='Request subject', required=True)
    avatar = fields.Binary(string='Image', default=_default_image)
    attachment_ids = fields.Many2many('ir.attachment', string='Attachments')
    category = fields.Selection([
        ('soft-installation', 'Software installation'),
        ('soft-problem', 'Problem with software'),
        ('hd-problem', 'Problem with hardware'),
        ('permissions/access', 'Lack of permissions/access'),
        ('odoo-problem', 'Problem with Odoo'),
        ('licence-problem', 'Problem with License'),
        ('other', 'Other'),
    ], string='Issue category', required=True)
    applicant = fields.Many2one('hr.employee', string='Request applicant', default=_get_current_user, required=True, readonly=True)
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
    ], default='0', index=True, string="Priority")
    realization_date = fields.Date(string="Preferred realization date", default=str(datetime.today()), help="If the problem is not urgent, choose a time to proceed with the repair, which may take several hours")
    description = fields.Text(string="Description", required=True, help="Post here as much detail as possible about the failure. When the problem occurred, under what conditions it occurred. etc.")
    state = fields.Selection([
        ('new', 'New'),
        ('in-progress', 'In progress'),
        ('done', 'Done')
    ], default='new', index=True, string="State")
