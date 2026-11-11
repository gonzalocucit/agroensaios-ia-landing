"""Landing page institucional do AgroEnsaios IA.

Etapa didática Streamlit: apresentação, colunas, cards, expanders, botões e tema.
Não abre a base, não executa auditoria, não cria relatórios e não treina modelos.
Indicadores do estudo T2 são um retrato documental, não métricas lidas ao vivo.
"""

from html import escape
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
CSS_PATH = ROOT / "landing_styles.css"

# Conteúdo institucional da plataforma. Não representa funcionalidades ativas.
MODULES = {
    "01 · Leitura da base local": {
        "status": "Integração futura",
        "description": (
            "A base será atualizada fora da aplicação. O sistema final deverá reconhecer "
            "novas safras, ensaios e alterações na fonte local, sem upload e sem "
            "modificar o arquivo original."
        ),
    },
    "02 · Auditoria e relatórios": {
        "status": "Núcleo científico existente · interface futura",
        "description": (
            "Reutilização das rotinas de conferência de dados, qualidade, cobertura "
            "e relatórios verificáveis já desenvolvidas no projeto. Alertas não "
            "serão convertidos automaticamente em exclusões ou correções."
        ),
    },
    "03 · Dashboard de ensaios": {
        "status": "Planejado",
        "description": (
            "Exploração por ano, ensaio, localidade, material e variável, com gráficos, "
            "comparações e indicadores agronômicos inspirados na experiência da "
            "aplicação Shiny."
        ),
    },
    "04 · Modelos de machine learning": {
        "status": "Pilotos existentes · interface futura",
        "description": (
            "Comparação entre referências estatísticas e métodos preditivos, com "
            "partições e métricas explícitas. Experimentos preliminares não são "
            "resultados finais nem modelos validados para uso comercial."
        ),
    },
    "05 · MLOps e rastreabilidade": {
        "status": "Registros existentes · integração futura",
        "description": (
            "Histórico de dados, parâmetros, versões, métricas e artefatos. "
            "A detecção de um novo ensaio não iniciará treinamento automaticamente."
        ),
    },
}

# Valores documentados no Canvas Científico Fase 1, referência fixa do estudo.
# NÃO inferir que estes números estejam atualizados na planilha local.
STUDY_SNAPSHOT = (
    ("2.843", "parcelas na base histórica"),
    ("5", "localidades T2 em 2026"),
    ("90", "materiais avaliados no núcleo T2"),
    ("700", "rendimentos observados no núcleo T2"),
)

STUDY_TEAM = (
    "Allison Samara Zabala Ramos",
    "Gonzalo Alejo Cucit",
    "Samara Dhyulle Magalhães Barros",
)


def _add_styles() -> None:
    """Aplica CSS local. Nenhuma dependência de serviços externos."""
    if CSS_PATH.is_file():
        st.markdown(f"<style>{CSS_PATH.read_text(encoding='utf-8')}</style>",
                    unsafe_allow_html=True)


def _eyebrow(index: str, label: str) -> None:
    st.markdown(
        f'<p class="ag-eyebrow"><span>{escape(index)}</span> {escape(label)}</p>',
        unsafe_allow_html=True,
    )


def _card(number: str, title: str, description: str, category: str) -> None:
    st.markdown(
        '<article class="ag-feature">'
        f'<div class="ag-feature-head"><span>{escape(number)}</span>'
        f'<small>{escape(category)}</small></div>'
        f'<h3>{escape(title)}</h3><p>{escape(description)}</p></article>',
        unsafe_allow_html=True,
    )


def _trial_panel() -> None:
    """Esquema técnico CSS de parcelas. Não representa observações."""
    palette = ("exp", "exp", "check", "exp", "exp", "missing", "exp", "check")
    cells = []
    for row in range(6):
        for col in range(8):
            category = palette[(col + row * 3) % len(palette)]
            cells.append(f'<span class="ag-plot-cell ag-plot-{category}" aria-hidden="true"></span>')
    markup = (
        '<div class="ag-tech-panel" role="img" aria-label="Esquema ilustrativo de '
        'uma malha de parcelas experimentais, com legendas de materiais e dados ausentes">'
        '<div class="ag-panel-head"><div><span class="ag-mini-kicker">VISUALIZAÇÃO TÉCNICA</span>'
        '<strong>Rede de ensaios</strong></div><span class="ag-panel-mark">G × E</span></div>'
        '<div class="ag-panel-rule"></div>'
        '<div class="ag-panel-bar"><span>PARCELAS · VISTA ESQUEMÁTICA</span><span>06 × 08</span></div>'
        '<div class="ag-plot-wrap"><div class="ag-axis ag-axis-y">BLOCOS</div>'
        '<div class="ag-plot-grid">' + ''.join(cells) + '</div></div>'
        '<div class="ag-plot-legend">'
        '<span><i class="ag-dot ag-dot-exp"></i>Experimental</span>'
        '<span><i class="ag-dot ag-dot-check"></i>Testemunha</span>'
        '<span><i class="ag-dot ag-dot-missing"></i>Sem dado</span>'
        '</div>'
        '<div class="ag-panel-data"><span>GENÓTIPO</span><span>AMBIENTE</span>'
        '<span>RENDIMENTO</span><span>VALIDAÇÃO</span></div>'
        '</div>'
    )
    st.markdown(markup, unsafe_allow_html=True)


def _snapshot() -> None:
    columns = st.columns(4, gap="small")
    for col, (value, title) in zip(columns, STUDY_SNAPSHOT):
        with col:
            st.markdown(
                '<div class="ag-stat">'
                f'<strong>{escape(value)}</strong><span>{escape(title)}</span></div>',
                unsafe_allow_html=True,
            )


def _step(number: str, title: str, copy: str) -> None:
    st.markdown(
        '<div class="ag-step">'
        f'<span>{escape(number)}</span><strong>{escape(title)}</strong>'
        f'<p>{escape(copy)}</p></div>',
        unsafe_allow_html=True,
    )


def main() -> None:
    """Exibe a landing sem chamar qualquer módulo científico."""
    st.set_page_config(
        page_title="AgroEnsaios IA | Ciência de Dados & Melhoramento",
        page_icon="🌱",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={"About": "AgroEnsaios IA · Apresentação da plataforma em desenvolvimento."},
    )
    _add_styles()

    st.markdown(
        '<header class="ag-topline">'
        '<span class="ag-brand"><span class="ag-brand-symbol">✦</span> AGROENSAIOS <b>IA</b></span>'
        '<span class="ag-topstate">PLATAFORMA CIENTÍFICA <i></i> APRESENTAÇÃO PÚBLICA</span>'
        '</header>',
        unsafe_allow_html=True,
    )

    # 01 · Hero: título à esquerda e visualização técnica ilustrativa à direita.
    with st.container(border=True):
        hero, visual = st.columns([1.1, 1], gap="large", vertical_alignment="center")
        with hero:
            st.markdown(
                '<p class="ag-kicker">MELHORAMENTO GENÉTICO <span> / </span> CIÊNCIA DE DADOS</p>'
                '<h1 class="ag-hero-title">Do ensaio de campo à '
                '<span>decisão baseada em evidências.</span></h1>'
                '<p class="ag-hero-copy">Uma plataforma para integrar qualidade '
                'de dados, análise de ensaios multiambientais e inteligência '
                'artificial — com rigor estatístico e rastreabilidade.</p>'
                '<div class="ag-chip-row"><span>PYTHON</span><span>STREAMLIT</span>'
                '<span>MELHORAMENTO</span><span>ML / MLOPS</span></div>',
                unsafe_allow_html=True,
            )
            if st.button("Conhecer a proposta", type="primary", key="hero_cta"):
                st.session_state["mostrar_escopo"] = not st.session_state.get(
                    "mostrar_escopo", False
                )
            if st.session_state.get("mostrar_escopo", False):
                st.info(
                    "Esta entrega apresenta a plataforma e o estudo de caso. "
                    "**Não executa** auditoria, leitura de planilhas, dashboards ou "
                    "treinamentos. Essas integrações virão nas próximas etapas."
                )
        with visual:
            _trial_panel()

    # 02 · Por que existe a plataforma.
    _eyebrow("01", "PROPÓSITO")
    st.markdown("## Uma plataforma. Três compromissos.")
    st.markdown(
        '<p class="ag-section-lead">Organizar a informação experimental para '
        'gerar comparações mais confiáveis e decisões transparentes.</p>',
        unsafe_allow_html=True,
    )
    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        _card("01", "Integridade dos dados", "Auditoria, consistência e histórico "
              "de decisões, sem correções silenciosas da fonte.", "QUALIDADE")
    with col2:
        _card("02", "Análise multiambiental", "Exploração de materiais, locais e "
              "cobertura para apoiar a interpretação agronômica.", "ESTATÍSTICA")
    with col3:
        _card("03", "Modelos reproduzíveis", "Comparações honestas de métodos, "
              "validação rigorosa e rastreabilidade.", "IA / MLOPS")

    # 03 · Estudo científico ilustrativo da plataforma.
    st.divider()
    _eyebrow("02", "ESTUDO DE CASO")
    study_main, study_note = st.columns([1.8, 1], gap="large")
    with study_main:
        st.markdown("## Rede T2 de sorgo granífero · 2026")
        st.markdown(
            "Na rede brasileira de ensaios multiambientais, a cobertura desigual de "
            "rendimentos pode comprometer a comparação direta de materiais. "
            "O estudo investiga o valor adicional de métodos preditivos frente a "
            "referências estatísticas, sem pressupor superioridade da IA."
        )
    with study_note:
        st.markdown(
            '<div class="ag-case-aside"><span>PERGUNTA DE PESQUISA</span>'
            '<p>Quando os métodos de aprendizado de máquina melhoram a predição '
            'do rendimento frente aos modelos estatísticos em uma rede incompleta?</p>'
            '</div>',
            unsafe_allow_html=True,
        )
    _snapshot()

    # 04 · Etapas: fluxo pretendido, não pipeline operacional nesta página.
    st.divider()
    _eyebrow("03", "METODOLOGIA")
    st.markdown("## Do dado bruto à interpretação agronômica")
    st.markdown(
        '<p class="ag-section-lead">Etapas conceituais da plataforma final. '
        'Cada análise deverá preservar sua origem e suas condições de validade.</p>',
        unsafe_allow_html=True,
    )
    steps = st.columns(4, gap="small")
    for col, args in zip(steps, (
        ("01", "Ler", "Reconhecer a fonte local e as novas campanhas."),
        ("02", "Auditar", "Conferir esquema, qualidade e cobertura."),
        ("03", "Analisar", "Explorar ensaios e comparações entre ambientes."),
        ("04", "Validar", "Avaliar modelos e registrar resultados reproduzíveis."),
    )):
        with col:
            _step(*args)

    # 05 · Módulos apresentados com expanders do tutorial.
    st.divider()
    _eyebrow("04", "ARQUITETURA PREVISTA")
    st.markdown("## Módulos da plataforma")
    st.caption("Escopo e estágio real de integração. Estes módulos ainda não são páginas operacionais.")
    for name, item in MODULES.items():
        with st.expander(name):
            st.caption(item["status"])
            st.write(item["description"])

    # 06 · Equipo del canvas, solamente nombres y ninguna atribución inventada.
    st.divider()
    _eyebrow("05", "EQUIPE DO ESTUDO")
    st.markdown("## Pesquisa construída em colaboração")
    members = st.columns(3, gap="medium")
    for col, name in zip(members, STUDY_TEAM):
        with col:
            st.markdown(
                f'<div class="ag-person"><strong>{escape(name)}</strong></div>',
                unsafe_allow_html=True,
            )

    # 07 · CTA real: apenas revela o planejamento.
    st.markdown(
        '<div class="ag-bottom-title">Uma base visual sólida para uma plataforma em evolução</div>'
        '<p class="ag-bottom-copy">Nesta etapa, aperfeiçoamos a apresentação da plataforma. '
        'A integração dos dados, análises e modelos acontecerá de forma controlada, '
        'preservando os arquivos científicos existentes.</p>',
        unsafe_allow_html=True,
    )
    _, centered, _ = st.columns([1, 1.2, 1])
    with centered:
        if st.button("Ver os próximos passos", key="final_cta", use_container_width=True):
            st.session_state["mostrar_proximos"] = not st.session_state.get(
                "mostrar_proximos", False
            )
    if st.session_state.get("mostrar_proximos", False):
        st.info(
            "Próximas integrações: **leitura automática da base local → auditoria "
            "e relatórios → dashboards de ensaios → ML → MLOps**. "
            "A atualização externa da planilha não deverá iniciar treinamento."
        )
    st.markdown(
        '<footer class="ag-footer"><span>© 2026 AGROENSAIOS <b>IA</b> · '
        'Ciência de dados para o melhoramento genético</span>'
        '<span>Etapa didática · Streamlit + Python · Apresentação pública</span></footer>',
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
