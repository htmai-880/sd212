import { createRequire } from 'module'
const require = createRequire(import.meta.url)
const malScraper = require('mal-scraper');

malScraper.getRecommendationsList({
    id: 45613
  })
    .then((data) => console.log(data))
    .catch((err) => console.log(err))

// Idea:
// Adjacency: Recommendations
// Labels: Genres
// Names: anime names
// https://scikit-network.readthedocs.io/en/latest/use_cases/recommendation.html
// https://github.com/Kylart/MalScraper/blob/master/README.md