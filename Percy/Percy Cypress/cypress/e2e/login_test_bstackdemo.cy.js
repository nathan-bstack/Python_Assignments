import '@percy/cypress';
describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://bstackdemo.com/');
    
    // Sign in
    cy.get('#signin').click();
    cy.get('#username > div > div.css-1wy0on6 > div').type('demouser');
    cy.get('#react-select-2-option-0-0').click()
    cy.get('#password > div > div.css-1wy0on6 > div').type('testingisfun99{enter}').click();
    cy.get('#react-select-3-option-0-0').click()
    cy.percySnapshot('Signin test', { widths: [768, 992, 1200] });
    // Add iPhone 12 to cart
    cy.wait(2000); // Wait for login to complete (adjust timing as needed)
    cy.get('#login-btn').click(); // Assuming this selector represents the iPhone 12
    cy.get('#confirmation-message').should('have.text', 'Your Order has been successfully placed.')

  });
});
  