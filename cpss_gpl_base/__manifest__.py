# -*- coding: utf-8 -*-
{
    'name': "CPSS GPL - Base & Configurations",
    'summary': "Module de base pour la gestion GPL - Configurations et paramètres",
    'description': """
        CPSS GPL - Module de Base
        =========================

        **Module fondamental pour la gestion GPL chez CPSS**

        🔧 **Fonctionnalités :**
        - Configuration initiale du système GPL
        - Séquences et données de base
        - Sécurité et droits d'accès
        - Paramètres généraux

        📋 **Prérequis :**
        Ce module doit être installé en premier avant tous les autres modules GPL CPSS.

        🏢 **Développé par CPSS :**
        Cedar Peak Systems & Solutions - Solutions GPL professionnelles
    """,

    'contributors': [
        'Cedar Peak Systems & Solutions Team',
    ],
    'author': 'Cedar Peak Systems & Solutions (CPSS)',
    'website': 'https://cedarpss.com/',
    'category': 'Industries/Automotive',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',

    # Dépendances de base
    'depends': [
        'base',
        'mail',  # Pour le suivi et notifications
        'web',  # Interface web
        'stock'
    ],

    # Données à charger
    'data': [
        # === SÉCURITÉ ===
        'security/gpl_security.xml',
        'security/ir.model.access.csv',

        # === DONNÉES DE BASE ===
        'data/ir_sequence_data.xml',

        # === CONFIGURATIONS ===
        'views/res_config_settings_views.xml',
        'views/res_company.xml',

        # === MENUS DE BASE ===
        'views/gpl_base_menus.xml',
    ],

    # Configuration
    'installable': True,
    'application': False,
    'auto_install': False,
    'sequence': 10,

    # Icône du module dans les paramètres
    'web_icon': 'cpss_gpl_base,static/description/icon.png',

    # Métadonnées
    'support': 'support@cedarpss.com',
    'maintainer': 'CPSS',

    # Images
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
    ],
}
