const fetch = require('node-fetch');

module.exports = async (req, res) => {
  const { ticker } = req.query;
  const apiKey = process.env.EODHD_API_KEY;
  const url = `https://eodhd.com/api/fundamentals/${ticker}.US?api_token=${apiKey}&fmt=json`;

  try {
    const response = await fetch(url);
    const text = await response.text();

    try {
      const data = JSON.parse(text);
      res.status(200).json(data);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
      res.status(500).json({ error: 'Invalid JSON response' });
    }
  } catch (error) {
    console.error('Error fetching data:', error);
    res.status(500).json({ error: 'An error occurred' });
  }
};