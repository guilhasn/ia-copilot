# -*- coding: utf-8 -*-
"""
Gera o site estático em materiais/ (hub ia-copilot) a partir dos materiais das sessões.

- index.html: uma secção por sessão, cartões de download agrupados por pasta
  (percorre as pastas reais — links sempre corretos e URL-encoded).
- Páginas HTML de leitura para o Enunciado e as Questões/Prompts de cada
  sessão (conversão DOCX -> HTML com mammoth), com download do .docx ao lado.

Uso:  python materiais/_gerar_site.py
"""
import html
import os
import re
import urllib.parse

import mammoth

RAIZ = os.path.dirname(os.path.abspath(__file__))
DOCS = RAIZ  # o script vive dentro de materiais/

# ---------------------------------------------------------------- conteúdo

CURSO = "IA Generativa e Copilot Microsoft 365"
SUBTITULO = "Formação ANFUP · Materiais para os formandos"
NOTA_FICTICIO = (
    "Todos os dados destes materiais são fictícios e foram criados "
    "exclusivamente para fins de formação. Nomes, entidades, avaliações e "
    "deliberações são inventados; qualquer semelhança com pessoas ou "
    "instituições reais é coincidência."
)

SESSOES = [
    {
        "slug": "sessao-9",
        "numero": "9",
        "acento": "#96520f",
        "acento_suave": "#f3e3cf",
        "titulo": "Análise de fichas SIADAP",
        "descricao": (
            "No papel de técnicos superiores da DARH do fictício Município de "
            "Vila Nova do Alva, os grupos analisam com o Copilot as 20 fichas "
            "de avaliação SIADAP 3 remetidas pelas unidades orgânicas: "
            "completude, coerência entre resultados e classificações, e "
            "igualdade de critérios — produzindo o relatório executivo e as "
            "comunicações de suporte à decisão."
        ),
        "leitura": [
            ("enunciado.html", "Enunciado do caso prático"),
            ("questoes.html", "Questões para resolver com o Copilot"),
            ("prompts.html", "Prompts prontos a usar"),
        ],
    },
    {
        "slug": "sessao-10",
        "numero": "10",
        "acento": "#155e68",
        "acento_suave": "#d8e8e6",
        "titulo": "Da convocatória à ata",
        "descricao": (
            "Como equipa de apoio ao secretariado do Conselho Científico da "
            "fictícia Universidade de Vale Verde, os grupos percorrem o ciclo "
            "completo de uma reunião de órgão: triagem de pedidos e "
            "convocatória, transcrição Teams, minuta de ata fiel, sigilo e "
            "anonimização, registo auditável de deliberações e as "
            "comunicações pós-reunião."
        ),
        "leitura": [
            ("enunciado.html", "Enunciado do caso prático"),
            ("questoes.html", "Questões e prompts por fase"),
        ],
    },
]

# páginas de leitura: (sessão, ficheiro html, docx de origem relativo à sessão, título)
PAGINAS_LEITURA = [
    ("sessao-9", "enunciado.html",
     "01_Enunciado/Enunciado_Caso_Pratico_SIADAP_Copilot.docx",
     "Enunciado — Análise de fichas SIADAP com o Copilot"),
    ("sessao-9", "questoes.html",
     "01_Enunciado/Questoes_para_Resolver_com_Copilot.docx",
     "Questões para resolver com o Copilot"),
    ("sessao-9", "prompts.html",
     "05_Prompts_Copilot/Prompts_Prontos_a_Usar_Copilot_M365.docx",
     "Prompts prontos a usar — Copilot Microsoft 365"),
    ("sessao-10", "enunciado.html",
     "01_Enunciado/Enunciado_Sessao10_Da_Convocatoria_a_Ata.docx",
     "Enunciado — Da convocatória à ata"),
    ("sessao-10", "questoes.html",
     "05_Prompts_Copilot/Questoes_e_Prompts_Copilot_Sessao10.docx",
     "Questões e prompts — Sessão 10"),
]

NOMES_PASTAS = {
    "01_Enunciado": "Enunciado",
    "02_Fichas_Avaliacao": "Fichas de avaliação (20 trabalhadores)",
    "02_Transcricao_Reuniao": "Transcrição da reunião",
    "03_Dados_Apoio": "Dados de apoio",
    "05_Prompts_Copilot": "Prompts Copilot",
}

# ---------------------------------------------------------------- aparência

CSS = """
:root{
  --papel:#f7f3ec; --papel-2:#efe9dd; --tinta:#23271f; --cinza:#6d6a5c;
  --filete:#d8d0bf; --acc:#3d5342;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0; background:var(--papel); color:var(--tinta);
  font-family:"Atkinson Hyperlegible",system-ui,sans-serif;
  font-size:17px; line-height:1.6;
  background-image:radial-gradient(rgba(35,39,31,.035) 1px, transparent 1px);
  background-size:22px 22px;
}
.pagina{max-width:1060px;margin:0 auto;padding:0 24px 96px}
a{color:inherit}

/* cabeçalho editorial */
.masthead{padding:44px 0 28px;border-bottom:3px double var(--filete)}
.masthead .antetitulo{
  font-size:.78rem;letter-spacing:.22em;text-transform:uppercase;color:var(--cinza);
  display:flex;align-items:center;gap:14px;margin-bottom:18px;
}
.masthead .antetitulo::before,.masthead .antetitulo::after{
  content:"";height:1px;background:var(--filete);flex:0 0 42px;
}
h1.curso{
  font-family:"Fraunces",serif;font-optical-sizing:auto;font-weight:640;
  font-size:clamp(2rem,5.4vw,3.4rem);line-height:1.06;margin:0 0 10px;
  letter-spacing:-.015em;
}
.masthead .sub{color:var(--cinza);font-size:1.02rem;margin:0}

.nota-ficticio{
  margin:30px 0 0;padding:14px 18px 14px 22px;position:relative;
  background:var(--papel-2);border:1px solid var(--filete);font-size:.92rem;
  color:#4c4a3e;
}
.nota-ficticio::before{
  content:"";position:absolute;left:-1px;top:-1px;bottom:-1px;width:5px;
  background:repeating-linear-gradient(-45deg,#b3a684 0 6px,var(--papel) 6px 12px);
}
.nota-ficticio strong{color:var(--tinta)}

/* menu de sessões (sticky) */
nav.menu-sessoes{
  position:sticky;top:0;z-index:20;display:flex;flex-wrap:wrap;gap:10px;
  padding:14px 0;margin-top:6px;background:var(--papel);
  border-bottom:1px solid var(--filete);
}
nav.menu-sessoes .rotulo-menu{
  align-self:center;font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--cinza);font-weight:700;margin-right:6px;
}
nav.menu-sessoes a{
  display:inline-flex;align-items:baseline;gap:9px;text-decoration:none;
  border:1.5px solid var(--acc-m,#3d5342);color:var(--acc-m,#3d5342);
  padding:8px 16px;border-radius:999px;font-weight:700;font-size:.92rem;
  transition:background .15s,color .15s,transform .15s;
}
nav.menu-sessoes a .num{
  font-family:"Fraunces",serif;font-weight:640;font-size:1.05rem;line-height:1;
}
nav.menu-sessoes a:hover{transform:translateY(-1px)}
nav.menu-sessoes a.ativo{background:var(--acc-m,#3d5342);color:var(--papel)}
body.js-tabs .sessao{display:none}
body.js-tabs .sessao.visivel{display:block;margin-top:34px}

/* secções de sessão */
.sessao{margin-top:64px;position:relative}
.sessao-cab{
  display:grid;grid-template-columns:auto 1fr;gap:6px 26px;align-items:baseline;
  border-bottom:1px solid var(--filete);padding-bottom:22px;
}
.sessao-num{
  grid-row:1/span 2;font-family:"Fraunces",serif;font-weight:300;
  font-size:clamp(4.6rem,10vw,7rem);line-height:.82;color:transparent;
  -webkit-text-stroke:1.6px var(--acc);letter-spacing:-.04em;
  transform:translateY(6px);
}
.sessao h2{
  font-family:"Fraunces",serif;font-weight:600;letter-spacing:-.01em;
  font-size:clamp(1.5rem,3.4vw,2.2rem);margin:0;
}
.sessao h2 .kicker{
  display:block;font-family:"Atkinson Hyperlegible",sans-serif;font-weight:700;
  font-size:.74rem;letter-spacing:.2em;text-transform:uppercase;color:var(--acc);
  margin-bottom:8px;
}
.sessao .descricao{margin:8px 0 0;max-width:62ch;color:#3d4136}

.leitura{display:flex;flex-wrap:wrap;gap:10px;margin:22px 0 8px}
.leitura a{
  display:inline-flex;align-items:center;gap:9px;text-decoration:none;
  border:1.5px solid var(--acc);color:var(--acc);background:transparent;
  padding:9px 16px;font-weight:700;font-size:.92rem;border-radius:2px;
  transition:background .15s,color .15s,transform .15s;
}
.leitura a::before{content:"❧";font-size:1rem}
.leitura a:hover{background:var(--acc);color:var(--papel);transform:translateY(-1px)}

.grupos{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:26px;margin-top:26px}
.grupo{border:1px solid var(--filete);background:rgba(255,255,255,.5);padding:18px 20px 14px}
.grupo.largo{grid-column:1/-1}
.grupo h3{
  font-size:.76rem;letter-spacing:.18em;text-transform:uppercase;color:var(--cinza);
  margin:0 0 12px;display:flex;align-items:center;gap:10px;font-weight:700;
}
.grupo h3::after{content:"";flex:1;height:1px;background:var(--filete)}
ul.ficheiros{list-style:none;margin:0;padding:0}
ul.ficheiros li{border-top:1px dashed var(--filete)}
ul.ficheiros li:first-child{border-top:0}
ul.ficheiros a{
  display:flex;align-items:center;gap:11px;padding:8px 4px;text-decoration:none;
  transition:background .12s;
}
ul.ficheiros a:hover{background:var(--papel-2)}
ul.ficheiros a:hover .nome{text-decoration:underline;text-underline-offset:3px}
.nome{flex:1;font-size:.95rem}
.tam{color:var(--cinza);font-size:.8rem;white-space:nowrap}
.seta{color:var(--acc);font-weight:700}
.badge{
  flex:0 0 auto;font-size:.62rem;font-weight:700;letter-spacing:.08em;
  padding:3px 7px;border-radius:2px;color:#fff;min-width:44px;text-align:center;
}
.badge.docx{background:#2b579a}.badge.xlsx{background:#217346}
.badge.vtt{background:#8a4baf}.badge.outro{background:#666}

.fichas-grelha ul.ficheiros{
  display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:2px 22px;
}
.fichas-grelha ul.ficheiros li{border-top:1px dashed var(--filete)!important}

/* páginas de documento */
.doc-topo{
  display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between;
  padding:18px 0;border-bottom:1px solid var(--filete);font-size:.9rem;
}
.doc-topo .voltar{text-decoration:none;color:var(--cinza);letter-spacing:.06em;text-transform:uppercase;font-size:.76rem;font-weight:700}
.doc-topo .voltar:hover{color:var(--acc)}
.btn-docx{
  display:inline-flex;align-items:center;gap:8px;text-decoration:none;font-weight:700;
  background:var(--acc);color:var(--papel);padding:9px 16px;border-radius:2px;font-size:.88rem;
  transition:transform .15s,box-shadow .15s;
}
.btn-docx:hover{transform:translateY(-1px);box-shadow:0 3px 10px rgba(0,0,0,.18)}
article.doc{max-width:74ch;margin:0 auto;padding-top:14px}
article.doc h1{
  font-family:"Fraunces",serif;font-weight:640;letter-spacing:-.015em;
  font-size:clamp(1.7rem,4vw,2.5rem);line-height:1.12;margin:26px 0 6px;
}
article.doc .sessao-tag{
  font-size:.74rem;letter-spacing:.2em;text-transform:uppercase;color:var(--acc);
  font-weight:700;margin-top:30px;
}
article.doc h2{
  font-family:"Fraunces",serif;font-weight:600;font-size:1.45rem;margin:2.1em 0 .5em;
  padding-top:.9em;border-top:1px solid var(--filete);
}
article.doc h3{font-family:"Fraunces",serif;font-weight:600;font-size:1.15rem;margin:1.6em 0 .4em}
article.doc p{margin:.7em 0}
article.doc li{margin:.35em 0}
article.doc table{border-collapse:collapse;width:100%;margin:1.2em 0;font-size:.93rem}
article.doc td,article.doc th{border:1px solid var(--filete);padding:8px 12px;vertical-align:top;text-align:left}
article.doc tr:first-child td{background:var(--papel-2);font-weight:700}
article.doc td p{margin:0}
article.doc em{color:#50503f}
article.doc pre,article.doc code{white-space:pre-wrap;word-break:break-word}
.doc-rodape{margin-top:56px;padding-top:18px;border-top:3px double var(--filete);text-align:center}

footer.rodape{
  margin-top:80px;padding-top:22px;border-top:3px double var(--filete);
  color:var(--cinza);font-size:.85rem;display:flex;flex-wrap:wrap;gap:8px 24px;
  justify-content:space-between;
}
@media (max-width:640px){
  .sessao-cab{grid-template-columns:1fr}
  .sessao-num{grid-row:auto;transform:none;margin-bottom:4px}
}
@media print{
  body{background:#fff}
  .leitura,.btn-docx,.doc-topo .voltar{display:none}
}
"""

FONTES = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Fraunces:opsz,wght@9..144,300;9..144,600;9..144,640&display=swap" rel="stylesheet">'
)

FAVICON = (
    '<link rel="icon" href="data:image/svg+xml,'
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
    "%3Crect width='32' height='32' fill='%23f7f3ec'/%3E"
    "%3Ctext x='16' y='23' font-family='Georgia' font-size='19' font-weight='bold' text-anchor='middle' fill='%23155e68'%3EAI%3C/text%3E%3C/svg%3E\">"
)


def esqueleto(titulo, corpo, descricao):
    return f"""<!DOCTYPE html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{html.escape(descricao)}">
<title>{html.escape(titulo)}</title>
{FONTES}
{FAVICON}
<style>{CSS}</style>
</head>
<body>
<div class="pagina">
{corpo}
</div>
</body>
</html>
"""


def kb(n):
    return f"{max(1, round(n / 1024))} KB"


def badge(nome):
    ext = os.path.splitext(nome)[1].lower().lstrip(".")
    classe = ext if ext in ("docx", "xlsx", "vtt") else "outro"
    return f'<span class="badge {classe}">{ext.upper()}</span>'


def rotulo(nome):
    """Nome de ficheiro -> rótulo legível."""
    base = os.path.splitext(nome)[0]
    m = re.match(r"Ficha_(\d+)_(.+)_([A-Z]+)$", base)
    if m:
        pessoa = m.group(2).replace("_", " ")
        return f"Ficha {m.group(1)} — {pessoa} ({m.group(3)})"
    return base.replace("_", " ")


def linha_ficheiro(caminho_rel, nome, tamanho):
    href = urllib.parse.quote(caminho_rel)
    return (
        f'<li><a href="{href}" download>{badge(nome)}'
        f'<span class="nome">{html.escape(rotulo(nome))}</span>'
        f'<span class="tam">{kb(tamanho)}</span><span class="seta">&#8595;</span></a></li>'
    )


def grupo_html(slug, pasta, base_dir):
    caminho = os.path.join(base_dir, pasta)
    itens = sorted(os.listdir(caminho))
    linhas = []
    for nome in itens:
        completo = os.path.join(caminho, nome)
        if os.path.isfile(completo):
            linhas.append(linha_ficheiro(f"{slug}/{pasta}/{nome}", nome, os.path.getsize(completo)))
    extra = ""
    if len(linhas) > 6:
        extra = " largo fichas-grelha"
    titulo = NOMES_PASTAS.get(pasta, pasta.replace("_", " "))
    return (
        f'<div class="grupo{extra}"><h3>{html.escape(titulo)}</h3>'
        f'<ul class="ficheiros">{"".join(linhas)}</ul></div>'
    )


def seccao_sessao(s):
    base_dir = os.path.join(DOCS, s["slug"])
    pastas = sorted(
        d for d in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, d))
    )
    grupos = "".join(grupo_html(s["slug"], p, base_dir) for p in pastas)
    leitura = "".join(
        f'<a href="{s["slug"]}/{f}">{html.escape(t)}</a>' for f, t in s["leitura"]
    )
    return f"""
<section class="sessao" id="{s['slug']}" style="--acc:{s['acento']};--papel-2:{s['acento_suave']}">
  <div class="sessao-cab">
    <div class="sessao-num" aria-hidden="true">{s['numero']}</div>
    <h2><span class="kicker">Sessão {s['numero']} · Caso prático</span>{html.escape(s['titulo'])}</h2>
    <p class="descricao">{html.escape(s['descricao'])}</p>
  </div>
  <div class="leitura">{leitura}</div>
  <div class="grupos">{grupos}</div>
</section>"""


def gerar_index():
    seccoes = "".join(seccao_sessao(s) for s in SESSOES)
    itens_menu = "".join(
        f'<a href="#{s["slug"]}" data-slug="{s["slug"]}" style="--acc-m:{s["acento"]}">'
        f'<span class="num">{s["numero"]}</span> {html.escape(s["titulo"])}</a>'
        for s in SESSOES
    )
    menu = (
        '<nav class="menu-sessoes" aria-label="Sessões">'
        '<span class="rotulo-menu">Sessões</span>'
        f"{itens_menu}</nav>"
    )
    # comutação de sessões: mostra uma de cada vez; sem JS, ficam todas
    # visíveis e o menu funciona como âncoras. O hash (#sessao-10) continua
    # a servir de link directo a partir das páginas das sessões do hub.
    script = """
<script>
(function () {
  var slugs = Array.prototype.map.call(
    document.querySelectorAll("nav.menu-sessoes a"),
    function (a) { return a.getAttribute("data-slug"); }
  );
  if (!slugs.length) { return; }
  document.body.classList.add("js-tabs");
  function ativar(slug) {
    if (slugs.indexOf(slug) === -1) { slug = slugs[0]; }
    document.querySelectorAll(".sessao").forEach(function (s) {
      s.classList.toggle("visivel", s.id === slug);
    });
    document.querySelectorAll("nav.menu-sessoes a").forEach(function (a) {
      a.classList.toggle("ativo", a.getAttribute("data-slug") === slug);
    });
  }
  window.addEventListener("hashchange", function () {
    ativar(location.hash.replace("#", ""));
    window.scrollTo(0, 0);
  });
  ativar(location.hash.replace("#", ""));
})();
</script>"""
    corpo = f"""
<header class="masthead">
  <p class="antetitulo">Formação ANFUP · 2026</p>
  <h1 class="curso">{html.escape(CURSO)}</h1>
  <p class="sub">{html.escape(SUBTITULO)}</p>
  <p class="nota-ficticio"><strong>Nota:</strong> {html.escape(NOTA_FICTICIO)}</p>
</header>
{menu}
{seccoes}
<footer class="rodape">
  <span>{html.escape(CURSO)} — Formação ANFUP</span>
  <span>Materiais de formação · dados fictícios</span>
</footer>
{script}"""
    with open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8") as f:
        f.write(esqueleto(
            f"{CURSO} — Formação ANFUP",
            corpo,
            "Materiais de formação para os formandos: enunciados, dados de apoio e prompts das sessões práticas.",
        ))
    print("index.html gerado")


def gerar_paginas_leitura():
    for slug, saida, docx_rel, titulo in PAGINAS_LEITURA:
        origem = os.path.join(DOCS, slug, docx_rel.replace("/", os.sep))
        with open(origem, "rb") as f:
            resultado = mammoth.convert_to_html(f)
        for aviso in resultado.messages:
            print(f"  aviso mammoth ({saida}): {aviso}")
        conteudo = resultado.value
        # o título da página é o h1; despromover os títulos do documento
        conteudo = conteudo.replace("<h2", "<h3").replace("</h2>", "</h3>")
        conteudo = conteudo.replace("<h1", "<h2").replace("</h1>", "</h2>")
        sessao = next(s for s in SESSOES if s["slug"] == slug)
        href_docx = urllib.parse.quote(docx_rel)
        nome_docx = os.path.basename(docx_rel)
        corpo = f"""
<div class="doc-topo" style="--acc:{sessao['acento']}">
  <a class="voltar" href="../index.html#{slug}">&#8592; Todos os materiais</a>
  <a class="btn-docx" href="{href_docx}" download>&#8595; Descarregar {html.escape(nome_docx)}</a>
</div>
<article class="doc" style="--acc:{sessao['acento']};--papel-2:{sessao['acento_suave']}">
  <p class="sessao-tag">Sessão {sessao['numero']} · {html.escape(sessao['titulo'])}</p>
  <h1>{html.escape(titulo)}</h1>
  {conteudo}
  <div class="doc-rodape">
    <a class="btn-docx" href="{href_docx}" download>&#8595; Descarregar {html.escape(nome_docx)}</a>
  </div>
</article>
<footer class="rodape">
  <span>{html.escape(CURSO)} — Formação ANFUP</span>
  <span>Materiais de formação · dados fictícios</span>
</footer>"""
        destino = os.path.join(DOCS, slug, saida)
        with open(destino, "w", encoding="utf-8") as f:
            f.write(esqueleto(
                f"{titulo} · Sessão {sessao['numero']} — Formação ANFUP",
                corpo,
                f"Versão de leitura de {nome_docx} (o download do documento Word continua disponível).",
            ))
        print(f"{slug}/{saida} gerado")


if __name__ == "__main__":
    gerar_paginas_leitura()
    gerar_index()
