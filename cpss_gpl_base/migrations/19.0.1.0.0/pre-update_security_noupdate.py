# -*- coding: utf-8 -*-
"""Migration 17.0 → 19.0 : synchronisation des enregistrements de sécurité.

Le fichier security/gpl_security.xml était installé en noupdate="1" sous
Odoo 17 ; il est passé en noupdate="0" pour Odoo 19 (convention des groupes
dans le cœur Odoo, et indispensable pour réappliquer privilege_id lors de la
mise à jour). Cependant, le drapeau stocké dans ir.model.data.noupdate — et
non l'attribut XML — pilote les mises à jour : tant qu'il reste à true,
convert.py/_load_records ignore les nouvelles valeurs du XML.

Ce script bascule donc le drapeau stocké à false AVANT le chargement des
données du module, ce qui permet au XML de :
  - rattacher les 4 groupes GPL au privilège res_groups_privilege_gpl
    (remplacement de l'ancien category_id supprimé en Odoo 19) ;
  - réécrire user_ids (ex-« users ») sur group_gpl_admin.

Portée limitée aux modèles définis par gpl_security.xml : les séquences
(ir.sequence, ir_sequence_data.xml) restent en noupdate=1 — les remettre à
false écraserait les compteurs de numérotation à chaque mise à jour.
"""

# Modèles déclarés dans security/gpl_security.xml.
SECURITY_MODELS = ('ir.module.category', 'res.groups', 'res.groups.privilege')


def migrate(cr, version):
    if not version:
        # Installation fraîche : les enregistrements sont créés directement
        # avec le noupdate du XML (0). Rien à corriger.
        return
    cr.execute(
        """
        UPDATE ir_model_data
           SET noupdate = false
         WHERE module = 'cpss_gpl_base'
           AND model IN %s
        """,
        (SECURITY_MODELS,),
    )
