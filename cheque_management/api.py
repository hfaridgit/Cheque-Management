# -*- coding: utf-8 -*-
# Copyright (c) 2017, Direction and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, erpnext
from frappe.utils import flt, cstr, nowdate, comma_and
from frappe import throw, msgprint, _

def pe_before_submit(self, method):
	if self.mode_of_payment == "Cheque" and self.payment_type == "Receive":
		notes_acc = frappe.db.get_value("Company", self.company, "receivable_notes_account")
		if not notes_acc:
			frappe.throw(_("Receivable Notes Account not defined in the company setup page"))
		rec_acc = frappe.db.get_value("Company", self.company, "default_receivable_account")
		if not rec_acc:
			frappe.throw(_("Default Receivable Account not defined in the company setup page"))
		self.db_set("paid_to", notes_acc)
		self.db_set("paid_from", rec_acc)
	if self.mode_of_payment == "Cheque" and self.payment_type == "Pay":
		notes_acc = frappe.db.get_value("Company", self.company, "payable_notes_account")
		if not notes_acc:
			frappe.throw(_("Payable Notes Account not defined in the company setup page"))
		rec_acc = frappe.db.get_value("Company", self.company, "default_payable_account")
		if not rec_acc:
			frappe.throw(_("Default Payable Account not defined in the company setup page"))
		self.db_set("paid_from", notes_acc)
		self.db_set("paid_to", rec_acc)

def pe_on_submit(self, method):
	hh_currency = erpnext.get_company_currency(self.company)
	if self.mode_of_payment == "Cheque" and self.paid_from_account_currency != hh_currency:
		frappe.throw(_("You cannot use foreign currencies with Mode of Payment   Cheque"))
	if self.mode_of_payment == "Cheque" and self.paid_to_account_currency != hh_currency:
		frappe.throw(_("You cannot use foreign currencies with Mode of Payment   Cheque"))
	if self.mode_of_payment == "Cheque" and self.payment_type == "Receive":
		notes_acc = frappe.db.get_value("Company", self.company, "receivable_notes_account")
		if not notes_acc:
			frappe.throw(_("Receivable Notes Account not defined in the company setup page"))
		self.db_set("paid_to", notes_acc)
		rec_acc = frappe.db.get_value("Company", self.company, "default_receivable_account")
		if not rec_acc:
			frappe.throw(_("Default Receivable Account not defined in the company setup page"))
		rc = frappe.new_doc("Receivable Cheques")
		rc.cheque_no = self.reference_no 
		rc.cheque_date = self.reference_date 
		rc.customer = self.party
		rc.company = self.company
		rc.payment_entry = self.name
		if self.project:
			rc.project = self.project
		rc.currency = hh_currency
		rc.amount = self.base_received_amount
		rc.exchange_rate = 1
		rc.remarks = self.remarks
		#rc.cheque_status = 1
		rc.set("status_history", [
			{
				"status": "Cheque Received",
				"transaction_date": nowdate(),
				"credit_account": rec_acc,
				"debit_account": notes_acc
			}
		])
		rc.insert(ignore_permissions=True)
		rc.submit()
		message = """<a href="#Form/Receivable Cheques/%s" target="_blank">%s</a>""" % (rc.name, rc.name)
		msgprint(_("Receivable Cheque {0} created").format(comma_and(message)))

	if self.mode_of_payment == "Cheque" and self.payment_type == "Pay":
		notes_acc = frappe.db.get_value("Company", self.company, "payable_notes_account")
		if not notes_acc:
			frappe.throw(_("Payable Notes Account not defined in the company setup page"))
		self.db_set("paid_from", notes_acc)
		rec_acc = frappe.db.get_value("Company", self.company, "default_payable_account")
		if not rec_acc:
			frappe.throw(_("Default Payable Account not defined in the company setup page"))
		pc = frappe.new_doc("Payable Cheques")
		pc.cheque_no = self.reference_no 
		pc.cheque_date = self.reference_date 
		pc.party_type = self.party_type
		pc.party = self.party
		pc.company = self.company
		pc.payment_entry = self.name
		if self.project:
			pc.project = self.project
		pc.currency = hh_currency
		pc.amount = self.base_paid_amount
		pc.exchange_rate = 1
		pc.remarks = self.remarks
		#pc.cheque_status = 1
		pc.set("status_history", [
			{
				"status": "Cheque Issued",
				"transaction_date": nowdate(),
				"credit_account": notes_acc,
				"debit_account": rec_acc
			}
		])
		pc.insert(ignore_permissions=True)
		pc.submit()
		message = """<a href="#Form/Payable Cheques/%s" target="_blank">%s</a>""" % (pc.name, pc.name)
		msgprint(_("Payable Cheque {0} created").format(comma_and(message)))

def pe_on_cancel(self, method):
	if frappe.db.sql("""select name from `tabReceivable Cheques` where payment_entry=%s and docstatus<>2  
				and not cheque_status in ("Cheque Cancelled","Cheque Rejected")""" , (self.name)):
		frappe.throw(_("Cannot Cancel this Payment Entry as it is Linked with Receivable Cheque"))
	if frappe.db.sql("""select name from `tabPayable Cheques` where payment_entry=%s and docstatus<>2  
				and cheque_status<>'Cheque Cancelled'""" , (self.name)):
		frappe.throw(_("Cannot Cancel this Payment Entry as it is Linked with Payable Cheque"))
	return
