import streamlit as st

st.title("Este é o título do app")
st.header("Este é o subtítulo")
st.subheader("Este é o terceiro subtítulo")
#st.markdown("Este é texto"): Permite inserir textos em Markdown. É ideal para formatação de texto, como negrito, itálico, listas, links, etc.
st.markdown("Este é texto")
#st.caption("Esta é a legenda"): Exibe uma legenda, que é uma anotação em um estilo menor e mais discreto, frequentemente usada para descrever gráficos ou imagens.
st.caption("Esta é a a legenda")
#Exibe o código formatado, com estilo de destaque, bom para mostrar trechos de código ou pseudocódigo.
st.code("x=2021")
#Renderiza expressões matemáticas usando sintaxe LaTeX, ideal para mostrar fórmulas complexas de forma legível.
st.latex(r''' a+a r^1+a r^2+a r^3 ''')