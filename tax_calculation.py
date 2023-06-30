from rich.console import Console
from rich.table import Table

# Prompt for input values
normal_earnings = float(input("Normal Taxable Earnings: "))
non_taxable_earnings = float(input("Total Earnings (excl Periodics): "))
travel_allowance = float(input("Taxable Value of Travel Allowance: "))
public_travel_allowance = float(input("Public Office and Travel Allowance: "))
reimbursive_travel = float(input("Taxable Value of Reimbursive Travel: "))
perks = float(input("Perks (Excluding Private RA's): "))
statutory_limits = float(input("Adjustments due to Statutory Limits: "))
annual_bonus = float(input("Provision for Tax on Annual Bonus: "))
company_contributions = float(input("Taxable Company Contributions: "))
deductions = float(input("Tax Deductible Deductions: "))
medical_aid_members = int(input("Number of people on Medical Aid: "))
age = int(input("Age: "))
total_taxable_amount = 0
tax_before_mtb = 0

# Calculate total taxable amount
total_taxable_amount = (
    normal_earnings
    + travel_allowance
    + public_travel_allowance
    + reimbursive_travel
    + perks
    + statutory_limits
    + annual_bonus
    + company_contributions
    - deductions
)

# Calculate tax rebate based on age
if age < 65:
    tax_rebate = 17235
elif age < 75:
    tax_rebate = 17235 + 9444
else:
    tax_rebate = 17235 + 9444 + 3145

# Determine tax bracket
if total_taxable_amount <= 237100:
    tax_rate = 0.18
    fixed_amount = 0
    tax_above = 0
elif total_taxable_amount <= 370500:
    tax_rate = 0.26
    fixed_amount = 42678
    tax_above = 237100
elif total_taxable_amount <= 512800:
    tax_rate = 0.31
    fixed_amount = 77362
    tax_above = 370500
elif total_taxable_amount <= 673000:
    tax_rate = 0.36
    fixed_amount = 121475
    tax_above = 512800
elif total_taxable_amount <= 857900:
    tax_rate = 0.39
    fixed_amount = 179147
    tax_above = 673000
elif total_taxable_amount <= 1817000:
    tax_rate = 0.41
    fixed_amount = 251258
    tax_above = 857900
else:
    tax_rate = 0.45
    fixed_amount = 644489
    tax_above = 1817000

# Calculate tax before medical tax credit
tax_before_mtb = (total_taxable_amount - tax_above) * tax_rate
tax_before_mtc = (tax_before_mtb + fixed_amount) - tax_rebate

# Calculate tax after medical tax credit
medical_tax_credit = (364 * 12) * medical_aid_members
final_tax = max(tax_before_mtc - medical_tax_credit, 0)

# Calculate monthly tax
monthly_tax = final_tax / 12

# Create a Table instance
table = Table(title="Result")

# Add columns to the table
table.add_column("Description", style="bold")
table.add_column("Amount", justify="right", style="bold")

# Add rows to the table
table.add_row("Total taxable amount", f"R {total_taxable_amount:,.2f}")
table.add_row("Taxable amount for the tax year", f"R {total_taxable_amount:,.2f}")
table.add_row("Fixed amount as per bracket", f"R {fixed_amount:,.2f}")
table.add_row("Total tax for the tax year", f"R {tax_before_mtc:,.2f}")
table.add_row("Medical Tax Credit", f"R {medical_tax_credit:,.2f}")
table.add_row("Final Tax", f"R {final_tax:,.2f}")
table.add_row("Monthly Tax", f"R {monthly_tax:,.2f}")

# Create a Console instance
console = Console()

# Print the table
console.print(table)
