// Copyright (c) 2017, Direction and contributors
// For license information, please see license.txt

frappe.ui.form.on('Receivable Cheques', {
	onload: function(frm) {
		// formatter for Receivable Cheques Status
		frm.set_indicator_formatter('status',
			function(doc) { 
				if(doc.status=="Cheque Received") {	return "lightblue"}
				if(doc.status=="Cheque Deposited") {	return "blue"}
				if(doc.status=="Cheque Collected") {	return "green"}
				if(doc.status=="Cheque Returned") {	return "orange"}
				if(doc.status=="Cheque Rejected") {	return "red"}
				if(doc.status=="Cheque Cancelled") {	return "black"}
		})
	},
	refresh: function(frm) {
		if (frm.doc.cheque_status=="Cheque Received" || frm.doc.cheque_status=="Cheque Returned") {
			frm.set_df_property("deposit_bank", 'read_only', 0);
			frm.set_df_property("deposit_bank", 'reqd', 1);
		}
		else {
			frm.set_df_property("deposit_bank", 'read_only', 1);
			frm.set_df_property("deposit_bank", 'reqd', 0);
		}
		var chq_sts = "";
		$.each(frm.doc["status_history"], function(i, row) {
			chq_sts = row.status;
		});
		if(frm.doc.cheque_status) {
			if (chq_sts!=frm.doc.cheque_status) {  
				frm.page.actions_btn_group.hide();
				if (frm.doc.cheque_status=="Cheque Cancelled" || frm.doc.cheque_status=="Cheque Rejected") {
					$c('runserverobj', args={'method':'on_update','docs':frm.doc},function(r,rt) {
							frm.page.actions_btn_group.show();
							frm.refresh();
					}); 
				}
				else {
					frappe.prompt([
						{'fieldname': 'posting_date', 'fieldtype': 'Date', 'label': 'Posting Date', 'reqd': 1}  
						],
						function(values){
							//if (values) {
								frm.doc.posting_date = values.posting_date;
								$c('runserverobj', args={'method':'on_update','docs':frm.doc},function(r,rt) {
										frm.page.actions_btn_group.show();
										frm.refresh_fields();
								}); 
							//}
						},
						__("Transaction Posting Date"),
						__("Confirm")
					);
				}
			}
		}
	}
});
cur_frm.fields_dict.deposit_bank.get_query = function(doc) {
	return {
		filters: [
			["Account", "account_type", "=", "Bank"],
			["Account", "root_type", "=", "Asset"],
			["Account", "is_group", "=",0],
			["Account", "company", "=", doc.company]
		]
	}
}
