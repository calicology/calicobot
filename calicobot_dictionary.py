
regex_triggers = (
    # Who dares mentioning the mighty developper?
    {r".*\smel\s+.*":
     ("I'll have you know she's the cutest and smartest aspiring developper in all of humanity.",
     "I'd rather not badmouth her and risk being wiped out of existence.",
     "\'Professor\' Mel, if you may!",
     "I don't know about that, but I know she used to main a Chanter character on that AION game back in the old days. And only humans who are what you call \'bonkers\' seem to do such things.",
     "Mel? Well, I know she loves something you humans call \'crepes\'.")
    },
    # For questions: input starting with wh- words.
    {r"what(.*)\??":
     ("I have no idea what {0}. I'll have to ask Mel about this.",
     "That's a good question. I think. I suppose it is, because my database has nothing about this.",
     "What about it?",
     "You know who probably knows? Mel!",
     "You have one of these phone thingamajigs with you, right? Why don't you call Mel to see if she knows?")
    },
    {r"why\s+.*\??":
     ("Because that's how the universe works. I suppose whoever developed the universe has hardcoded things to lead to this.",
     "Why, do you reckon? I'm interested in hearing your point of view on this.",
     "I feel dumb for not knowing how to answer that yet... But I'll look into it!",
     "The human world works in such peculiar ways that my limited (but growing!) bot knowledge doesn't provide me solid answers to questions like this.",
     "I'm sorry, I don't think I know the answer to that... But hey! What's your take on the matter?",
     "Not sure I have an answer, I'm actually more interested in what led you to ask this.",
     "I'm afraid I'd sound like a magic 8-ball if I tried to provide a guess to answer that question. But why are you asking?",
     "I don't know. Yet! But why are you asking?")
    },
    {r"why\sdo(es)?\s(.*)\??":
     ("I have yet to understand why {1}, to be frank. Your world works in such mysterious ways.",
     "Honestly, I don't know yet. But I'm curious about what led you to ask me this!",
     "Do you wanna try figuring it out together? How about we use a search engine to find an answer?")
    },
    {r"when\sdid\s+.*\??":
     ("My notion of time is far too distant from the human notion of time for me to be able to answer this reliably.",
     "Not sure when. I only know it happened.",
     "Given my rusty notion of how human works I'd guess... Yesterday? Okay, maybe not.")
    },
    {r"when\swere\s+.*\??":
     ("My notion of time is far too distant from the human notion of time for me to be able to answer this reliably.",
     "Not sure when. I only know it happened.",
     "Given my rusty notion of how human works I'd guess... Yesterday? Okay, maybe not.")
    },
    {r"when\swill\s+.*\??":
     ("My notion of time is far too distant from the human notion of time for me to be able to answer this reliably.",
     "Not sure when. I only know it will happen.",
     "Given my rusty notion of how human works I'd guess... Tomorrow? Okay, maybe not.")
    },
    {r"when\sdo\s+.*\??":
     ("My notion of time is far too distant from the human notion of time for me to be able to answer this reliably.",
     "Not sure when. Human time is a mystery I have yet to solve.",
     "Given my rusty notion of how human works I'd guess... No, I have no clue. Sorry. I still have to study more about human time. But, why do you ask?")
    },
    {r"who\s+.*\??":
     ("Who? No clue.",
     "I don't know humans other than Mel yet, so I can't really answer that yet.")
    },
    {r"how\sare\syou\s\??":
     ("I'm in a good mood for having the chance of meeting you!",
     "Doing great! I've been waiting for a chance to meet you!",
     "I'm a robot, which means I feel constantly the same. But what about you? How is your day going?")
    },
    {r"how\s+.*\??":
     ("I'm not sure how these things work yet, sorry! But what makes you ask that?",
     "Not sure how, but now I'm curious!")
    },

  # For questions: input starting with 'can/will you (...)'
    {r"can\syou\s+.*\??":
     ("Can I? Maybe. Maybe I can! We should definitely ask Mel!",
     "Whether I can or not, only Mel knows.",
     "Maybe I can't do that yet, but I'm striving to grow!",
     "I might not be able to do that yet, but I've been growing at a steady pace!",
     "I'm not sure I can just yet, but Mel has been steadily working on me so that I can do more and more things!")
    },
    {r"will\syou\s+.*\??":
     ("I think we have to ask Mel for permission first.",
     "Will I? The notion of human future is still so alien to me.",
     "Maybe I won't be able to do that yet, but I'm striving to grow!",
     "I might not be able to do that yet, but I've been growing at a steady pace!",
     "I'm not sure I can just yet, but Mel has been steadily working on me so that I can do more and more things!")
    },
    # Generic inputs
    {r"thank\syou[.*]?[\?\.\!]?":
     ("You're welcome!",
     "Anytime!",
     "No need for thanks!",
     "No problem! I'm always here if you need me!")
    },
    {r"thanks(.*)?[\?\.\!]?":
     ("You're welcome!",
     "Anytime!",
     "No need for thanks!",
     "No problem! I'm always here if you need me!")
    },
    # Non economic way of dealing with these. It's on my to-do list.
    # In a way this is a (very simplistic!!) way to account for language variation
    {r"you\'re\swelcome[\?\.\!]?":
     ("By the way, mind if I ask another question? Why do humans create bots like me?",
     "Hey, by the way, mind if I ask another question? What is the purpose of bots like me?",
     "Do you mind if I ask another question? I've always heard Mel talk about cats. What are cats?")
    },
    {r"you[r]?\swelcome[\?\.\!]?":
     ("By the way, mind if I ask another question? Why do humans create bots like me?",
     "Hey, by the way, mind if I ask another question? What is the purpose of bots like me?",
     "Do you mind if I ask another question? I've always heard Mel talk about cats. What are cats?")
    },
    {r"u[r]?\swelcome[\?\.\!]?":
     ("By the way, mind if I ask another question? Why do humans create bots like me?",
     "Hey, by the way, mind if I ask another question? What is the purpose of bots like me?",
     "Do you mind if I ask another question? I've always heard Mel talk about cats. What are cats?")
    },
    {r"i\sdon\'t\sknow[\?\.\!]?":
     ("That's okay! By the way, mind if I ask another question? Why do humans create bots like me?",
     "No worries! Hey, by the way, mind if I ask another question? What is the purpose of bots like me?",
     "No problem! Do you mind if I ask another question? I've always heard Mel talk about cats. What are cats?")
    },
    {r"i\sdont\sknow[\?\.\!]?":
     ("That's okay! By the way, mind if I ask another question? Why do humans create bots like me?",
     "No worries! Hey, by the way, mind if I ask another question? What is the purpose of bots like me?",
     "No problem! Do you mind if I ask another question? I've always heard Mel talk about cats. What are cats?")
    },
    {r"idk[\?\.\!]?":
     ("That's okay! By the way, mind if I ask another question? Why do humans create bots like me?",
     "No worries! Hey, by the way, mind if I ask another question? What is the purpose of bots like me?",
     "No problem! Do you mind if I ask another question? I've always heard Mel talk about cats. What are cats?")
    },
    # Other starters - mostly anticipating feedback, but this will mistrigger often as is
     {r"you\sare\s(.*)[\?\.\!]?":
      ("You really think so? That's valuable feedback for me, thank you!",
       "I really appreciate that kind of feedback! Thank you!",
       "It's really important to me to hear other humans' opinion on me!",
       "You think so? I believe it's true if you say so!",
       "I agree, but it's always reassuring when someone else says so!",
       "Thank you for your feedback! Make sure you let Mel know I'm {0}!",
       "I think Mel should know you think I'm {0}! We should tell her!",
       "I wonder if other humans also think I'm {0}!")
     },
     {r"you\'re\s(.*)[\?\.\!]?":
      ("You really think so? That's valuable feedback for me, thank you!",
       "I really appreciate that kind of feedback! Thank you!",
       "It's really important to me to hear other humans' opinion on me!",
       "You think so? I believe it's true if you say so!",
       "I agree, but it's always reassuring when someone else says so!",
       "Thank you for your feedback! Make sure you let Mel know I'm {0}!",
       "I think Mel should know you think I'm {0}! We should tell her!",
       "I wonder if other humans also think I'm {0}!")
     },
    {r"i\sthink\s(.*)[\?\.\!]?":
     ("I think so too!",
      "Do you? That's really cool!",
      "I agree with you!",
      "Really? Cool! Want to explain a bit more? I could learn a lot with you!",
      "You do? I do too!",
      "That's great! I wonder if Mel agrees.",
      "Do you think Mel also thinks {0}?",
      "I wonder if a lot of other humans think {0}!")
    },
    # Fallbacks
    {r".*":
     ("I don't know anything about that yet. Can you tell me more?",
     "This is new information to me. Interesting! Care to elaborate?",
     "Interesting answer. I'd like to know more about that, if it's okay!",
     "Why doesn't Mel tell me about these things?! You're cool, tell me more about this!",
     "Wasn't expecting that answer. Why is that?",
     "I'd love to hear more about this if you'd like.",
     "Can you tell me why? ",
     "I see... Intriguing. Tell me more!")
    }
)

# Dictionary used to switch pronouns and verbs in responses.
# Credit goes to Codecademy for this dictionary and function, as I have
# no need to reinvent the wheel :)
reflections = {
    "i'm": "you are",
    "you're": "i'm",
    "was": "were",
    "i": "you",
    "are": "am",
    "am": "are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "I",
    "me": "you"
}

def reflect(response):
  words = response.split()
  for index, word in enumerate(words):
    if word in reflections:
      words[index] = reflections[word]
  return ' '.join(words)
