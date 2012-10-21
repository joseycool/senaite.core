from AccessControl import getSecurityManager
from DateTime import DateTime
from Products.AdvancedQuery import Or, MatchRegexp, Between
from Products.Archetypes.config import REFERENCE_CATALOG
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from bika.lims import PMF, logger, bikaMessageFactory as _
from bika.lims.browser import BrowserView
from bika.lims.browser.analysisrequest import AnalysisRequestWorkflowAction, \
    AnalysisRequestsView
from bika.lims.browser.bika_listing import BikaListingView
from bika.lims.browser.client import ClientAnalysisRequestsView, \
    ClientSamplesView
from bika.lims.browser.publish import Publish
from bika.lims.browser.sample import SamplesView
from bika.lims.idserver import renameAfterCreation
from bika.lims.interfaces import IContacts
from bika.lims.permissions import *
from bika.lims.subscribers import doActionFor, skip
from bika.lims.utils import isActive
from operator import itemgetter
from plone.app.content.browser.interfaces import IFolderContentsView
from plone.app.layout.globals.interfaces import IViewView
from zope.i18n import translate
from zope.interface import implements
import json
import plone

class BatchAnalysisRequestsView(AnalysisRequestsView):
    def __init__(self, context, request):
        super(BatchAnalysisRequestsView, self).__init__(context, request)
        self.contentFilter['getBatchUID'] = self.context.UID()
    def __call__(self):
        self.context_actions = {}
#        wf = getToolByName(self.context, 'portal_workflow')
#        mtool = getToolByName(self.context, 'portal_membership')
#        addPortalMessage = self.context.plone_utils.addPortalMessage
#        if isActive(self.context):
#            if mtool.checkPermission(AddAnalysisRequest, PR):
#                self.context_actions[self.context.translate(_('Add'))] = {
#                    'url':PR.absolute_url() + '/ar_add',
#                    'icon': '++resource++bika.lims.images/add.png'}
        return super(BatchAnalysisRequestsView, self).__call__()

class BatchSamplesView(SamplesView):
    def __init__(self, context, request):
        super(BatchSamplesView, self).__init__(context, request)
        self.contentFilter['getBatchUID'] = self.context.UID()
