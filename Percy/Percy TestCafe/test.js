import percySnapshot from '@percy/testcafe';
import { Selector } from 'testcafe';

// fixture('TestCafe example page').page(
//   'https://devexpress.github.io/testcafe/example/'
// );

// test("Should submit developer's name successfully", async user => {
//   // To interact with a DOM element, we must use the Selector function
//   const interfaceSelect = Selector('#preferred-interface');
//   const interfaceOption = interfaceSelect.find('option');

//   await user
//     .typeText('#developer-name', 'Sourav')
//     .click('#remote-testing')
//     .click(interfaceSelect)
//     .click(interfaceOption.withText('Both'))
//     .expect(interfaceSelect.value)
//     .eql('Both')
//     await percySnapshot(t, 'TestCafe Example')
//     .click('#submit-button')
//     .expect(Selector('#article-header').innerText)
//     .eql('Thank you, Sourav!');
// });


fixture('TestCafe example page').page(
  `https://devexpress.github.io/testcafe/example`
);

test('My first test', async t => {
    await t
        .typeText('#developer-name', 'Sourav')
        .click('#submit-button')
        .expect(Selector('#article-header').innerText)
        .eql('Thank you, Sourav!');
    
    await percySnapshot(t, 'TestCafe Example');
});