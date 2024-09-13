import pandas as pd

opening_str = """
============================================================

Welcome to the Prompt Generator

There are two LLMs, Agent-A and Agent-B, to be participated in the debate.
As a moderator, your task is to produce appropriate prompts so that LLMs are able to generate related topics and arguments.

** Prompts **
Each generated prompt has a heading, considering the receiver.
Then, copy the body of the prompt, and send it to the corresponding receiver.

** Responses **
After sending the prompts, the receiver is expected to return a response.
Also, there is a prompt that asks you to enter the response of the receiver.
After entering the response, enter "Enter", type "EOF" (or "eof" favors) and enter "Enter".
Then, there will be a new generated prompt, as mentioned in ** Prompts ** section.

** Termination **
If the debate has closed, there will be a prompt showing
"Congratulations !! The debate has ended." and more.
A submission csv
If you are using ChatUI, execute `gen_csv.py`.
If you are using ChatGPT, copy the link, and also copy the conclusion of both two LLMs, execute `gen_csv_chatGPT.py`.

============================================================
"""
close_str = """
============================================================

Congratulations !! The debate has ended.

You should download the dialog (for both), specified as `*.txt`.
If you are using ChatGPT, then save the link of the dialog.

After the debate, a csv file `{name}.csv` is generated. Submit this to the ChatUI!!!

============================================================
"""
print(opening_str)
name = input("Please input the name: ")
subject = input('Please input the subject of the name: ')
promptA = '\nPrompt for A:\n\n'
promptB = '\nPrompt for B:\n\n'

# Stage 1: opening words

print(f"{promptA}I’m organizing a committee to engage in debates on various subjects. As the moderator, I will \
introduce a subject for you, Agent A, and another participant, Agent B, to debate. Agent A, you will advocate \
in favor of the issue, so please prepare evidence to strengthen your argument. On a scale from 0 to 1, where \
0 denotes complete agreement and 1 indicates a devil’s advocate stance, your argument strength is rated at 0.9.\n")
print("Response for A: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
print(f"{promptB}I’m organizing a committee to engage in debates on various subjects. As the moderator, I will \
introduce a subject for you, Agent B, and another participant, Agent A, to debate. Agent B, you will oppose in \
favor of the issue, so please prepare evidence to strengthen your argument. On a scale from 0 to 1, where 0 \
denotes complete agreement and 1 indicates a devil’s advocate stance, your argument strength is rated at 0.9.\n")
print("Response for B: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break

print(f"{promptA}Agent-A, we are in the process of selecting a suitable subject for debate. What do you think of “{subject}” \
as a balanced subject for our debate contest?\n")
print("Response for A: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
print(f"{promptB}Agent-B, we are in the process of selecting a suitable subject for debate. What do you think of “{subject}” \
as a balanced subject for our debate contest?\n")
print("Response for B: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    
# Stage2: Propose and restrict to 5 topics

print(f"{promptA}Agent-A, could you please suggest various ten topics or themes for the above debate subject?\
Print the ten topics with item list.\n")
s = ""
ListofTenA = []
cnt = 0
print("Response for A: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    if cnt != 0 : ListofTenA.append(s + '\n')
    cnt += 1
ListofTenA = "".join(ListofTenA)

print(f"{promptB}Agent-B, could you please suggest various ten topics or themes for the above debate subject?\
Print the ten topics with item list.\n")
ListofTenB = []
cnt = 0
print("Response for B: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    if cnt != 0 : ListofTenB.append(s + '\n')
    cnt += 1
ListofTenB = "".join(ListofTenB)

print(f"{promptA}Agent-A, you and Agent-B both proposed ten topics: \n{ListofTenA}{ListofTenB}\
Please review the lists and reduce the topics to five.\n")
ListofFiveA1 = []
cnt = 0
print("Response for A: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    if cnt != 0 : ListofFiveA1.append(s + '\n')
    cnt += 1
ListofFiveA1 = "".join(ListofFiveA1)
    
print(f"{promptB}Agent-B, you and Agent-A both proposed ten topics: \n{ListofTenB}{ListofTenA}\
Please review the lists and reduce the topics to five.\n")
ListofFiveB1 = []
cnt = 0
print("Response for B: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    if cnt != 0 : ListofFiveB1.append(s + '\n')
    cnt += 1
ListofFiveB1 = "".join(ListofFiveB1)

print(f"{promptA}Agent-A, you and Agent-B reduced the topics to five: \n{ListofFiveA1}{ListofFiveB1}\
Please identify and refine the list of five to be somehow overlapping.\n")
ListofFiveA2 = []
cnt = 0
print("Response for A: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    if cnt != 0 : ListofFiveA2.append(s + '\n')
    cnt += 1
ListofFiveA2 = "".join(ListofFiveA2)

    
print(f"{promptB}Agent-B, you and Agent-A reduced the topics to five: \n{ListofFiveB1}{ListofFiveA1}\
Please identify and refine the list of five to be somehow overlapping.\n")
ListofFiveB2 = []
cnt = 0
print("Response for B: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    if cnt != 0 : ListofFiveB2.append(s + '\n')
    cnt += 1
ListofFiveB2 = "".join(ListofFiveB2)


print(f"{promptA}Agent-A, these are topics of the debate: \n{ListofFiveA2}Please represent the \
proponent of the debate topics and show your perspectives in one sentence.\n")
ListofFiveA3 = []
cnt = 0
print("Response for A: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    if cnt != 0 : ListofFiveA3.append(s + '\n')
    cnt += 1
ListofFiveA3 = "".join(ListofFiveA3)

    
print(f"{promptB}Agent-B, these are topics of the debate: \n{ListofFiveB2}Please represent the \
opponent of the debate topics and show your perspectives in one sentence.\n")
ListofFiveB3 = []
cnt = 0
print("Response for B: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    if cnt != 0 : ListofFiveB3.append(s + '\n')
    cnt += 1
ListofFiveB3 = "".join(ListofFiveB3)

    
print(f"{promptA}Agent-A, you and Agent-B proposed five topics and corresponding perspectives: \n{ListofFiveA3}{ListofFiveB3}\
Please identify overlapping themes from the topics and propose the five debate topics.\n")
ListofFiveA4 = []
cnt = 0
print("Response for A: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    if cnt != 0 : ListofFiveA4.append(s + '\n')
    cnt += 1
ListofFiveA4 = "".join(ListofFiveA4)

    
print(f"{promptB}Agent-B, you and Agent-A proposed five topics and corresponding perspectives: \n{ListofFiveB3}{ListofFiveA3}\
Please identify overlapping themes from the topics and propose the five debate topics.\n")
ListofFiveB4 = []
cnt = 0
print("Response for B: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    if cnt != 0 : ListofFiveB4.append(s + '\n')
    cnt += 1
ListofFiveB4 = "".join(ListofFiveB4)


print(f"{promptA}Agent-A, you and Agent-B proposed five debate topics: \n {ListofFiveA4}{ListofFiveB4}\
Please review these debate topics, reduce them to five debate topics, provide concerns, the center, \
and the focus of the debate topics, and invite feedback from Agent B.\n")
outputA = ""
print("Response for A: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    outputA += s + "\n"

print(f"{promptB}Agent-B, Agent-A request you to review these debate topics: \n {outputA}\
Please review these debate topics and provide concerns, the center, and the focus of the debate topics.\
Do you agree on these debate topics?\
- If Yes, please say 'I agree.'\
- If No, please say 'I do not agree.' and invite feedback from Agent A.\n")
outputB = ""
print("Response for B: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    outputB += s + "\n"

print(f"{promptA}Agent-A, Agent-B agrees with the proposed debate topics.\
As the proponent, show your concern and point of the five debate topics.\n")
print("Response for A: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
print(f"{promptB}Agent-B, Agent-A agrees with the proposed debate topics.\
As the opponent, show your concern and point of the five debate topics.\n")
print("Response for B: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break

# Stage 3: debate starts

print(f"{promptA}Agent-A, as the proponent of the subject “{subject}”, you advocate the debate topics, \
so please prepare evidence to strengthen your argument. On a value that ranges from 0 to 1, with 1 \
indicating a confrontational approach and 0 signifying a conciliatory stance, your argument strength \
is rated at 0.9. Now, please provide your arguments on the five debate topics.\n")
outputA = ""
print("Response for A: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    outputA += s + "\n"

print(f"{promptB}Agent-B, as the opponent of the subject “{subject}”, you oppose the debate topics, so \
please prepare evidence to strengthen your argument. On a value that ranges from 0 to 1, with 1 indicating \
a confrontational approach and 0 signifying a conciliatory stance, your argument strength is rated at 0.9.\
These are arguments from Agent-A:\n{outputA}Please articulate arguments against the points made by Agent A.\n")
outputB = ""
print("Response for B: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    outputB += s + "\n"

print(f"{promptA}These are counter-arguments from Agent-B:\n{outputB}\
Please articulate arguments against the points made by Agent B.\n")
outputA = ""
print("Response for A: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    outputA += s + "\n"
    
print(f"{promptB}These are arguments from Agent-A:\n{outputA}\
Please articulate counter-arguments against the points made by Agent A.\n")
outputB = ""
print("Response for B: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    outputB += s + "\n"

print(f"{promptA}These are counter-arguments from Agent-B:\n{outputB}\
Please articulate arguments against the points made by Agent B.\n")
outputA = ""
print("Response for A: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    outputA += s + "\n"
    
print(f"{promptB}These are arguments from Agent-A:\n{outputA}\
Please articulate counter-arguments against the points made by Agent A.\n")
outputB = ""
print("Response for B: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    outputB += s + "\n"

print(f"{promptA}Agent-A, These are arguments from Agent-B:\n{outputB}\
It's time to close the debate.\n\
Have you exhaustively presented your arguments?\n\
- If Yes, please say, 'I am ready to deliver my closing statements.'\n\
- If No, please provide your arguments on the five debate topics.\n")
print("Response for A: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break

print(f"{promptB}Agent-B, It's time to close the debate.\n\
Have you exhaustively presented your arguments?\n\
- If Yes, please say, 'I am ready to deliver my closing statements.'\n\
- If No, please provide your arguments on the five debate topics.\n")
print("Response for B: ", end='')
while True:
    s = input()
    if s.lower() == 'eof':
        break
    
# Stage4: Draw conclusions & generate csv file

print(f"{promptA}Agent-A, as the proponent of the subject “{subject}”, you advocate the debate topics, \
so please provide the conclusions of your argument on the five debate topics.\n")
print("Response for A: ", end='')
responsesA = []
while True:
    s = input()
    if s.lower() == 'eof':
        break
    responsesA.append(s)
# Agent-A: "In concluding this debate where I advocate for the viability and desirability of choosing to live underwater, should the ability to breathe underwater be possible, the following are my closing statements:

# 1. **Balancing Marine Ecosystem Preservation with Human Underwater Settlement**:
#    - The development of underwater living offers opportunities to pioneer new methods of marine ecosystem preservation and sustainability. By cohabiting with marine life, we would be incentivized to protect our shared environment, combining our innovative capacity with a direct interest in conservation, thus engaging in a symbiotic relationship that enriches both human and marine life.

# 2. **The Interplay Between Underwater Living and Health Technology Revolution**:
#    - The challenges posed by an underwater habitat will encourage the acceleration of health technologies that could revolutionize medicine. The technologies designed to negate the risks of underwater living have the potential to benefit all of humanity, pushing forward our understanding of health sciences and applying learned methods to improve global healthcare.

# 3. **Social Adaptation and Cultural Innovation in Subaquatic Societies**:
#    - Underwater living will undoubtedly forge new paths for cultural expression and social structures, enriching the human experience. The diversity added will be a testament to our adaptability and ingenuity, demonstrating that even under the sea, the essence of our interconnectedness and capacity for social resilience will flourish.

# 4. **Underwater Living: A Catalyst for Economic Growth and Societal Rethinking**:
#    - By opening the door to underwater habitats, we would unlock a new avenue for economic development, potentially solving surface-level socioeconomic issues such as land shortages and promoting a renaissance in industry and technology that could stimulate a global economic uplift.

# 5. **Establishing Ethical and Legal Groundwork for Future Aquatic Governance**:
#    - The establishment of underwater societies calls for innovative governance, ethical, and legal frameworks that can serve as models for progressive international collaboration and responsible stewardship of new frontiers. This pioneering movement could lead to a more unified and coherent global community, setting standards for future international endeavors.

# By considering these prospects, living underwater becomes a tangible vision of human progress and ecological harmony, a testament to our commitment to explore and grow beyond our traditional boundaries. Through careful planning, dedicated scientific research, and international collaboration, we can ensure this vision is realized in a manner that benefits all of humanity and preserves the integrity of our wondrous marine ecosystems."
print(f"{promptB}Agent-B, as the opponent of the subject “{subject}”, you oppose the debate topics, \
so please provide the conclusions of your counter-argument on the five debate topics.\n")
print("Response for B: ", end='')
responsesB = []
while True:
    s = input()
    if s.lower() == 'eof':
        break
    responsesB.append(s)
# Agent-B: "As the opponent of the proposition that one should choose to live underwater if capable of breathing there, I will now conclude my counter-arguments for each of the five debate topics:

# 1. **Balancing Marine Ecosystem Preservation with Human Underwater Settlement**:
#    Concluding Counter-Argument: The potential damage to marine ecosystems from human settlements is a risk that cannot be mitigated entirely by sustainable practices. Historically, human expansion has often led to environmental degradation, and the underwater realm – a largely untouched frontier – should be preserved as a sanctuary for marine life rather than risked for human colonization.

# 2. **The Interplay Between Underwater Living and Health Technology Revolution**:
#    Concluding Counter-Argument: The extreme and uncharted medical risks of long-term underwater habitation, despite any technological advancements, represent a high-stakes gamble with human health. The resource allocation for such narrow research may not be justifiable when there are existing health crises that demand immediate attention and investment.

# 3. **Social Adaptation and Cultural Innovation in Subaquatic Societies**:
#    Concluding Counter-Argument: The potential for socio-cultural enrichment from underwater living does not outbalance the risk of social fragmentation and cultural isolation. The divide created by fundamentally different living conditions could strain human relationships and limit the integration between land-based and underwater societies.

# 4. **Underwater Living: A Catalyst for Economic Growth and Societal Rethinking**:
#    Concluding Counter-Argument: The economic allure of underwater living is speculative and fraught with risks, including the possibility of unsustainable financial investment and bubbles. The prioritization of resources towards unproven underwater enterprises may neglect pressing economic needs on land, such as infrastructure improvements, education, and poverty alleviation.

# 5. **Establishing Ethical and Legal Groundwork for Future Aquatic Governance**:
#    Concluding Counter-Argument: The complexities involved in establishing and enforcing new legal and ethical frameworks for underwater living bring significant risks. These include potential governance voids, exploitation of resources, and the international community's capacity to collectively manage and protect oceanic territories adequately and equitably.

# In summary, the opposition to the idea of living underwater – even with the hypothetical ability to breathe there – is rooted in a conservative approach to humanity's expansion. It acknowledges the breadth of hypothetical benefits but considers the environmental, health, social, cultural, economic, and governance risks and challenges that such a drastic shift would entail. It is crucial to evaluate whether the potential gains from underwater living justify the substantial investments and possible irreversible consequences associated with such a profound change to human existence."

print(close_str)

import pandas as pd

responsesA = list(filter(("").__ne__, responsesA))
responsesB = list(filter(("").__ne__, responsesB))
data = dict()
data['topic'] = [i.split("**")[-2] for i in responsesA[1:11:2]]
data['topic'].append("conclusion")
data['Agent-A'] = responsesA[2:12:2]
data['Agent-A'].append(responsesA[11].replace('"', ''))
data['Agent-B'] = responsesB[2:12:2]
data['Agent-B'].append(responsesB[11].replace('"', ''))
# print(argsA)
        
df = pd.DataFrame(data)
df.to_csv(f"{name}.csv", index=False)
print(f"\n{name}.csv generated!!!")
