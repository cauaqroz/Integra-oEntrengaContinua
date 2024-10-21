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
