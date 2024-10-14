describe("Teste de criação, login e delete", () => {
	it("teste delete de usuario com sucesso", () => {
		// Create user
		goToPage()
		cy.get('.btn-link').click()
		cy.get('#firstName').type("User1")
		cy.get('#Text1').type("User1")
		cy.get('#username').type("User1")
		cy.get('#password').type("securePassword")
		cy.get('.btn-primary').click()
		cy.get('.ng-binding').should("contain.text", "Registration successful")

		// Login
		goToPage()
		cy.get('#username').type("User1")
		cy.get('#password').type("securePassword")
		cy.get('.btn-primary').click()
		cy.get('h1.ng-binding').should("contains.text", "User1")

		// Delete user
        cy.get('.ng-binding > a').click()
        cy.get('.btn').click()
        cy.get('h2').should("contain.text", "Login")

		// Login (failed)
		cy.get('#username').type("User1")
		cy.get('#password').type("securePassword")
		cy.get('.btn-primary').click()
        cy.get('.ng-binding').should("contain.text", "password is incorrect")
	})
})

function goToPage() {
	cy.visit('https://www.globalsqa.com/angularJs-protractor/registration-login-example/#/login')
}
