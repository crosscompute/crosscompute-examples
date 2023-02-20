<div id="q" class="side"></div>

<div id="a" class="side"></div>

{ cards }

<script src="https://cdn.jsdelivr.net/npm/showdown"></script>

<script>
const q = document.getElementById('q'), a = document.getElementById('a'), delayInMilliseconds = 2000, c = new showdown.Converter(), getRandomIndex = count => Math.floor(Math.random() * count);

async function showCards() {
  const { cards } = variables;
  if (cards && cards.length) {
    const cardIndex = getRandomIndex(cards.length), card = cards[cardIndex], sideIndex = getRandomIndex(2);
    if (sideIndex == 0) {
        q.innerHTML = c.makeHtml(card[0]);
        await sleep(delayInMilliseconds);
        a.innerHTML = c.makeHtml(card[1]);
    } else {
        a.innerHTML = c.makeHtml(card[1]);
        await sleep(delayInMilliseconds);
        q.innerHTML = c.makeHtml(card[0]);
    }
    await sleep(delayInMilliseconds);
    q.innerHTML = '';
    a.innerHTML = '';
  }
  setTimeout(showCards, delayInMilliseconds);
}

setTimeout(showCards, delayInMilliseconds);
</script>
