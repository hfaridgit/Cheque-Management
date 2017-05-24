// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.query_reports["Cheque Ledger Report"] = {
	"filters": [
		{
			"fieldname":"cheque_no",
			"label": __("Cheque No."),
			"fieldtype": "Data",
			"default": "",
			"reqd": 1,
		},
	]
}
