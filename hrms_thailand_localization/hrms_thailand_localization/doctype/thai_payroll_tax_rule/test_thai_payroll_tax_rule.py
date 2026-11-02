import unittest

import frappe

from hrms_thailand_localization.hrms_thailand_localization.doctype.thai_payroll_tax_rule.thai_payroll_tax_rule import (
	ThaiPayrollTaxRule,
)


class TestThaiPayrollTaxRule(unittest.TestCase):
	def test_rejects_reversed_effective_dates(self):
		rule = ThaiPayrollTaxRule(
			{"doctype": "Thai Payroll Tax Rule", "from_date": "2026-03-01", "to_date": "2026-02-28"}
		)
		with self.assertRaises(frappe.ValidationError):
			rule.validate()

	def test_accepts_open_ended_rule(self):
		rule = ThaiPayrollTaxRule({"doctype": "Thai Payroll Tax Rule", "from_date": "2026-03-01"})
		rule.validate()

	def test_accepts_same_day_rule(self):
		rule = ThaiPayrollTaxRule(
			{"doctype": "Thai Payroll Tax Rule", "from_date": "2026-03-01", "to_date": "2026-03-01"}
		)
		rule.validate()
