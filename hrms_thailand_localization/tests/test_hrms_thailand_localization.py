# Copyright (c) 2026, SpaceCode Co., Ltd. and contributors

import frappe
from frappe.tests import IntegrationTestCase


class TestHrmsThailandLocalization(IntegrationTestCase):
	"""Smoke tests: scaffolded app metadata must be exposed through hooks."""

	def test_app_hooks_are_registered(self):
		hooks = frappe.get_hooks()
		self.assertIn("hrms_thailand_localization", hooks.get("app_name", []))
		self.assertIn("HRMS Thailand Localization", hooks.get("app_title", []))
		self.assertIn("SpaceCode Co., Ltd.", hooks.get("app_publisher", []))
		self.assertIn("p@spacecode.co.th", hooks.get("app_email", []))

	def test_app_package_is_importable(self):
		import hrms_thailand_localization

		self.assertEqual(hrms_thailand_localization.__version__, "0.0.1")
