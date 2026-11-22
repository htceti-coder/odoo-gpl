from odoo import models, fields


class GplVehicleTag(models.Model):
    _name = 'gpl.vehicle.tag'
    _description = 'Tags pour véhicules GPL'
    _order = 'name'

    name = fields.Char('Nom', required=True)
    color = fields.Integer('Couleur', default=0)
    active = fields.Boolean('Actif', default=True)
    description = fields.Text('Description')

    # Odoo 19 : _sql_constraints n'est plus supporté → models.Constraint
    _name_uniq = models.Constraint('unique (name)', "Ce tag existe déjà!")
