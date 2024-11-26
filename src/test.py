from query import Query
from node import Node
from rdr import RDR
import random

# WORD_POOL_FEW = [   
#     "alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india",
#     "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo"]
# WORD_POOL = [
#     "alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india",
#     "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo",
#     "sierra", "tango", "uniform", "victor", "whiskey", "xray", "yankee", "zulu",
#     "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
#     "iguana", "jaguar", "koala", "lemur", "mongoose", "narwhal", "octopus", "penguin",
#     "quokka", "raven", "sparrow", "turtle", "umbrella", "vulture"
# ]

# # Function to create queries matching the patterns
# def generate_queries(list_of_word: list = WORD_POOL, type :str = 'ask'):
#     queries = []
#     for _ in range(100): 
#         if (type == 'ask' or type == 'mix'):
#           # Matching the 'ask_pattern'
#           ask_words = random.sample(list_of_word, random.randint(1, 4))  # Select 1-4 words
#           query_ask = ', '.join(ask_words) + '?'
#           queries.append(query_ask)
          

#         elif (type == 'add' or type == 'mix'):
#           # Matching the 'add_pattern'
#           add_words = random.sample(list_of_word, random.randint(0, 3))  # Select 1-3 words
#           result_word = random.choice(list_of_word)
#           query_add = ', '.join(add_words) + ' > ' + result_word
#           queries.append(query_add)

#     return queries

INSURANCE_CLAIM_QUERIES = '''collision, at-fault > requires inspection
collision, not at-fault > check third-party insurance
collision, no police report > request police report before processing
collision, at-fault, hit-and-run > apply uninsured motorist coverage
damage from animal > apply comprehensive coverage
damage from animal, parked vehicle > apply comprehensive coverage
hit-and-run, uninsured third party > apply uninsured motorist coverage
late claim filing > deny claim
late claim filing, theft > request explanation for delay
comprehensive > total loss evaluation
comprehensive, weather-related > total loss evaluation
comprehensive, theft, no police report > deny claim
claim exceeds $15000, medical expenses > verify medical coverage and adjust payout
claim exceeds $15000, multiple injuries, at-fault > flag for supervisor review
claim exceeds $15000, hit-and-run, uninsured motorist > flag for supervisor review
luxury vehicle > adjust payout for luxury vehicle standards
luxury vehicle, major damage > send for specialized adjuster review
luxury vehicle, stolen > verify police report and apply theft coverage
electric vehicle > adjust payout for ev repair costs
electric vehicle, battery damage > apply comprehensive coverage for battery replacement
electric vehicle, fire-related damage > adjust payout for ev-specific parts
vehicle total loss > adjust payout for aftermarket parts
vehicle total loss, modified aftermarket parts > adjust payout for aftermarket parts
vehicle total loss, flood damage > verify flood coverage endorsement
pre-existing damage > exclude pre-existing damage from payout
policy exclusion > deny claim
policy exclusion, racing-related accident > deny claim
driver intoxicated > deny claim
policy exclusion, driver intoxicated > deny claim
suspicious claim > flag for fraud review or request additional documents
suspicious claim, inflated repair costs > request secondary inspection
driver under 18 > adjust payout based on minor driver rules
collision, not at-fault, major damage > check third-party insurance
collision, not at-fault, minor damage > process claim under own coverage
collision, at-fault, major damage > requires inspection
collision, at-fault, minor damage > apply repair estimate
damage during off-road use > apply off-road coverage
damage during off-road use, no off-road coverage > deny claim
damage during off-road use, pre-existing damage > exclude pre-existing damage
hit-and-run, uninsured third party, major damage > apply uninsured motorist coverage
hit-and-run, uninsured third party, minor damage > apply uninsured motorist coverage for repairs
claim filed over 60 days > flag for fraud review
claim filed over 60 days, comprehensive > request explanation for late filing
claim filed over 60 days, multiple vehicles, at-fault, major damage > adjust payout for each vehicle involved
claim filed over 60 days, multiple vehicles, not at-fault, major damage > apply third-party insurance for each vehicle
claim exceeds $15,000, medical expenses > flag for supervisor review
theft, vehicle recovered with damage > apply comprehensive coverage for repairs
collision, uninsured motorist, at-fault > deny uninsured motorist coverage
flood damage > verify flood coverage endorsement
flood damage, uninsured third party > deny claim under third-party coverage'''

if __name__ == "__main__":


  rdr = RDR()
  queries = INSURANCE_CLAIM_QUERIES.split("\n")
  for query in queries:
    rdr.execute_query(Query(query))

  rdr.save_txt_tree("insurance_claim_knowledge")
  # rdr.save_json_tree("insurance_claim_knowledge")

  # rdr = RDR()
  # rdr.load_txt_tree()
  # rdr.print_tree()

  


