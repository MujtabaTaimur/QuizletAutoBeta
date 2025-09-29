from .browser import launch_browser
from .auth import login
from .dataset import extract_set_data
from .modes import flashcards, learn, write, spell, match, test

def run_bot(username, password, set_urls, modes, headless=True):
    pw, browser, context, page = launch_browser(headless=headless)
    try:
        login(page, username, password)
        for url in set_urls:
            print(f"Processing set: {url}")
            page.goto(url)
            items = extract_set_data(page)
            if not items:
                print("Failed to extract terms for set:", url)
                continue

            # Create map for quick lookup
            term_map = {i.term.lower(): i.definition for i in items}
            def_map = {i.definition.lower(): i.term for i in items}

            selected_modes = ["flashcards","learn","write","spell","match","test"] if modes=="all" else modes
            for mode in selected_modes:
                print(f"Running mode: {mode}")
                if mode=="flashcards": flashcards.run(page)
                elif mode=="learn": learn.run(page, term_map, def_map)
                elif mode=="write": write.run(page, term_map, def_map)
                elif mode=="spell": spell.run(page, term_map, def_map)
                elif mode=="match": match.run(page, term_map, def_map)
                elif mode=="test": test.run(page, term_map, def_map)
    finally:
        browser.close()
        pw.stop()
