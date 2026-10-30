
import streamlit as st
import pandas as pd
import plotly.express as px

# CONFIGURACAO DA PAGINA
st.set_page_config(
    page_title="FinAI",
    page_icon="💳",
    layout="wide"
)

# ESTILO
st.markdown("""
<style>
.stApp {
    background-color: #F4F6FA;
}

[data-testid="stSidebar"] {
    background-color: #14213D;
}

[data-testid="stSidebar"] * {
    color: white;
}

.metric-card {
    background: white;
    padding: 22px;
    border-radius: 12px;
    border: 1px solid #E5E7EB;
}

.metric-label {
    color: #64748B;
    font-size: 14px;
}

.metric-value {
    color: #14213D;
    font-size: 27px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# DADOS FICTICIOS PARA TESTE
dados = {
    "descricao": [
        "Salario",
        "Supermercado",
        "Academia",
        "Restaurante",
        "Internet",
        "Freelance"
    ],
    "categoria": [
        "Receita",
        "Alimentacao",
        "Saude",
        "Alimentacao",
        "Moradia",
        "Receita"
    ],
    "tipo": [
        "Receita",
        "Despesa",
        "Despesa",
        "Despesa",
        "Despesa",
        "Receita"
    ],
    "valor": [
        3000,
        250,
        100,
        90,
        120,
        500
    ]
}

df = pd.DataFrame(dados)


# MENU LATERAL
with st.sidebar:

    st.title("💳 FinAI")
    st.caption("FINANCIAL INTELLIGENCE")

    st.divider()

    pagina = st.radio(
        "MENU",
        [
            "Dashboard",
            "Transacoes",
            "Assistente IA"
        ]
    )


# CALCULOS
receitas = df[df["tipo"] == "Receita"]["valor"].sum()

despesas = df[df["tipo"] == "Despesa"]["valor"].sum()

saldo = receitas - despesas


# DASHBOARD
if pagina == "Dashboard":

    st.title("Visao geral")
    st.caption("Acompanhe sua vida financeira.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Saldo</div>
            <div class="metric-value">
                R$ {saldo:,.2f}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Receitas</div>
            <div class="metric-value">
                R$ {receitas:,.2f}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Despesas</div>
            <div class="metric-value">
                R$ {despesas:,.2f}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    col4, col5 = st.columns(2)

    with col4:

        st.subheader("Despesas por categoria")

        gastos = df[df["tipo"] == "Despesa"]

        gastos = gastos.groupby(
            "categoria"
        )["valor"].sum().reset_index()

        fig = px.pie(
            gastos,
            names="categoria",
            values="valor",
            hole=0.6
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col5:

        st.subheader("Receitas x Despesas")

        comparacao = pd.DataFrame({
            "Tipo": ["Receitas", "Despesas"],
            "Valor": [receitas, despesas]
        })

        fig = px.bar(
            comparacao,
            x="Tipo",
            y="Valor",
            color="Tipo",
            text_auto=True
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.subheader("Ultimas transacoes")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# TRANSACOES
elif pagina == "Transacoes":

    st.title("Transacoes financeiras")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "Na proxima etapa vamos permitir "
        "cadastrar e armazenar transacoes."
    )


# ASSISTENTE IA
elif pagina == "Assistente IA":

    st.title("Assistente FinAI")

    st.write(
        "Converse com seu assistente financeiro."
    )

    st.info(
        "O agente de inteligencia artificial "
        "sera integrado em uma proxima etapa."
    )

    pergunta = st.chat_input(
        "Ex.: Quanto gastei com alimentacao?"
    )

    if pergunta:
        st.chat_message("user").write(pergunta)

        st.chat_message("assistant").write(
            "Estou sendo desenvolvido! "
            "Em breve poderei analisar seus dados financeiros."
        )
