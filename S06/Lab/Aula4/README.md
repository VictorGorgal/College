# Projeto de Testes com Cypress

Este diretório contém a tarefa da lista 1.
Devido ao fato de que o repositório inclui materiais de outras disciplinas, recomendo fazer o download apenas da pasta da tarefa.

## Instalação do Projeto

### Opção 1: Baixar apenas a pasta da tarefa

1. Acesse [download-directory.github.io](https://download-directory.github.io/).
2. Cole o link da pasta específica da tarefa no GitHub:  
   `https://github.com/VictorGorgal/College/tree/main/S06/Lab/Aula4`.
3. Clique em “Download” para baixar apenas a pasta como um arquivo ZIP.
4. Extraia o conteúdo da pasta ZIP em seu computador.

### Opção 2: Clonar o Repositório Completo

Caso prefira, você também pode clonar o repositório completo:

```bash
git clone https://github.com/VictorGorgal/College.git
```

Depois, navegue até a pasta da tarefa:

```bash
cd ./College/S06/Lab/Aula4
```

## Dependências

```bash
npm install cypress --save-dev
npm install cypress-mochawesome-reporter --save-dev
```

## Executando os Testes

Para rodar os testes com o Cypress:

```bash
npx cypress run --browser chrome
```

## Visualizando o Relatório

Após rodar os testes, você pode visualizar o relatório:

1. Vá até a pasta `./cypress/reports`.
2. Abra o arquivo `index.html` em seu navegador para visualizar o relatório detalhado dos testes.

