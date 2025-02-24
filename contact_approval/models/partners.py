# -*- coding: utf-8 -*-

from odoo import models, fields


class Partners(models.Model):
    _inherit = 'res.partner'

    approver_id = fields.Many2one('res.users', string='Approved By', readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='draft', string="Approval Status")

    def action_approved(self):
        for rec in self:
            rec.approver_id = self.env.user
            rec.state = 'approved'

    def action_cancel(self):
        for rec in self:
            rec.state = 'rejected'

    def action_reset(self):
        for rec in self:
            rec.state = 'draft'
            rec.approver_id = False  # Mereset approved by

