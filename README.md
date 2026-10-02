# HRMS Thailand Localization

Thailand localization for ERPNext

HRMS Thailand Localization provides Thailand-specific HR and payroll
localization on top of ERPNext, targeting Frappe/ERPNext `version-16`.
It is intended to hold Thai tax, social security, and payroll-related
customizations as the project evolves.

## Requirements

- Frappe Framework `version-16`
- ERPNext `version-16`

## Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch version-16
bench install-app hrms_thailand_localization
```

## Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/hrms_thailand_localization
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

## CI

This app uses GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app on a Frappe `version-16` bench and runs unit tests on every push to the `version-16` branch and on every pull request.
- Linters: Runs [pre-commit](https://pre-commit.com) hooks and [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules), plus a [pip-audit](https://pypi.org/project/pip-audit/) vulnerable dependency check, on every pull request.

## License

MIT
