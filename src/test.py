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

INSURANCE_CLAIM_QUERIES = '''damage from animal, collision, at-fault > apply collision coverage
damage during off-road use, off-road coverage available > apply off-road coverage
claim exceeds $10000, hit-and-run, uninsured motorist > flag for supervisor review
claim, multiple vehicles, not at-fault, major damage > apply third-party insurance for each vehicle
suspicious information, claim filed over 60 days > flag for fraud review
damage from hit-and-run, no third-party insurance, major damage > apply uninsured motorist coverage
luxury vehicle, minor damage, comprehensive > adjust payout for luxury vehicle standards
claim exceeds $15000, multiple injuries, at-fault > flag for supervisor review
electric vehicle, battery damage, comprehensive > apply comprehensive coverage for battery replacement
pre-existing damage, comprehensive, theft > exclude pre-existing damage from payout
claim exceeds $15000, comprehensive, major damage > flag for supervisor review
collision, at-fault, major damage > requires inspection
hit-and-run, no insurance, vehicle identified > apply uninsured motorist coverage
damage from hit-and-run, no third-party insurance, minor damage > apply uninsured motorist coverage for repairs
driver intoxicated, collision, at-fault > deny claim
vehicle total loss, modified aftermarket parts, at-fault > adjust payout for aftermarket parts
late claim filing (More than 90 days), collision > deny claim
damage during off-road use, no off-road coverage, major damage > deny claim
policy exclusion, off-road use > deny claim for off-road damage
uninsured third party, hit-and-run, minor damage > apply uninsured motorist coverage for repairs
damage from animal, comprehensive > apply comprehensive coverage
damage from hit-and-run, police report > process under uninsured motorist coverage
damage from hit-and-run, no third-party insurance, major damage > apply uninsured motorist coverage
claim, multiple vehicles, at-fault, major damage > adjust payout for each vehicle involved
luxury vehicle, major damage, collision > send for specialized adjuster review
pre-existing damage, collision, at-fault > exclude pre-existing damage from payout
claim exceeds $15000, medical expenses > verify medical coverage and adjust payout
suspicious information, no supporting documents, major damage > deny claim
rideshare use, collision, not at-fault > process under rideshare coverage
no collision coverage, not at-fault, vehicle damage > deny collision claim
claim exceeds $10000, hit-and-run, uninsured motorist > flag for supervisor review
hit-and-run, police report, third-party identified > process uninsured motorist claim
electric vehicle, major damage, collision > adjust payout for ev repair costs
vehicle total loss, modified aftermarket parts, not at-fault > adjust payout for aftermarket parts
rideshare use, collision, at-fault > verify commercial coverage
collision, not at-fault, minor damage > process claim under own coverage
uninsured third party, hit-and-run, major damage > apply uninsured motorist coverage
damage from animal, collision, at-fault > apply collision coverage
suspicious information, no supporting documents, minor damage > request additional documents
electric vehicle, minor damage, collision > apply ev-specific repair coverage
no collision coverage, at-fault, vehicle damage > deny collision claim
damage during off-road use, no off-road coverage, major damage > deny claim
driver under 18, at-fault, minor damage > adjust payout based on minor driver rules
claim exceeds $15000, comprehensive, major damage > flag for supervisor review
pre-existing damage, comprehensive, theft > exclude pre-existing damage from payout
claim, multiple vehicles, at-fault, major damage > adjust payout for each vehicle involved
rideshare use, non-collision, theft > process under rideshare coverage for theft
uninsured third party, hit-and-run, no police report > deny claim
late claim filing (More than 90 days), comprehensive > deny claim
driver intoxicated, collision, not at-fault > deny claim
luxury vehicle, major damage, collision > send for specialized adjuster review
policy exclusion, unlicensed driver > deny claim
damage from hit-and-run, no third-party insurance, major damage > apply uninsured motorist coverage
claim exceeds $15000, medical expenses > verify medical coverage and adjust payout
rideshare use, collision, not at-fault > process under rideshare coverage
electric vehicle, battery damage, comprehensive > apply comprehensive coverage for battery replacement
collision, at-fault, minor damage > apply repair estimate
driver under 18, not at-fault, minor damage > adjust payout based on minor driver rules
damage from hit-and-run, no police report > process under uninsured motorist coverage
suspicious information, claim filed over 60 days > flag for fraud review'''

if __name__ == "__main__":


  rdr = RDR()
  queries = INSURANCE_CLAIM_QUERIES.split("\n")
  for query in queries:
    rdr.execute_query(Query(query))

  rdr.save_txt_tree("insurance_claim_knowledge")
  # rdr.save_json_tree("insurance_claim_knowledge")

  


