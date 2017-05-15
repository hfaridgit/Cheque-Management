from __future__ import unicode_literals

docs_version = "7.x.x"

source_link = "https://github.com/hfaridgit/Cheque-Management"
docs_base_url = "https://frappe.github.io/erpnext"
headline = "Cheque Management Documentation"
sub_heading = "Detailed explanation for all ERPNext features and developer API"
long_description = """ERPNext is a fully featured ERP system designed for Small and Medium Sized
business. ERPNext covers a wide range of features including Accounting, CRM,
Inventory management, Selling, Purchasing, Manufacturing, Projects, HR &
Payroll, Website, E-Commerce and much more.

ERPNext is based on the Frappe Framework is highly customizable and extendable.
You can create Custom Form, Fields, Scripts and can also create your own Apps
to extend ERPNext functionality.

ERPNext is Open Source under the GNU General Public Licence v3 and has been
listed as one of the Best Open Source Softwares in the world by many online
blogs."""

splash_light_background = True

# source_link = "https://github.com/[org_name]/cheque_management"
# docs_base_url = "https://[org_name].github.io/cheque_management"
# headline = "App that does everything"
# sub_heading = "Yes, you got that right the first time, everything"

def get_context(context):
	#context.brand_html = "Cheque Management"
	context.brand_html = ('<img class="brand-logo" src="'+context.docs_base_url
		+'/assets/img/erpnext-docs.png"> Cheque Management</img>')
	context.app.splash_light_background = True
	context.top_bar_items = [
		{"label": "User Manual", "url": context.docs_base_url + "/user/manual", "right": 1}
	]
