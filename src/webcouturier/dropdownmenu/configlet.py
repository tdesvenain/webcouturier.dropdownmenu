from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from plone.app.controlpanel.form import ControlPanelForm
from zope.component import adapts, getUtility
from zope.formlib.form import FormFields
from zope.interface import implements
from webcouturier.dropdownmenu.browser.interfaces import IDropdownConfiguration
from webcouturier.dropdownmenu import msg_fact as _


class DropdownControlPanelAdapter(SchemaAdapterBase):
    adapts(IPloneSiteRoot)
    implements(IDropdownConfiguration)

    def __init__(self, context):
        super(DropdownControlPanelAdapter, self).__init__(context)
        self.context = getUtility(IPropertiesTool).dropdown_properties

    dropdown_depth = ProxyFieldProperty(
        IDropdownConfiguration['dropdown_depth'])
    enable_caching = ProxyFieldProperty(
        IDropdownConfiguration['enable_caching'])
    enable_parent_clickable = ProxyFieldProperty(
        IDropdownConfiguration['enable_parent_clickable'])
    enable_desc = ProxyFieldProperty(
        IDropdownConfiguration['enable_desc'])
    enable_thumbs = ProxyFieldProperty(
        IDropdownConfiguration['enable_thumbs'])

class DropdownControlPanel(ControlPanelForm):
    form_fields = FormFields(IDropdownConfiguration)

    label = _(u"A dropdown menu configuration.")
    description = _(
        u'Settings to configure dropdown menus for global navigation.')
    form_name = _(u'Dropdown menu settings')
