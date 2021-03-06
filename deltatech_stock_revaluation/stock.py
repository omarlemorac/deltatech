# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2016 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com       
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################



from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp
from dateutil.relativedelta import relativedelta
from datetime import datetime, date, timedelta
import logging



class stock_quant(models.Model):
    _inherit = "stock.quant"

    init_value = fields.Float(string='Initial value')
    first_revaluation = fields.Date(string='First Revaluation')

    @api.multi
    def view_revaluation(self):
        action = self.env.ref('deltatech_stock_revaluation.action_stock_revaluation_line').read()[0]
        action['domain'] = "[('quant_id','in',[" + ','.join(map(str, self.ids)) + "])]"
        return action
    

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: