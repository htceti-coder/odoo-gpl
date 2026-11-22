# === 1. __manifest__.py ===
{
    'name': "CPSS GPL - Gestion de Garage",
    'summary': "Module spécialisé pour la gestion d'atelier et planning GPL",
    'description': """
        CPSS GPL - Gestion de Garage
        =============================

        **Module spécialisé pour la gestion d'atelier automobile GPL**

        🚗 **Gestion Véhicules :**
        - Fiche véhicule complète avec tags
        - Suivi client et historique
        - Photos et documents
        - États et workflows

        📅 **Planning Atelier :**
        - Calendrier interactif multi-vues
        - Gestion des rendez-vous
        - Assignation des techniciens
        - Notifications automatiques

        👥 **Gestion Clients :**
        - Fiche client enrichie
        - Historique des interventions
        - Contacts et communications
        - Devis et facturation

        ⚙️ **Workflow Optimisé :**
        - Assistant de reprogrammation
        - Création rapide de RDV
        - Suivi en temps réel
        - Alertes et rappels

        🏢 **Développé par CPSS :**
        Cedar Peak Systems & Solutions
    """,

    'author': 'Cedar Peak Systems & Solutions (CPSS)',
    'website': 'https://cedarpss.com/',
    'category': 'Industries/Automotive',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',

    # Dépendances
    'depends': [
        'cpss_gpl_reservoir',
        'fleet',            # Module fleet d'Odoo
        'calendar',         # Gestion des rendez-vous
        'hr',              # Gestion des employés/techniciens
        'contacts',        # Gestion des clients
    ],

    # Données à charger
    'data': [
        # === SÉCURITÉ ===
        'security/ir.model.access.csv',

        # === DONNÉES DE BASE ===
        'data/gpl_vehicle_status_data.xml',
        'data/calendar_event_type_data.xml',
        'data/hr_department_data.xml',
        'data/cron_jobs.xml',

        # === VUES PRINCIPALES ===
        # Véhicules
        'views/gpl_vehicle_tag_views.xml',
        'views/gpl_vehicle_status_views.xml',
        'views/gpl_vehicle_views.xml',
        'views/stock_lot_views.xml',

        # Rendez-vous
        'views/gpl_appointment_views.xml',

        # Clients (extension res_partner)
        'views/res_partner_views.xml',

        # Fleet vehicle model (extension)
        'views/fleet_vehicle_model_views.xml',

        # Planning et calendrier
        'views/calendar_views.xml',


        # === MENUS ===
        'views/gpl_garage_menus.xml',

        'wizard/vehicle_appointment_wizard_views.xml',
        'wizard/notification_test_wizard_views.xml',

    ],

    # Assets web
    'assets': {
        'web.assets_backend': [
            'cpss_gpl_garage/static/src/css/garage_calendar.css',
            'cpss_gpl_garage/static/src/js/garage_calendar.js',
            'cpss_gpl_garage/static/src/js/simple_calendar_override.js'
        ],
    },


    # Configuration
    'installable': True,
    'application': True,  # Module d'extension
    'auto_install': False,
    'sequence': 30,

    # Métadonnées
    'support': 'support@cedarpss.com',
    'maintainer': 'CPSS',

    # Images
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
    ],
}
