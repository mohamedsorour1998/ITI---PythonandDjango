const fetch = require('node-fetch');

async function fetchPosts() {
  try {
    const response = await fetch("http://127.0.0.1:8000/myblog/api/post?format=json");
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

fetchPosts();
