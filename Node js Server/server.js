const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const axios = require('axios'); 

const app = express();
app.use(express.json());

const fastapiUrl = 'http://localhost:8000';

const options = {
  target: fastapiUrl,
  changeOrigin: true,
  ws: true, 
};
const fastapiProxy = createProxyMiddleware(options);

app.use('/api', fastapiProxy);
app.post('/add-instructor', async (req, res) => {
  try {
    const response = await axios.post(`${fastapiUrl}/add-instructor`, req.body);
    res.json(response.data);
  } catch (error) {
    console.error('Error:', error.response.data);
    res.status(error.response.status).json({ error: error.response.data });
  }
});

app.post('/add-course', async (req, res) => {
  try {
    const response = await axios.post(`${fastapiUrl}/add-course`, req.body);
    res.json(response.data); 
  } catch (error) {

    console.error('Error:', error.response.data);
    res.status(error.response.status).json({ error: error.response.data });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Express server is listening on port ${PORT}`);
});
