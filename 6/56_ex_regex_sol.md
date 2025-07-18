1. Given the tweet "This pop concert by that really popular artist is great and I'm very glad I went to it. #Concert #Rizz #Yapping". Extract the hashtags.

```python
text = "This pop concert by that really popular artist is great and I'm very glad I went to it. #Concert #Rizz #Yapping"
print(re.findall(r"#\w+", text))
```

2. Given the blog post, extract the dates.
```python
s = """Get ready! Popular pop artist is hitting the road in 2025! Check out the full list of tour dates below and grab your tickets before they get picked up by bots in the first five seconds and resold a half dozen times.  (Which ticketmaster is totally ok with because they make a fraction of every resale)

Miami, FL – 03/15/2025

Atlanta, GA – 03/18/2025

New York, NY – 03/22/2025

Chicago, IL – 03/25/2025

Dallas, TX – 03/28/2025

Denver, CO – 04/01/2025

Seattle, WA – 04/04/2025

Los Angeles, CA – 04/07/2025

San Francisco, CA – 04/10/2025

Las Vegas, NV – 04/13/2025

For more info, VIP packages, and tickets, check out our site"""

dates = re.findall(r'\d{1,2}/\d{1,2}/\d{2,4}' s)
```

3. Strong passwords only.  Write a regex to ensure a password has numbers, letters uppercase, and letters lowercase.

```python
def is_strong(pw):
    return bool(re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$', pw))
```

