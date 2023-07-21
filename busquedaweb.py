from duckduckgo_search import DDGS

with DDGS() as ddgs:
    for r in ddgs.text('pension alimenticia jurisprudencia argentina', region='ar-es', safesearch='Off', timelimit='y'):
        print(r)