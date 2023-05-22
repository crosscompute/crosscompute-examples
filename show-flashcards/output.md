<div id="q" class="side"></div>

<div id="a" class="side"></div>

{ cards }

<script src="https://cdnjs.cloudflare.com/ajax/libs/showdown/2.1.0/showdown.min.js"></script>

<script>
const q = document.getElementById('q'), a = document.getElementById('a'), c = new showdown.Converter(), getRandomIndex = count => Math.floor(Math.random() * count);

async function showCards() {
  const { cards } = variables;
  if (cards && cards.length) {
    const cardIndex = getRandomIndex(cards.length), card = cards[cardIndex], sideIndex = getRandomIndex(2);
    if (sideIndex == 0) {
        q.innerHTML = c.makeHtml(card[0]);
        await sleep(2000);
        a.innerHTML = c.makeHtml(card[1]);
    } else {
        a.innerHTML = c.makeHtml(card[1]);
        await sleep(2000);
        q.innerHTML = c.makeHtml(card[0]);
    }
    await sleep(2000);
    q.innerHTML = '';
    a.innerHTML = '';
  }
}

let refreshInterval;
registerCallback('cards', function() {
  clearInterval(refreshInterval);
  refreshInterval = setInterval(showCards, 6000);
});
</script>
