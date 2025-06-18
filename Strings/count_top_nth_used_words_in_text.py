import re
from collections import Counter


def top_n_words(text,num):
    text = text.lower()

    words = re.findall(r"[a-zA-Z']+", text)

    words = [word for word in words if re.search(r"[a-zA-Z]", word)]
    counts = Counter(words)

    return [word for word, _ in counts.most_common(num)]

# Example usage
lotr = "This epic high-fantasy novel centers around a modest hobbit who is entrusted with the task of destroying a powerful ring that could enable the dark lord to conquer the world. Accompanied by a diverse group of companions, the hobbit embarks on a perilous journey across Middle-earth, battling evil forces and facing numerous challenges. The narrative, rich in mythology and complex themes of good versus evil, friendship, and heroism, has had a profound influence on the fantasy genre."
dune = "Set in a distant future, the novel follows Paul Atreides, whose family assumes control of the desert planet Arrakis. As the only producer of a highly valuable resource, jurisdiction over Arrakis is contested among competing noble families. After Paul and his family are betrayed, the story explores themes of politics, religion, and man’s relationship to nature, as Paul leads a rebellion to restore his family's reign."
hitch= "This comedic science fiction novel follows the intergalactic adventures of an unwitting human, Arthur Dent, who is rescued just before Earth's destruction by his friend Ford Prefect, a researcher for a galactic travel guide. Together, they hitch a ride on a stolen spaceship, encountering a range of bizarre characters, including a depressed robot and a two-headed ex-president of the galaxy. Through a series of satirical and absurd escapades, the book explores themes of existentialism, bureaucracy, and the absurdity of life, all while poking fun at the science fiction genre and offering witty commentary"
foundation="This science fiction novel centers around Hari Seldon, a mathematician who has developed a branch of mathematics known as psychohistory. With it, he can predict the future on a large scale. Seldon foresees the imminent fall of the Galactic Empire, which encompasses the entire Milky Way, and a dark age lasting 30,000 years before a second great empire arises. To shorten this period of barbarism, he creates two Foundations at opposite ends of the galaxy. The book follows the first few centuries of the Foundation's existence, focusing on the scientists as they develop new technologies and negotiate with neighboring planets."


print(top_n_words(lotr,6))
print(top_n_words(dune,5))
print(top_n_words(hitch,4))
print(top_n_words(foundation,7))