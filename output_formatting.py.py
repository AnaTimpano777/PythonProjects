#Name: Ana Timpano
#Course Code: ICS3U
#Program Description: This program shows how output formatting is used in Python

# Assigning variables 
valuein = 123456.956778

# Output the value without formatting
print ("The un-formatted value is: ", valuein)

# You can format to any decimal place, just by editing the format string and changing to suit your needs.

# Formats to 3 decimal places
print ("The value formatted to 3 decimal places is: {0:12,.3f}".format(valuein))
# Formats to 2 decimal places
print ("The value formatted to 2 decimal places is: {0:12,.2f}".format(valuein))
# Formats to 1 decimal place
print ("The value formatted to 1 decimal place is: {0:12,.1f}".format(valuein))
