import time
from datetime import datetime

# Get curren epoch time with decimal precision
epoch_time = time.time()

# Format epoch time
scientific_notation = "{:g}".format(epoch_time)
formatted_epoch_time = f"{epoch_time:,.4f}"

# Get the current date
current_date = datetime.now().strftime("%b %d %Y")

# Print output
print(f"Seconds since January 1, 1970: {formatted_epoch_time} or {scientific_notation} in scientific notation")
print(current_date)

# Key caracteristic of Epoch time
# - Reference Point The starting point is always January 1, 1970, 00:00:00 UTC.
# - Continuous Counting
# - Timezone Independent
# - Precision (float - include fractions of a second)
# Simplicity: It's a single, continuously increasing number.
# Efficiency: Faster to store and compare than date strings.
# Interoperability: Universally supported across platforms and languages.