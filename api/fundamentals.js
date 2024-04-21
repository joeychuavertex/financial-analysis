const fetch = require('node-fetch');

module.exports = async (req, res) => {
  const { ticker } = req.query;
  const url = `https://eodhd.com/api/fundamentals/${ticker}.US?api_token=demo&fmt=json`;

  try {
    const response = await fetch(url);
    const data = await response.json();
    res.status(200).json(data);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'An error occurred' });
  }
};