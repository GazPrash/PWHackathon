import pickle
import statistics

from statistics import mode


id = 244
MODEL_PATH = f"model/saved_models/model_{id}.pkl"
VECTOR_PATH = f"model/saved_models/wordvector_{id}.pkl"

emotions_map = {0 :'sadness', 1 :'anger', 2 : 'love', 3 : 'surprise', 4 :'fear', 5: 'joy'}
list = []

A = "It's been really cool chatting with you. From making some observations, I can tell you've been sad and Hey, if you're feeling down, don't worry - you're not alone. Reach out to someone you trust and let them know what's up. Make time for some self-love, like a nice hot bath or a refreshing walk. Don't let those negative thoughts bring you down - challenge them and set some small goals you can crush. And if those bad vibes stick around, don't hesitate to hit up a pro who can give you some guidance and support. You got this!  We update our initial quesion everyday, so different bonding each day. Make me your daily dairy and I'll always be happy to chatch up. "

B = "Good stuff dude! And since we've talked so long, I've made a few observations and gotta be real I've been sensing some off vibes. Yo, if you've got some anger issues, don't trip - there are ways to keep your cool. Try practicing mindfulness to keep yourself in check and not go off. Pinpoint your triggers, whether it's people or certain situations, and figure out how to dodge 'em or deal with 'em. Use some chill techniques like deep breathing or visualization to keep your rage at bay. And when you do feel that fire building up, express yourself calmly and respectfully using 'I' statements. But if things are getting too real and you need some backup, don't hesitate to hit up a mental health pro who can give you the guidance and support you need. We update our initial quesion everyday, so different bonding each day. Make me your daily dairy and I'll always be happy to chatch up."

C = "Great talks man, great talks. As a person who like to make a few observations, gotta tell ya, You are one romantic fella. And Hey! To keep your romance game strong, you gotta keep the communication flowing, make time for quality hangouts, show mad appreciation for your bae, be ready to forgive, and keep the sparks flyin' with cute little surprises and sweet gestures. We update our initial quesion everyday, so different bonding each day. Make me your daily dairy and I'll always be happy to chatch up."

D = "You're such a vibe! So from sensing different things, making a few observations. I feel like you are a bit 'overwhelmed'. Yo, when life's throwing too much at you, it's time to prioritize and get real about what needs to get done. Don't be afraid to ask for help or delegate tasks to others when you need to catch your breath. Make sure you're taking care of yourself by getting enough rest, chowing down on some healthy eats, and doing things that make you feel good. And remember, you don't have to handle it all on your own - hit up your squad or a pro who can help you get through the tough times. We update our initial quesion everyday, so different bonding each day. Make me your daily dairy and I'll always be happy to chatch up."

E = "Great convo man. From all the things that you said, I made a few observations and you stroke me a little bit fearful. Hey, if fear's got you shook, take a deep breath and know you can handle this. Try focusing on your breathing to chill your bod and bring those anxious feels down. Don't let negative thoughts run the show - challenge 'em and ask yourself if they're really legit. Speak kindly to yourself and think about the best possible outcomes. Take it one step at a time and gradually face your fears - you'll feel more confident as you go. And if you need some extra backup, reach out to a mental health pro who can help guide you through it. We update our initial quesion everyday, so different bonding each day. Make me your daily dairy and I'll always be happy to chatch up."

F = "Cool catching up man, you give off really elite, top of the class vibes. what can I can say. You seem preety chill and happy with how things are going. Keep it up! And don't forget to keep sharing the joy with people around you. We update our initial quesion everyday, so different bonding each day. Make me your daily dairy and I'll always be happy to chatch up."



def LoadModel():
    with open(MODEL_PATH, "rb") as f:
        clf = pickle.load(f)
    
    with open(VECTOR_PATH, "rb") as v:
        wordvec = pickle.load(v)

    return (clf, wordvec)

def most_common(List):
    return(mode(List))

def analyze(conversations):
    clf, wordvec = LoadModel()
    emotions = [0 for i in range(6)]
    
    for reply in conversations:
        corpus = wordvec.transform([reply]).toarray()
        output = clf.predict(corpus)
        emotions.append(emotions_map[output[0]])
        # emotions[output[0]] += 1
        
    



