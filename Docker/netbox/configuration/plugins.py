# Enable installed plugins. Add the name of each plugin to the list.
PLUGINS = ['nextbox_ui_plugin', 'netbox_ipcalculator', 'netbox_napalm_plugin']

# Plugins configuration settings. These settings are used by various plugins that the user may have installed.
# Each key in the dictionary is the name of an installed plugin and its value is a dictionary of settings.
PLUGINS_CONFIG = {
    'netbox_napalm_plugin': {
        'NAPALM_USERNAME': '',
        'NAPALM_PASSWORD': ''
    }
}
