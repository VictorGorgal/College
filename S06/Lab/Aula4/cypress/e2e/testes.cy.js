describe("Teste wikipeadia", () => {
	it("Teste pesquisar uma pagina", () => {
		goToJavaPage()
		cy.get('.mw-page-title-main').should("contain.text", "Java (programming language)")
	})
	
	it("Teste pesquisar uma pagina inexistente", () => {
		goToPage()

		cy.get('#searchInput').type("adsjahsdjahsdjhasdjkhasd")
		cy.get('.pure-button').click()
		cy.get('.mw-search-nonefound').should("contain.text", "There were no results matching the query.")
	})
	
	it("Teste trocar linguagem da pagina", () => {
		goToJavaPage()

		cy.get('#p-lang-btn-checkbox').click()
		cy.get('.uls-languagefilter').type("portugues")
		cy.get('[data-region="all"] > .row > .three > .interlanguage-link > .autonym').click()
		cy.get('.mw-page-title-main').should("contain.text", "Java (linguagem de programação)")
	})
	
	it("Teste de hyperlinks", () => {
		goToJavaPage()

		cy.get(':nth-child(11) > [href="/wiki/Java_virtual_machine"]').click()
		cy.get('.mw-page-title-main').should("contain.text", "Java virtual machine")
	})
	
	it("Teste de login com falha", () => {
		goToJavaPage()
		
		cy.get('#pt-login-2 > a > span').click()
		cy.get('#wpName1').type("UserNotCreated")
		cy.get('#wpPassword1').type("UserNotCreated")
		cy.get('#wpLoginAttempt').click()
		cy.get('.cdx-message__content').should(($el) => {
			const text = $el.text().trim();
			expect(
			  text.includes("Incorrect username or password entered.\nPlease try again.") ||
			  text.includes("There are problems with some of your input.")
			).to.be.true;
		});
	})
	
	it("Teste de criar conta com falha - senha fraca", () => {
		goToJavaPage()
		
		cy.get('#pt-createaccount-2 > a > span').click()
		cy.get('#wpName2').type("SomeUsername")
		cy.get('#wpPassword2').type("123")
		cy.get('#wpRetype').type("123")
		cy.get('#wpCreateaccount').click()

		cy.get('.cdx-message__content > ul > :nth-child(1)').should("contain.text", "Passwords must be at least 8 characters.")
		cy.get('.cdx-message__content > ul > :nth-child(2)').should("contain.text", "The password entered is in a list of very commonly used passwords. Please choose a more unique password.")
	})
})

function goToPage() {
	cy.visit('https://www.wikipedia.org')
}

function goToJavaPage() {
	goToPage()
	cy.get('#searchInput').type("Java")
	cy.get('[href="https://en.wikipedia.org/wiki/Java_(programming_language)"]').click()
}
