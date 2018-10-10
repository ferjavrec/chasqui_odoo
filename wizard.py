# -*- coding: utf-8 -*-

from openerp import models, fields, api
import os


class Wizard(models.TransientModel):
    _name = 'chasqui.wizard'

    name = fields.Char('Name')


    @api.multi
    def create_request(self):
        os.system ("/usr/bin/python /home/servidor/odoo/adaptador/chasqui2odoo.py /home/servidor/odoo/adaptador/log/chasqui2odoo.log 2>&1")
		os.system ("/usr/bin/python /home/servidor/odoo/adaptador/odoo2chasqui.py /home/servidor/odoo/adaptador/log/odoo2chasqui.log 2>&1")
        return True