import re

def analyze_email_domains(data):
    # Identify publishers that look like email addresses
    email_publishers = data[data['publisher'].str.contains('@', na=False)]
    
    # Extract domain names from email addresses
    email_publishers['domain'] = email_publishers['publisher'].apply(lambda x: re.findall(r'@([\w\.-]+)', x)[0])
    
    # Count the number of articles per domain
    domain_counts = email_publishers['domain'].value_counts()
    
    return domain_counts
