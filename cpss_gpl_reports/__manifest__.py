# -*- coding: utf-8 -*-
{
    'name': "CPSS GPL - Rapports & Certificats",
    'summary': "Module centralisé pour tous les rapports et certificats GPL",
    'description': """
        CPSS GPL - Module Rapports & Certificats
        ========================================

        **Module centralisé pour la génération de tous les rapports GPL**

        📄 **Certificats officiels :**
        - Certificat de montage GPL
        - Certificat de contrôle triennal
        - Autorisation d'utilisation GPL
        - Certificat de contrôle technique

        📊 **Rapports administratifs :**
        - Bordereau d'envoi pour les dossiers
        - Factures personnalisées GPL
        - Rapports d'interventions

        📈 **Rapports analytiques :**
        - État des réservoirs (expirations, tests)
        - Planning mensuel des interventions
        - Statistiques d'activité GPL
        - Historique client détaillé

        🎨 **Caractéristiques :**
        - Templates professionnels
        - Formats personnalisables
        - En-têtes avec logo entreprise
        - Export multi-formats (PDF, Excel)

        🏢 **Développé par CPSS :**
        Cedar Peak Systems & Solutions
    """,

    'contributors': [
        'Cedar Peak Systems & Solutions Team',
    ],
    'author': 'Cedar Peak Systems & Solutions (CPSS)',
    'website': 'https://cedarpss.com/',
    'category': 'Industries/Automotive',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',

    # Dépendances
    'depends': [
        'base',
        'account',  # Pour les factures
        'cpss_gpl_base',  # Module de base
        'cpss_gpl_reservoir',  # Pour les rapports réservoirs
        'cpss_gpl_garage',  # Pour les véhicules et clients
        'cpss_gpl_operations',  # Pour les opérations
        'l10n_dz_regions', # Pour les willayas en arabe
    ],

    # Données à charger
    'data': [
        # === SÉCURITÉ ===
        'security/ir.model.access.csv',

        # === FORMATS DE PAPIER ===
        'data/report_paperformat_data.xml',

        # === Modifications des vues ===
        'views/gpl_installation_views.xml',
        'views/gpl_inspection_views.xml',

        # === RAPPORTS ===
        # Templates de base
        'reports/gpl_report_templates.xml',

        # Certificats officiels
        'reports/gpl_montage_certificate.xml',
        'reports/gpl_triennial_certificate.xml',
        'reports/gpl_authorization_report.xml',
        'reports/gpl_installation_invoice.xml',
        'reports/gpl_card.xml',
        'reports/gpl_card_verso.xml',

        # Rapports administratifs
        'reports/gpl_bordereau_envoi.xml',
        'reports/gpl_custom_invoice.xml',

        # Rapports opérationnels
        # 'reports/gpl_inspection_report.xml',
        # 'reports/gpl_repair_report.xml',

        # Rapports analytiques
        #'reports/gpl_reservoir_report.xml',

    ],

    # Configuration
    'installable': True,
    'application': False,  # Module d'extension
    'auto_install': False,
    'sequence': 50,


    # Métadonnées
    'support': 'support@cedarpss.com',
    'maintainer': 'CPSS',

    # Images
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
    ],
}
