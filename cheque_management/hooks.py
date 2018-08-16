# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "cheque_management"
app_title = "Cheque Management"
app_publisher = "Direction"
app_description = "For managing receivable and payable cheques in local currency only"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@egdirection.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cheque_management/css/cheque_management.css"
# app_include_js = "/assets/cheque_management/js/cheque_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/cheque_management/css/cheque_management.css"
# web_include_js = "/assets/cheque_management/js/cheque_management.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "cheque_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "cheque_management.install.before_install"
# after_install = "cheque_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cheque_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
    "Payment Entry": {
        "on_submit": "cheque_management.api.pe_on_submit",
        "before_submit": "cheque_management.api.pe_before_submit",
        "on_cancel": "cheque_management.api.pe_on_cancel"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cheque_management.tasks.all"
# 	],
# 	"daily": [
# 		"cheque_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"cheque_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cheque_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"cheque_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "cheque_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cheque_management.event.get_events"
# }


fixtures = [{"dt": "Custom Field", "filters": [["name", "in", [
		"Company-cb_00",
		"Company-cheques_default_accounts",
		"Company-cheques_under_collection_account",
		"Company-payable_notes_account",
		"Company-receivable_notes_account"
	]]]},
    {"dt": "Workflow", "filters": [["name", "like", 
        "%Cheques Cycle"
    ]]},
    {"dt": "Workflow State", "filters": [["name", "like", 
        "Cheque%"
    ]]},
    {"dt": "Workflow Action", "filters": [["name", "like", 
        "Cheque%"
    ]]}
]
