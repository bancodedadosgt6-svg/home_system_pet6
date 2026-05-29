import base64
from pathlib import Path

import streamlit as st


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
    page_title="Sistema de Saúde Alimentar e Nutricional - GT6",
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def load_css() -> None:
    """
    Carrega o CSS externo do projeto, se existir.
    """
    if STYLE_PATH.exists():
        with open(STYLE_PATH, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def file_to_base64(file_path: Path) -> str:
    """
    Converte um arquivo local para base64.
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


def safe_image(image_path: Path, width: int | None = None) -> None:
    """
    Renderiza imagem somente se o arquivo existir.
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


def get_header_logo_path() -> Path | None:
    """
    Prioriza logo SVG para o cabeçalho.
    Caso não exista, usa PNG.
    """
    if LOGO_SVG_PATH.exists():
        return LOGO_SVG_PATH

    if LOGO_PNG_PATH.exists():
        return LOGO_PNG_PATH

    return None


def apply_global_styles() -> None:
    """
    CSS global do sistema:
    - fundo com assets/fundo.png;
    - cabeçalho institucional;
    - botões-imagem;
    - ajustes de clique.
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
                pointer-events: none !important;
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

            .block-container {{
                padding-top: 1.4rem !important;
                background: transparent !important;
                max-width: 1180px !important;
            }}

            div[data-testid="stHeading"] {{
                text-align: center !important;
            }}

            div[data-testid="stHeading"] h1 {{
                width: 100% !important;
                text-align: center !important;
            }}

            .app-header {{
                width: 100%;
                min-height: 78px;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 22px;
                padding: 12px 28px;
                margin: 0 auto 2.3rem auto;
                border-radius: 0 0 26px 26px;
                background: linear-gradient(90deg, #049149 0%, #5480a8 56%, #6d80ac 100%);
                border-bottom: 4px solid #f4d207;
                box-shadow: 0 10px 28px rgba(4, 145, 73, 0.20);
            }}

            .app-header-logo {{
                height: 56px;
                width: auto;
                object-fit: contain;
                display: block;
            }}

            .app-header-title {{
                color: #ffffff;
                font-size: 1.45rem;
                font-weight: 800;
                letter-spacing: -0.02em;
                line-height: 1.2;
                text-align: center;
                text-shadow: 0 2px 8px rgba(0, 0, 0, 0.18);
            }}

            .image-action-wrapper {{
                width: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 0.5rem;
                margin-bottom: 0.5rem;
                position: relative !important;
                z-index: 999999 !important;
                pointer-events: auto !important;
            }}

            .image-action-button {{
                width: 100%;
                max-width: 560px;
                display: block;
                border-radius: 999px;
                text-decoration: none !important;
                transition: all 0.28s ease;
                filter: drop-shadow(0 10px 18px rgba(4, 145, 73, 0.18));
                cursor: pointer !important;
                position: relative !important;
                z-index: 1000000 !important;
                pointer-events: auto !important;
            }}

            .image-action-button-submeter-dados {{
                max-width: 560px !important;
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
                cursor: pointer !important;
                pointer-events: auto !important;
                position: relative !important;
                z-index: 1000001 !important;
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
                cursor: pointer !important;
                position: relative !important;
                z-index: 1000000 !important;
                pointer-events: auto !important;
            }}

            .external-button-fallback:hover {{
                background: linear-gradient(135deg, #f4d207 0%, #65c463 100%);
                color: #17301f !important;
                transform: translateY(-2px);
                border-color: rgba(244, 210, 7, 0.65);
                text-decoration: none !important;
            }}

            .footer {{
                text-align: center;
                color: #5c6b73;
                font-size: 14px;
                padding: 10px;
            }}

            @media (max-width: 900px) {{
                .app-header {{
                    gap: 14px;
                    padding: 12px 18px;
                    margin-bottom: 1.7rem;
                }}

                .app-header-logo {{
                    height: 48px;
                }}

                .app-header-title {{
                    font-size: 1.08rem;
                }}

                .image-action-button {{
                    max-width: 460px;
                }}

                .image-action-button-sala-situacao {{
                    max-width: 300px !important;
                }}
            }}

            @media (max-width: 520px) {{
                .app-header {{
                    flex-direction: column;
                    gap: 8px;
                    padding: 14px;
                }}

                .app-header-logo {{
                    height: 46px;
                }}

                .app-header-title {{
                    font-size: 1rem;
                }}

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


# ============================================================
# COMPONENTES
# ============================================================

def render_header() -> None:
    """
    Renderiza cabeçalho sem botões de navegação.
    Apenas logo e título institucional.
    """

    logo_path = get_header_logo_path()

    if logo_path:
        logo_base64 = file_to_base64(logo_path)
        logo_mime = get_image_mime_type(logo_path)

        logo_html = (
            f'<img class="app-header-logo" '
            f'src="data:{logo_mime};base64,{logo_base64}" '
            f'alt="Logo GT6">'
        )
    else:
        logo_html = ""

    st.markdown(
        f"""
        <div class="app-header">
            {logo_html}
            <div class="app-header-title">
                Sistema de Saúde Alimentar e Nutricional - GT6
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_external_image_button(
    image_path: Path | None,
    external_url: str,
    fallback_label: str,
    css_suffix: str,
) -> None:
    """
    Renderiza um botão baseado em imagem apontando para sistema externo.
    """
    safe_url = external_url.strip()

    if image_path and image_path.exists():
        image_base64 = file_to_base64(image_path)
        image_mime = get_image_mime_type(image_path)

        st.markdown(
            f"""
            <div class="image-action-wrapper">
                <a
                    class="image-action-button image-action-button-{css_suffix}"
                    href="{safe_url}"
                    target="_blank"
                    rel="noopener noreferrer"
                    title="{fallback_label}"
                    onclick="window.open('{safe_url}', '_blank', 'noopener,noreferrer'); return false;"
                >
                    <img
                        src="data:{image_mime};base64,{image_base64}"
                        alt="{fallback_label}"
                    >
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
                    href="{safe_url}"
                    target="_blank"
                    rel="noopener noreferrer"
                    title="{fallback_label}"
                    onclick="window.open('{safe_url}', '_blank', 'noopener,noreferrer'); return false;"
                >
                    {fallback_label}
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )


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
# PÁGINA PRINCIPAL
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


# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================

def main() -> None:
    load_css()
    apply_global_styles()
    render_header()
    render_home()
    render_footer()


if __name__ == "__main__":
    main()