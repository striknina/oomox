from abc import ABCMeta, abstractproperty


class OomoxPlugin(object, metaclass=ABCMeta):

    @abstractproperty
    def name(self):
        pass

    @abstractproperty
    def display_name(self):
        pass


class OomoxImportPlugin(OomoxPlugin):
    pass


class OomoxThemePlugin(OomoxPlugin):

    @abstractproperty
    def description(self):
        pass

    @abstractproperty
    def export_dialog(self):
        pass

    @abstractproperty
    def gtk_preview_css_dir(self):
        pass

    enabled_keys_gtk = []
    enabled_keys_options = []
    enabled_keys_other = []

    theme_model_gtk = []
    theme_model_options = []
    theme_model_other = []

    def preview_before_load_callback(self, preview_object, colorscheme):
        pass


class OomoxIconsPlugin(OomoxPlugin):
    pass


class OomoxExportPlugin(OomoxPlugin):
    pass
