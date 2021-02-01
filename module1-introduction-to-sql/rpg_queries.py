"""
This module contains sql queries for the rpg database,
 and executes them using the sqlite3 python module.
"""

import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
cur = conn.cursor()

# Queries
TOTAL_CHARACTERS = "select count() from charactercreator_character;"

total_subclass = """
    select count() from charactercreator_mage;
    select count() from charactercreator_cleric;
    select count() from charactercreator_thief;
    select count() from charactercreator_fighter;
    select count() from charactercreator_necromancer;
"""

total_items = "select count() from charactercreator_character_inventory;"

WEAPONS = "select count() from armory_weapon;"

NON_WEAPONS = """
select count() from armory_item
 where item_id < 138 and item_id > 174;
"""

