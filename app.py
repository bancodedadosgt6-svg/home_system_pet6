import base64
from pathlib import Path

import streamlit as st
from streamlit_navigation_bar import st_navbar


# ============================================================
# CONFIGURAÇÕES GERAIS
# ============================================================

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
STYLE_PATH = BASE_DIR / "style.css"

LOGO_SVG_PATH = ASSETS_DIR / "logo.svg"
LOGO_PNG_PATH = ASSETS_DIR / "logo.png"
LOGO_UNB_PATH = ASSETS_DIR / "logounb.png"
FUNDO_PATH = ASSETS_DIR / "fundo.png"

SUBMETER_DADOS_URL = "https://coleta-dados-pet6.streamlit.app/"
SALA_SITUACAO_URL = "https://painel-dados-pet6.streamlit.app/"

SUBMETER_BUTTON_CANDIDATES = [
    ASSETS_DIR / "submeter_dados.png",
    ASSETS_DIR / "submeter_dados(1).png",
    ASSETS_DIR / "botao_submeter_dados.png",
]

SALA_BUTTON_CANDIDATES = [
    ASSETS_DIR / "sala_de_situacao.png",
    ASSETS_DIR / "sala_situacao.png",
    ASSETS_DIR / "botao_sala_de_situacao.png",
]

PAGE_ICON = str(LOGO_PNG_PATH) if LOGO_PNG_PATH.exists() else "🍎"

st.set_page_config(
    page_title="PET-Saúde GT-6",
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# MAPA DE PÁGINAS
# ============================================================

PAGE_HOME = "🏠 Início"
PAGE_SUBMETER = "📊 Submeter Dados"
PAGE_SALA = "📈 Sala de Situação Alimentar"

SLUG_TO_PAGE = {
    "inicio": PAGE_HOME,
    "submeter-dados": PAGE_SUBMETER,
    "sala-situacao": PAGE_SALA,
}

PAGE_TO_SLUG = {
    PAGE_HOME: "inicio",
    PAGE_SUBMETER: "submeter-dados",
    PAGE_SALA: "sala-situacao",
}


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def load_css() -> None:
    """
    Carrega o CSS externo do projeto, se existir.
    Evita quebrar o app caso o arquivo style.css não seja encontrado.
    """
    if STYLE_PATH.exists():
        with open(STYLE_PATH, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def file_to_base64(file_path: Path) -> str:
    """
    Converte um arquivo local para base64.
    Usado para imagens de fundo e botões-imagem.
    """
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")


def get_image_mime_type(image_path: Path) -> str:
    """
    Define o MIME type com base na extensão da imagem.
    """
    suffix = image_path.suffix.lower()

    if suffix in [".jpg", ".jpeg"]:
        return "image/jpeg"

    if suffix == ".webp":
        return "image/webp"

    if suffix == ".svg":
        return "image/svg+xml"

    return "image/png"


def apply_global_styles() -> None:
    """
    CSS global mínimo complementar.
    O estilo principal deve ficar no style.css.
    Aqui entram ajustes do fundo e dos botões-imagem.
    """

    if FUNDO_PATH.exists():
        fundo_base64 = file_to_base64(FUNDO_PATH)
        fundo_mime = get_image_mime_type(FUNDO_PATH)

        background_css = f"""
            .stApp {{
                background-image: url("data:{fundo_mime};base64,{fundo_base64}") !important;
                background-size: cover !important;
                background-repeat: no-repeat !important;
                background-position: center center !important;
                background-attachment: fixed !important;
                background-color: #ffffff !important;
            }}

            [data-testid="stAppViewContainer"] {{
                background: transparent !important;
            }}

            [data-testid="stHeader"] {{
                background: transparent !important;
            }}

            .main {{
                background: transparent !important;
            }}
        """
    else:
        background_css = """
            .stApp {
                background: #ffffff !important;
            }
        """

    st.markdown(
        f"""
        <style>
            {background_css}

            div[data-testid="stHeading"] {{
                text-align: center !important;
            }}

            div[data-testid="stHeading"] h1 {{
                width: 100% !important;
                text-align: center !important;
            }}

            .block-container {{
                padding-top: 2rem;
                background: transparent !important;
            }}

            .image-action-wrapper {{
                width: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 0.5rem;
                margin-bottom: 0.5rem;
            }}

            .image-action-button {{
                width: 100%;
                max-width: 560px;
                display: block;
                border-radius: 999px;
                text-decoration: none !important;
                transition: all 0.28s ease;
                filter: drop-shadow(0 10px 18px rgba(4, 145, 73, 0.18));
                cursor: pointer;
            }}

            .image-action-button-sala-situacao {{
                max-width: 320px !important;
            }}

            .image-action-button:hover {{
                transform: translateY(-5px) scale(1.025);
                filter:
                    drop-shadow(0 18px 28px rgba(4, 145, 73, 0.28))
                    drop-shadow(0 0 18px rgba(244, 210, 7, 0.35));
            }}

            .image-action-button:active {{
                transform: translateY(-1px) scale(0.99);
            }}

            .image-action-button img {{
                width: 100%;
                height: auto;
                display: block;
                border-radius: 999px;
                transition: all 0.28s ease;
            }}

            .image-action-button:hover img {{
                filter: brightness(1.04);
            }}

            .external-button-fallback {{
                width: 100%;
                min-height: 92px;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                font-size: 17px;
                font-weight: 750;
                border-radius: 24px;
                border: 1px solid rgba(4, 145, 73, 0.16);
                background: linear-gradient(135deg, #049149 0%, #5480a8 100%);
                color: #ffffff !important;
                box-shadow: 0 12px 32px rgba(84, 128, 168, 0.16);
                transition: all 0.25s ease;
                text-decoration: none !important;
            }}

            .external-button-fallback:hover {{
                background: linear-gradient(135deg, #f4d207 0%, #65c463 100%);
                color: #17301f !important;
                transform: translateY(-2px);
                border-color: rgba(244, 210, 7, 0.65);
                text-decoration: none !important;
            }}

            @media (max-width: 900px) {{
                .image-action-button {{
                    max-width: 460px;
                }}

                .image-action-button-sala-situacao {{
                    max-width: 300px !important;
                }}
            }}

            @media (max-width: 520px) {{
                .image-action-button {{
                    max-width: 340px;
                }}

                .image-action-button-sala-situacao {{
                    max-width: 280px !important;
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def safe_image(image_path: Path, width: int | None = None) -> None:
    """
    Renderiza imagem somente se o arquivo existir.
    Evita erro em deploy quando algum asset não subir corretamente.
    """
    if image_path.exists():
        st.image(str(image_path), width=width)


def find_existing_file(candidates: list[Path]) -> Path | None:
    """
    Retorna o primeiro arquivo existente dentro da lista de candidatos.
    """
    for file_path in candidates:
        if file_path.exists():
            return file_path

    return None


def image_to_base64(image_path: Path) -> str:
    """
    Converte uma imagem local para base64.
    Permite criar botão-imagem clicável com HTML.
    """
    return file_to_base64(image_path)


def get_current_page_from_query_params() -> str:
    """
    Lê a página atual a partir da URL.
    Exemplo:
    ?page=inicio
    """
    page_slug = st.query_params.get("page", "inicio")

    if isinstance(page_slug, list):
        page_slug = page_slug[0] if page_slug else "inicio"

    return SLUG_TO_PAGE.get(page_slug, PAGE_HOME)


def set_page(page_name: str) -> None:
    """
    Atualiza a página ativa via session_state e query params.
    """
    st.session_state["current_page"] = page_name
    st.query_params["page"] = PAGE_TO_SLUG.get(page_name, "inicio")
    st.rerun()


def render_external_image_button(
    image_path: Path | None,
    external_url: str,
    fallback_label: str,
    css_suffix: str,
) -> None:
    """
    Renderiza um botão baseado em imagem apontando para um sistema externo.
    Caso a imagem não exista, renderiza um botão HTML simples com o mesmo link.
    """
    if image_path and image_path.exists():
        image_base64 = image_to_base64(image_path)
        image_mime = get_image_mime_type(image_path)

        st.markdown(
            f"""
            <div class="image-action-wrapper">
                <a
                    class="image-action-button image-action-button-{css_suffix}"
                    href="{external_url}"
                    target="_blank"
                    rel="noopener noreferrer"
                    title="{fallback_label}"
                >
                    <img src="data:{image_mime};base64,{image_base64}" alt="{fallback_label}">
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="image-action-wrapper">
                <a
                    class="external-button-fallback"
                    href="{external_url}"
                    target="_blank"
                    rel="noopener noreferrer"
                    title="{fallback_label}"
                >
                    {fallback_label}
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# COMPONENTES
# ============================================================

def render_navbar() -> str:
    """
    Renderiza a navbar principal.
    Compatível com versões do streamlit-navigation-bar que não aceitam css.
    """

    pages = [
        PAGE_HOME,
        PAGE_SUBMETER,
        PAGE_SALA,
    ]

    if "current_page" not in st.session_state:
        st.session_state["current_page"] = get_current_page_from_query_params()

    styles = {
        "nav": {
            "background": "linear-gradient(90deg, #049149 0%, #5480a8 55%, #6d80ac 100%)",
            "height": "76px",
            "display": "flex",
            "align-items": "center",
            "justify-content": "center",
            "padding-left": "2rem",
            "padding-right": "2rem",
            "border-bottom": "4px solid #f4d207",
            "box-shadow": "0 8px 28px rgba(4, 145, 73, 0.22)",
        },
        "div": {
            "max-width": "1180px",
            "width": "100%",
            "display": "flex",
            "align-items": "center",
            "margin": "0 auto",
        },
        "ul": {
            "width": "100%",
            "display": "flex",
            "align-items": "center",
            "justify-content": "center",
            "gap": "28px",
        },
        "li": {
            "display": "flex",
            "align-items": "center",
        },
        "a": {
            "text-decoration": "none",
        },
        "span": {
            "color": "white",
            "font-size": "15.5px",
            "font-weight": "600",
            "padding": "12px 18px",
            "background": "rgba(255,255,255,0.10)",
            "border": "1px solid rgba(255,255,255,0.20)",
            "border-radius": "999px",
            "transition": "all 0.25s ease",
            "text-decoration": "none",
            "display": "inline-block",
        },
        "hover": {
            "color": "white",
            "background-color": "rgba(255,255,255,0.20)",
            "transform": "translateY(-1px)",
        },
        "active": {
            "color": "#17301f",
            "background": "#f4d207",
            "border-color": "#f4d207",
            "box-shadow": "0 8px 20px rgba(244, 210, 7, 0.26)",
            "transform": "translateY(-1px)",
            "letter-spacing": ".5px",
        },
        "img": {
            "height": "58px",
            "width": "auto",
            "object-fit": "contain",
        },
    }

    logo_path = str(LOGO_SVG_PATH) if LOGO_SVG_PATH.exists() else None

    try:
        selected_page = st_navbar(
            pages=pages,
            logo_path=logo_path,
            styles=styles,
            selected=st.session_state["current_page"],
        )
    except TypeError:
        selected_page = st_navbar(
            pages,
            logo_path=logo_path,
            styles=styles,
        )

    if selected_page:
        st.session_state["current_page"] = selected_page
        st.query_params["page"] = PAGE_TO_SLUG.get(selected_page, "inicio")

    return st.session_state["current_page"]


def render_footer() -> None:
    """
    Rodapé institucional.
    """
    st.markdown(
        """
        <hr style="margin-top: 50px;">

        <div class="footer">
            © 2026 PET-Saúde UNB • Todos os direitos reservados
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([3.1, 1, 3])

    with col2:
        safe_image(LOGO_UNB_PATH, width=60)


def render_team() -> None:
    """
    Renderiza a equipe do GT-6.
    Mantém os dados centralizados e mais fáceis de editar.
    """

    equipe = {
        "Gestão": [
            ("Patrícia de Fragas", "Coordenadora"),
            ("David Francisco", "Coordenador Adjunto"),
            ("Rafaela Garcia", "Gestora Júnior"),
            ("Raynara Ferreira", "Gestora Júnior"),
        ],
        "Equipe de Comunicação": [
            ("Eduarda Nascimento", "Comunicação e Design"),
            ("Yasmin Fagundes", "Comunicação e Design"),
        ],
        "Equipe de TI": [
            ("Cauã Nicolas", "TI"),
            ("Pedro Augusto", "TI"),
            ("Jean Carlos", "TI"),
        ],
        "Equipe de Pesquisa": [
            ("Débora Beatriz", "Pesquisa"),
            ("Kelly Cristina", "Pesquisa"),
            ("Taís Nazário", "Pesquisa"),
            ("Tainá Ribeiro", "Pesquisa"),
            ("Talitha de Souza", "Pesquisa"),
        ],
        "Preceptores": [
            ("Ana Paula Loschi", "Preceptora - UBS Jardins Mangueiral"),
            ("Leniela Afra", "Preceptora - DIRAPS"),
            ("Vanessa Araújo", "Preceptora - UBS Gama"),
        ],
    }

    st.divider()
    st.title("Equipe GT-6")
    st.header("Integrantes")

    for grupo, integrantes in equipe.items():
        st.subheader(grupo)

        for nome, funcao in integrantes:
            st.write(f"**{nome}** - {funcao}")


# ============================================================
# PÁGINAS
# ============================================================

def render_home() -> None:
    """
    Página inicial institucional.
    """

    submeter_button_path = find_existing_file(SUBMETER_BUTTON_CANDIDATES)
    sala_button_path = find_existing_file(SALA_BUTTON_CANDIDATES)

    col1, col2, col3 = st.columns([2, 1, 2])

    with col2:
        safe_image(LOGO_PNG_PATH, width=300)

    st.title("PET-Saúde")
    st.subheader("GT 6: Vigilância Alimentar e Nutricional")

    st.write(
        "O GT 6 foca na capacitação de profissionais da Atenção Básica para o uso "
        "adequado de marcadores alimentares no SUS, integrando a transformação "
        "digital à saúde pública."
    )

    st.divider()

    col1, col2, col3, col4 = st.columns([1.25, 1.6, 1.6, 1.25])

    with col2:
        render_external_image_button(
            image_path=submeter_button_path,
            external_url=SUBMETER_DADOS_URL,
            fallback_label="Submeter Dados",
            css_suffix="submeter-dados",
        )

    with col3:
        render_external_image_button(
            image_path=sala_button_path,
            external_url=SALA_SITUACAO_URL,
            fallback_label="Sala de Situação Saúde Alimentar",
            css_suffix="sala-situacao",
        )

    render_team()


def render_submeter_dados() -> None:
    """
    Página interna informativa para submissão de dados.
    O acesso principal é feito pelo botão externo da página inicial.
    """

    st.title("Submeter Dados")
    st.subheader("Sistema externo de coleta de dados")

    st.info(
        "A submissão de dados é realizada em um sistema externo dedicado."
    )

    st.markdown(
        f"""
        <div class="image-action-wrapper">
            <a
                class="external-button-fallback"
                href="{SUBMETER_DADOS_URL}"
                target="_blank"
                rel="noopener noreferrer"
            >
                Acessar sistema de Submissão de Dados
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sala_situacao() -> None:
    """
    Página interna informativa para a sala de situação.
    O acesso principal é feito pelo botão externo da página inicial.
    """

    st.title("Sala de Situação Alimentar")
    st.subheader("Painel externo de monitoramento")

    st.info(
        "A Sala de Situação de Saúde Alimentar é acessada em um painel externo dedicado."
    )

    st.markdown(
        f"""
        <div class="image-action-wrapper">
            <a
                class="external-button-fallback"
                href="{SALA_SITUACAO_URL}"
                target="_blank"
                rel="noopener noreferrer"
            >
                Acessar Sala de Situação Saúde Alimentar
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================

def main() -> None:
    load_css()
    apply_global_styles()

    current_page = render_navbar()

    if current_page == PAGE_HOME:
        render_home()

    elif current_page == PAGE_SUBMETER:
        render_submeter_dados()

    elif current_page == PAGE_SALA:
        render_sala_situacao()

    else:
        render_home()

    render_footer()


if __name__ == "__main__":
    main()