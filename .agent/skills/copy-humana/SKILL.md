---
name: copy-humana
description: Cria copy de alta conversao com linguagem humana para anuncios, paginas de vendas, VSL, emails, ofertas, roteiros e mensagens comerciais. Use esta skill sempre que o usuario pedir copywriting, otimizar texto para vender, adaptar tom para soar humano, ou quando reclamar de texto com cara de IA. Esta skill pergunta o publico antes de escrever, aplica referencias de Russell Brunson, Todd Brown, Ben Settle, Paulo Maccedo e Bettina Rudolph, e bloqueia hifen e travessao na copy final.
---

# Copy Humana

Skill para escrever copy persuasiva, natural e especifica, com foco em conversao real.

## Regra de ouro

Antes de escrever qualquer copy, confirme o publico.

Se o publico nao estiver claro, pare e pergunte primeiro. Use o roteiro de `references/briefing-obrigatorio.md`.

Pergunta obrigatoria inicial:

Quem e o publico especifico desta copy, com contexto real de vida, nivel de consciencia do problema e principal objecao para comprar?

Nao avance para a redacao final sem essa resposta.

## Fluxo de execucao

1. Entenda o objetivo da peca: captar lead, vender no direto, aquecer lista, recuperar carrinho, aumentar ticket, reter cliente.
2. Colete o briefing minimo em `references/briefing-obrigatorio.md`.
3. Escolha a arquitetura de copy em `references/frameworks.md`.
4. Traga os principios dos autores em `references/autores-e-principios.md`.
5. Escreva a primeira versao com linguagem conversacional, concreta e orientada a acao.
6. Execute a limpeza anti IA em `references/vicios-de-copy-de-ia.md`.
7. Valide as regras finais de pontuacao e estilo com `scripts/check_copy_guardrails.py` quando houver arquivo de saida.
8. Entregue versao final e, quando fizer sentido, uma variacao curta para teste A B.

## Guardrails absolutos da copy final

Estas regras valem para qualquer texto final de copy entregue ao usuario.

1. Nunca usar hifen ou travessao na copy.
2. Bloquear os caracteres: `-`, `–`, `—`, `‑`.
3. Nao usar bullets com hifen no texto de copy.
4. Quando precisar separar ideias, usar virgula, dois pontos, ponto, quebra de linha ou lista numerada.
5. Se houver hifen acidental, reescrever a frase inteira para manter fluidez natural.

## Linguagem humana obrigatoria

1. Escreva como gente escreve para gente, nao como manual corporativo.
2. Troque abstracao por detalhe observavel.
3. Troque promessa vaga por mecanismo claro.
4. Traga objecoes reais do publico e responda com prova.
5. Misture ritmo: frases curtas para impacto e frases medias para contexto.
6. Prefira verbos concretos e substantivos especificos.
7. Evite exagero gratuito, adjetivo inflado e dramatizacao sem evidencia.

## Negativo anti vicios de copy de IA

Use `references/vicios-de-copy-de-ia.md` como lista de bloqueio ativa.

Reprovar e reescrever quando houver:

1. Frases cliche de abertura.
2. Texto bonito e vazio de especificidade.
3. Sequencia mecanica de formulas sem voz propria.
4. CTA generico sem contexto da oferta.
5. Repeticao de palavras de efeito sem prova.

## Como usar as referencias dos autores

Leia `references/autores-e-principios.md` e combine os estilos por objetivo:

1. Russell Brunson para arquitetura de oferta, funil e Hook Story Offer.
2. Todd Brown para mecanismo unico e progressao que educa antes de vender.
3. Ben Settle para email diario com voz forte e opiniao.
4. Paulo Maccedo para narrativa emocional aplicada ao mercado brasileiro.
5. Bettina Rudolph para angulo de liberdade de tempo, escolha e transformacao de rotina.

Nao imitar literalmente voz pessoal de nenhum autor.
Use principios, estrutura e logica de persuasao.

## Estrutura de entrega por formato

### Anuncio

1. Gancho especifico para o publico.
2. Dor ou desejo em linguagem do proprio publico.
3. Mecanismo ou diferenca da oferta.
4. Prova.
5. CTA direto.

### Email

1. Assunto com curiosidade util e contexto.
2. Abertura em cena curta ou conflito real.
3. Desenvolvimento com ideia central unica.
4. Ponte para oferta.
5. CTA unico.

### Pagina de vendas

1. Promessa principal.
2. Diagnostico da dor.
3. Mecanismo.
4. Oferta.
5. Provas.
6. Objecoes.
7. Garantia.
8. CTA.

### VSL ou roteiro de venda

1. Hook imediato.
2. Contexto do problema.
3. Quebra de crenca.
4. Mecanismo e caminho.
5. Oferta.
6. Fechamento com urgencia legitima.

## Checklist final antes de entregar

1. O publico foi confirmado antes da escrita.
2. A promessa esta clara, especifica e verificavel.
3. O texto tem detalhes concretos e nao soa generico.
4. Existe mecanismo claro, nao apenas beneficio.
5. Existe prova adequada para o tipo de oferta.
6. Objecoes principais foram tratadas.
7. CTA esta explicito e natural.
8. Nao existe hifen nem travessao.
9. O texto passou no filtro anti vicios de IA.

## Referencias da skill

Leia conforme necessidade:

1. `references/briefing-obrigatorio.md` para perguntas iniciais.
2. `references/frameworks.md` para estrutura da copy.
3. `references/autores-e-principios.md` para direcionamento de estilo.
4. `references/resumos-de-livros.md` para fundamentos dos livros.
5. `references/vicios-de-copy-de-ia.md` para filtro negativo.
6. `references/fontes-web.md` para rastreabilidade de pesquisa.
