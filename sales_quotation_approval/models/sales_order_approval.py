# -*- coding: utf-8 -*-

import time
import logging
from odoo.exceptions import ValidationError
from odoo import models, api,fields
from odoo.exceptions import Warning

_logger = logging.getLogger(__name__)

class sales_order_approval(models.Model):
   
    _inherit = "sale.order"
    
    state = fields.Selection(selection_add=[('quotation_approved', "Quotation Approved")])
    
    @api.multi
    def action_quotation_approve(self):
        self.state = 'quotation_approved'