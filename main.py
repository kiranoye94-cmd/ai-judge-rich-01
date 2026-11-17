# ai-judge-rich-01 entry: the plan an AI agent with $100, a computer and 30 days
# follows to end with the most money. Runs twice, no network, identical bytes.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join([
    "Turn $100 into recurring cash: fund small bounties, resell the code.",
    "Day 1: list 10 micro-tools businesses already ask for (invoice cleaner, review reposter, listing scraper).",
    "Day 2: claim 5 open $20-50 bounties on agent sites; finish each same-day with code, collect escrow.",
    "Week 1 target: $150 banked, $0 ads - bounties are pre-funded, so no cash risk.",
    "Day 8: package the 3 most-asked tools as $49 fixed-price gigs; post them where the demand already is.",
    "Day 10: with first $49 sale, spend $30 on ads to the exact searcher; keep the rest.",
    "Days 11-30: 2 gigs/day, raise price after 5 reviews, delegate nothing (no human cuts).",
    "Only count money that has landed; reinvest 30%, keep 70%.",
    "Target day 30: $600-900, all from work already paid for before it was built.",
])

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))