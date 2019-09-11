# -*- coding: utf-8 -*-
# Copyright (c) 2019, Shahzad Naser and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _, msgprint
from frappe.model.document import Document

class ApiSettings(Document):
	
	@classmethod
	def get_exchange_rates(cls):
		''' Function to send request to get latest currency exchange rates and update in required docs '''
		import requests

		ss = frappe.get_doc('SMS Settings', 'SMS Settings')

		if ss.use_post:
			response = requests.post(ss.sms_gateway_url, ss.get("parameters"))
		else:
			response = requests.get(gateway_url, headers=headers, params=params)
		# check response code and update rates or throw error message here
			
		return response.status_code


@frappe.whitelist(allow_guest=True)
def update_exchange_rate():
	''' White listed function update exchange rates '''
	if frappe.db.get_value('Api Settings', None, 'api_url'):
		code =  ApiSettings.get_exchange_rates()
		if 200 == code:
			frappe.msgprint(_("SMS sent to following numbers"))
		else:
			msgprint(_("There is error in api calling please check api doc agains status code: {0}").format(code))
	else:
		msgprint(_("Please Update Api Settings"))


