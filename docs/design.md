# Design System & UI/UX - EduAi Academy

Este documento oficializa todas as definições visuais, espaçamentos e mecânicas de componentes atuais da Landing Page, após a profunda refatoração baseada nos guias estritos de alta conversão (`@ui-ux-pro-max`).

## 1. Princípios Globais de UI

O visual adota um estilo **"Dark Mode Premium Editorial"**, fugindo da estética de "cursinho barato" e mirando em uma comunicação de "software de alto calibre".
- **Glassmorphism Premium (Estilo Emil Kowalski):** Cartões semi-transparentes (`rgba(20, 20, 20, 0.6)`) com desfoque traseiro pesado (`backdrop-filter: blur(16px)`), bordas translúcidas muito sutis (`rgba(255... 0.08)`) e leve sombra direcional escura para criar profundidade física na tela.
- **Micro-Noise:** Uma levíssima textura estática cobre a tela (fundo baseado em SVG fractals), removendo a artificialidade das cores digitais chapadas.
- **Interação sem Pulo de Layout (No Layout Shift):** Tudo responde a hovers sutis que movem (`translateY`) no máximo 2px com curvas beizer customizadas, sem reorganizar o restante do site.
- **Acessibilidade:** Uso de "Cursor pointer" implícito, transições polidas (200-300ms) e legibilidade em todas as condições de luz.

## 2. Cores e Tipografia

### 🎨 Paleta Restrita
- **Background Root:** `#080808` (Pitch black).
- **Surface Panels:** `#111111` / `rgba(20, 20, 20, 0.6)`
- **Linhas / Divisões:** Escala fina de `rgba(255, 255, 255, 0.1)`.
- **Textos:** Títulos brancos (`#fff`), textos principais em tom quebrado macio (`#f5f5f7`), textos acessórios em cinza mudo (`#a1a1a6`).
- **Marca / Destaque (Terracota):** Base primária `#da7756` (um laranja-abóbora muito elegante, fugindo do vermelho amador ou azul genérico). Com variações leves de saturação/luz (`#f0a084`).

### ✒️ Matriz Tipográfica
- **Títulos (h1, h2, h3):** `Space Grotesk` (Letra mais quadrada, brutalista na medida, transmite tecnologia moderna, weight: 600/700).
- **Condução Textual (`body` e `p`):** `Inter` (Font baseada em dados tipográficos perfeitos da Apple UI, sem erro de leitura em tela móvel).
- **Ritmo de Leitura (Crucial):** Todos os corpos de texto operam cravados com `line-height: 1.6`. Isso garante o "respiro vertical" perfeito entre as palavras no celular.

## 3. Engrenagem de Componentes 

### 🧊 Grids Auto-Amortizáveis (Masonry/Stretch Flex)
Abandonamos as grades duras onde os textos quebravam a assimetria visual. 
- Componentes como **`.step-card`**, **`.value-card`** e **`.fit-card`** agora são impiedosamente calculados. Eles recebem `display: flex; flex-direction: column; height: 100%`, enquanto os subtítulos possuem 0 de margem base e os parágrafos ganharam a ordem magna de `flex-grow: 1`. 
- **O Resultado:** Se um texto tem 3 linhas e o cartão colado a ele tem 15, o fundo preto fosco do cartão desce até igualar o outro lado milimetricamente.

### 🎭 Ponto de Convergência (Focus Tracking UI)
- A seção de pagamentos (**`.price-wrap`**) deixou de ser uma "caixa neutra". Modificamos para comportar um brilho nativo por trás (`radial-gradient` no `<article>` com variação de 10% da opacidade do Terracota). Isso direciona o olhar do leitor instantaneamente para a decisão gráfica: `12x R$20,37`. 

### 👤 Autoridade Editorial (`.about-grid`)
- O design de "Sobre Mim" abandonou o jeito corporativo antigo e adotou a classe de Portfólios Modernos: Coluna estreita ao lado para Foto (travada no formato `1:1` quadrado premium via `aspect-ratio` auto-cortada pelo `object-fit: cover`) acompanhada de uma Bio alinhada à direita; quando migra pro celular, a foto desliza polidamente para o topo (Stack).

### ✔️ Garantias & Prova-Social
- **`.micro-proof`**: Adota agora um Flex Flow para abraçar todo o espaço excedente, centrando e agrupando dinamicamente "selos de confiança" sem risco de overflow horizontal na caixa do container em telas muito pequenas (abaixo de 400 pixels). 

---
**Nota Técnica:** Modificadores responsivos no CSS (como o `@media max-width 940px` convertendo as grids para `1fr`) e botões animados vindos de "21st.dev" usando gradientes cónicos nativos rodam direto no GPU via CSS Variables interpoladas. Todo o esqueleto está blindado.
