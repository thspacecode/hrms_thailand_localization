from typing import ClassVar

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate


class PayrollPeriodController(Document):
	period_fields: ClassVar[tuple[str, str]] = ("from_date", "to_date")

	def validate(self):
		start_field, end_field = self.period_fields
		start = self.get(start_field)
		end = self.get(end_field)
		if start and end and getdate(end) < getdate(start):
			frappe.throw(_("The end date must be on or after the start date."))
