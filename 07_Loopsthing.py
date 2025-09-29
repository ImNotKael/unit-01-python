# Created inputs used in the document
campaign_name = input("Enter campaign name: ")
email_list_input = input("Enter email addresses (comma-separated): ")
engagement_input = input("Enter engagement status for each email (comma-separated): ")

# Splitted the emails that is going to be inputted into a list so it would not print out the paranthesis and comas.
email_list = [email.strip().lower() for email in email_list_input.split(",")]
engagement_list = [status.strip().lower() for status in engagement_input.split(",")]

# Made sure to make the email valid so it doesn't make an error.
if len(email_list) != len(engagement_list):
    print("Error: Number of emails and engagement statuses do not match.")
    exit()

# Created a counter for the domain counts and the engagment summary.
domain_counts = {}
engagement_summary = {
    "opened": 0,
    "clicked": 0,
    "bounced": 0,
    "unsubscribed": 0
}

# Made sure to input the emails shown into the domain so it could count on what action it has done
for email, status in zip(email_list, engagement_list):
    domain = email.split("@")[-1]
    domain_counts[domain] = domain_counts.get(domain, 0) + 1

    if status in engagement_summary:
        engagement_summary[status] += 1

# Calculated the click rate based on the engagement summary
total_emails = len(email_list)
clicks = engagement_summary["clicked"]
click_rate = (clicks / total_emails) * 100  # 100 is percentage

# Created the click rate statements as if else statement to show the result based on the calculator.
if click_rate >= 50:
    success = "Excellent"
elif click_rate >= 30:
    success = "Good"
elif click_rate >= 10:
    success = "Average"
else:
    success = "Poor"

# printed out the results based on what the user inputted their data.
print("\n--- Campaign Report ---")
print(f"Campaign Name: {campaign_name}")
print("\nDomain Counts:")
for domain, count in domain_counts.items():
    print(f"  {domain}: {count}")

print("\nEngagement Summary:")
for key, value in engagement_summary.items():
    print(f"  {key.capitalize()}: {value}")

print(f"\nClick Rate: {click_rate:.2f}%")
print(f"Success Rating: {success}")
