import yaml
from datetime import date
from jinja2 import Template

# Load controls
with open("controls/AnnexA.yaml", "r") as f:
    data = yaml.safe_load(f)

# Load Jinja2 template
with open("reports/soa_report_template.j2", "r") as t:
    template = Template(t.read())

# Render report
report = template.render(controls=data["controls"], date=date.today())

# Save output
with open("reports/Statement_of_Applicability.txt", "w") as f:
    f.write(report)

print("📄 Statement of Applicability generated successfully!")
