# AgroEnsaios IA — Landing pública

Apresentação institucional e acadêmica da plataforma **AgroEnsaios IA**, construída em Python e Streamlit.

Esta versão pública é exclusivamente informativa. Não carrega bancos de dados, não executa auditoria, não realiza predições e não treina modelos.

## Arquivos

- `streamlit_app.py`: arquivo principal da aplicação.
- `landing_page.py`: estrutura e textos da página.
- `landing_styles.css`: identidade visual.
- `.streamlit/config.toml`: tema da aplicação.
- `requirements.txt`: dependência necessária.

## Executar localmente

```powershell
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

## Publicar no Streamlit Community Cloud

1. Crie um repositório no GitHub e envie **somente os arquivos deste pacote** para a raiz do repositório, preservando a pasta `.streamlit`.
2. Entre em https://share.streamlit.io/ e selecione **Create app**.
3. Escolha o repositório, a branch `main` e o arquivo principal `streamlit_app.py`.
4. Se necessário, selecione Python **3.12** em **Advanced settings**.
5. Clique em **Deploy** e compartilhe a URL gerada.

**Nota:** Ao publicar, revise se os nomes dos integrantes e os indicadores históricos podem ser exibidos publicamente. Não envie as pastas `02_dados`, `04_resultados`, `07_codigo` nem documentos internos do projeto científico. Não compartilhe senhas ou credenciais.

## Relação com o projeto local

A plataforma científica completa continua no computador de desenvolvimento. Mudanças no repositório público não alteram a base local e a página pública não se conecta automaticamente a ela.
