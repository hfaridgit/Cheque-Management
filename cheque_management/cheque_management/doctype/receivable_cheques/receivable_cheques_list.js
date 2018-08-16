// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

// render
frappe.listview_settings['Receivable Cheques Status'] = {
	add_fields: ["cheque_status", "transaction_date", "bank", "journal_entry", "payment_entry"],
	get_indicator: function(doc) {
		if(cheque_status=="Cheque Received") {
			return [__("Cheque Received"), "lightblue", "cheque_status,=,'Cheque Received'"];
		} 
		if(cheque_status=="Cheque Deposited") {
			return [__("Cheque Deposited"), "blue", "cheque_status,=,'Cheque Deposited'"];
		} 
		if(cheque_status=="Cheque Collected") {
			return [__("Cheque Collected"), "green", "cheque_status,=,'Cheque Collected'"];
		} 
		if(cheque_status=="Cheque Returned") {
			return [__("Cheque Returned"), "orange", "cheque_status,=,'Cheque Returned'"];
		} 
		if(cheque_status=="Cheque Rejected") {
			return [__("Cheque Rejected"), "red", "cheque_status,=,'Cheque Rejected'"];
		} 
		if(cheque_status=="Cheque Cancelled") {
			return [__("Cheque Cancelled"), "black", "cheque_status,=,'Cheque Cancelled'"];
		} 
 	}
};
