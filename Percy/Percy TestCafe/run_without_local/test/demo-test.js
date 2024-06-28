import percySnapshot from '@percy/testcafe';
import { Selector } from 'testcafe';

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