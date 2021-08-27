# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class MyPet(models.Model):
    _name = "my.project"
    _description = "My project model"

    Lab = fields.Char('Lab Name', required=True)
    Zone = fields.Char('Zone Name')
    Temperature = fields.Float('Temperature')
    