import pandas as pd
from playwright.sync_api import sync_playwright

# Esta função contém toda a lógica que você criou
def extrair_dados_da_pagina(page):
    # Rola para garantir o carregamento
    page.mouse.wheel(0, 10000)
    page.wait_for_timeout(2000)
    
    dados_pagina = []
    
    # 1. Localiza TODOS os cards dos livros
    cards = page.locator(".zg-grid-general-faceout")
    
    # 2. Itera card por card (a forma mais segura de todas)
    for i in range(cards.count()):
        card = cards.nth(i)
        
        # Extração de Título/Autor (Usando seu seletor robusto)
        # Pegamos todos os textos de classe line-clamp dentro deste card
        textos = card.locator("[class*='line-clamp']").all_text_contents()
        titulo = textos[0].strip() if len(textos) > 0 else "N/A"
        autor = textos[1].strip() if len(textos) > 1 else "N/A"
        
        # Extração de Preço
        # Tentamos pegar o preço, se não existir, fica "N/A"
        preco_el = card.locator("._cDEzb_p13n-sc-price_3mJ9Z")
        preco = preco_el.inner_text().strip() if preco_el.count() > 0 else "N/A"
        
        # Extração de Nota e Avaliações (O ponto onde você tinha dúvida)
        # Buscamos o link das estrelas dentro deste card específico
        rating_el = card.locator("a.a-link-normal:has(.a-icon-star-small)")
        
        if rating_el.count() > 0:
            aria_label = rating_el.first.get_attribute("aria-label")
            partes = aria_label.split()
            nota = partes[0]
            qtd = partes[4].replace('.', '')
        else:
            # Caso não tenha classificação, preenchemos com 0
            nota = "0"
            qtd = "0"
            
        # Adiciona ao dicionário desta linha
        dados_pagina.append({
            'Titulo': titulo,
            'Autor': autor,
            'Preço': preco,
            'Nota': nota,
            'Qtd_Avaliacoes': qtd
        })
        
    return dados_pagina

# --- CÓDIGO PRINCIPAL ---
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.amazon.com.br/gp/bestsellers/books")
    
    # Extrai Página 1
    dados1 = extrair_dados_da_pagina(page)
    df1 = pd.DataFrame(dados1)
    
    # Navega para Página 2
    page.get_by_role("link", name="2", exact=True).click()
    page.wait_for_load_state("networkidle") # Espera a página carregar completamente
    
    # Extrai Página 2
    dados2 = extrair_dados_da_pagina(page)
    df2 = pd.DataFrame(dados2)
    
    # Junta as duas tabelas
    df_final = pd.concat([df1, df2], ignore_index=True)
    
    # Adiciona a coluna Ranking sequencial (1 até o total)
    df_final.insert(0, 'Ranking', range(1, len(df_final) + 1))
    
    print(df_final.tail(50))
    df_final['Nota'] = df_final['Nota'].str.replace(',', '.', regex=True)
    df_final.to_excel('parciais2.xlsx', index=False)
    
    browser.close()