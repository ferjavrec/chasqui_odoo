# -*- coding: utf-8 -*-

from openerp import models, fields, api
import os


class Wizard(models.TransientModel):
    _name = 'chasqui.wizard'

    name = fields.Char('Name')


    @api.multi
    def create_request(self):
        #/usr/bin/python /home/fer/unqui/chasqui2odoo.py
        os.system ("/usr/bin/python --version")

        return True