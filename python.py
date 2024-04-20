with open("random_paragraphs.txt") as file:
    contents = file.read()
    print(contents)
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download the stopwords corpus if you haven't already
nltk.download('stopwords')
nltk.download('punkt')

# Load the stop words
stop_words = set(stopwords.words('english'))


text = contents

# Tokenize the text
words = word_tokenize(text)

# Remove stop words
filtered_text = [word for word in words if word.lower() not in stop_words]

# Join the words back into a single string
filtered_text = ' '.join(filtered_text)


#print(filtered_text)
import re
from nltk import FreqDist


# Split the filtered_text into a list of words based on the specified pattern
words_list = re.split(r'[ ,.?!\n\(\)\[\]]+', filtered_text)

# Calculate the frequency distribution
freq_dist = FreqDist(words_list)

# Print the frequency of each word
for word, frequency in freq_dist.items():
    print(f"{word}: {frequency}")
print(freq_dist['two'])







    