# -*- coding: utf-8 -*-

from odoo import _, models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_rental_order = fields.Boolean()
    rental_start_date = fields.Datetime()
    rental_return_date = fields.Datetime()
    duration_days = fields.Integer(compute="_compute_duration_days")
    rental_status = fields.Selection(
        [
            ('draft', 'Draft'),
            ('reserved', 'Reserved'),
            ('returned', 'Returned'),
            ('cancelled', 'Cancelled'),
        ],
        default='draft',
    )

    @api.depends("rental_start_date", "rental_return_date")
    def _compute_duration_days(self):
        for record in self:
            if record.rental_start_date and record.rental_return_date:
                start_date = record.rental_start_date.replace(hour=0, minute=0, second=0)
                return_date = record.rental_return_date.replace(hour=0, minute=0, second=0)
                record.duration_days = (return_date - start_date).days
            else:
                record.duration_days = 0

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if order.is_rental_order:
                now = fields.Datetime.now()
                if order.rental_start_date <= now <= order.rental_return_date:
                    order.rental_status = 'reserved'
        return res

    def action_reserve(self):
        for record in self:
            record.rental_status = 'reserved'

    def action_returned(self):
        for record in self:
            record.rental_status = 'returned'