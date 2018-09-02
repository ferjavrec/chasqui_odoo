# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Wizard(models.TransientModel):
    _name = 'chasqui.wizard'

    name = fields.Char('Name')


    @api.multi
    def create_request(self):
        print "You click finish"

        return True