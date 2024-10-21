## O que é automação de testes?
> Automação de testes é a prática de utilizar software para executar testes em aplicações de software. Ao invés de realizar manualmente cada teste, a automação permite criar scripts que interagem com a aplicação, simulando ações do usuário e verificando os resultados.

## Principais benefícios de realizar testes automatizados

> Eficiência: Redução do tempo necessário para a execução de testes.

> Consistência: Execução repetitiva e precisa de testes.

> Cobertura: Aumento da cobertura de testes, garantindo que mais partes do código sejam verificadas.

> Custo-benefício: Redução dos custos a longo prazo com a detecção precoce de bugs.

## Diferença entre testes unitários, de integração e end-to-end (E2E)

> Testes Unitários: Verificam individualmente cada componente ou unidade do código, garantindo que funcionem corretamente isoladamente.

> Testes de Integração: Avaliam a interação entre diferentes componentes ou unidades, garantindo que funcionem bem juntos.

> Testes End-to-End (E2E): Verificam o funcionamento da aplicação como um todo, do início ao fim, simulando o comportamento do usuário.

## Ferramentas de Teste para Automação de Aplicações Web

### 1. Selenium:

> Selenium é uma das ferramentas mais populares para automação de testes de comportamento. É amplamente utilizada para realizar testes end-to-end (E2E) em aplicações web. Com Selenium, é possível automatizar a interação com o navegador, permitindo a execução de testes que simulam a experiência do usuário real.

> ### Uso no Projeto de Leilão: 
> No contexto do projeto de leilão, Selenium foi usado para verificar as funcionalidades da aplicação. Por exemplo, ao inserir um valor de lance menor que o mínimo, Selenium foi usado para automatizar a inserção do valor, clicar no botão "Enviar Lance" e verificar se a mensagem de erro é exibida corretamente. Da mesma forma, pode validar se um lance válido exibe a mensagem de sucesso esperada.

>### Uso do Selenium
>Para usar o selenium olhe o arquivo `TesteSelenium.py` apos abrir o codigo para testes, você precisara configurar o Selenium em seu ambiente. Isso inclui instalar o WebDriver correspondente ao navegador que você usará para os testes (por exemplo, ChromeDriver para Google Chrome).

> agora configure os testes que serão feitos na sua aplicação e inicie o arquivo com os testes que você deseja realizar

### 2. Cypress:

> Cypress é uma ferramenta moderna e robusta voltada para testes de interface (UI) de aplicações web. Ela facilita a criação de testes end-to-end, oferecendo uma experiência de desenvolvimento integrada e amigável. Cypress se destaca por sua capacidade de executar testes em tempo real e fornecer um feedback rápido e detalhado.

> ### Uso no Projeto de Leilão
> No projeto de leilão, Cypress pode ser usado para testar as mesmas funcionalidades que Selenium. A ferramenta automatiza a interação com os elementos da página, como o campo de entrada de lance e o botão de envio. Cypress verifica se a mensagem de erro aparece ao inserir um valor menor que o lance mínimo e se a mensagem de sucesso aparece ao inserir um valor válido.

> ### Uso do Cypress
> Para uso do Cypress instale o proprio com `npm install cypress --save-dev` e `npx cypress open`, após isso configure o seu arquivo javascript para incluir os testes automatizados do cypress que podemos observar com o uso da tag `cy`:

```Javascript

describe('Leilão de Produto', () => {
    it('Deve exibir mensagem de erro para lance menor que o mínimo', () => {
        cy.visit('caminho-para-o-seu-projeto');
        cy.get('#bidValue').type('50');
        cy.contains('Enviar Lance').click();
        cy.get('#message').should('have.class', 'error')
                          .and('contain', 'O valor do lance deve ser no mínimo R$ 100,00.');
    });

    it('Deve aceitar lance igual ou maior que o mínimo', () => {
        cy.visit('caminho-para-o-seu-projeto');
        cy.get('#bidValue').type('150');
        cy.contains('Enviar Lance').click();
        cy.get('#message').should('have.class', 'success')
                          .and('contain', 'Lance de R$ 150 aceito com sucesso!');
    });
});

``` 
>Dessa forma os testes com o cypress ficam automatizados na aplicação 
