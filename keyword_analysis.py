import re
from collections import Counter

def get_top_keywords(texts, n=10):
    words = re.findall(r'\b\w+\b', ' '.join(texts).lower())
    stopwords = {'the', 'is', 'and', 'to', 'a', 'of', 'in', 'for'}
    filtered = [word for word in words if word not in stopwords and len(word) > 2]
    return Counter(filtered).most_common(n)
