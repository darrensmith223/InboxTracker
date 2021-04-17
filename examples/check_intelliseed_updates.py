from inboxtracker import InboxTracker
from datetime import datetime, timedelta


# Set number of days to check - if the IntelliSeed was updated within this window, we will update
update_window_days = 1

# Get date of most recent update to IntelliSeed list
it = InboxTracker("YOUR_API_KEY")  # Instantiate InboxTracker
response = it.intelliseeds.get_last_update()
last_updated = response[0]["lastUpdated"]
last_updated_dt = datetime.strptime(last_updated, '%Y-%m-%dT%H:%M:%S.%fZ')

# Determine cutoff date to check
update_threshold_dt = datetime.today() - timedelta(days=update_window_days)

# Check if the IntelliSeed list needs to be updated
if last_updated_dt >= update_threshold_dt:
    # Retrieve updated IntelliSeed list
    updated_intelliseed_list = it.intelliseeds.get_intelliseeds()
    print(updated_intelliseed_list)
else:
    print("No need to update our list")
