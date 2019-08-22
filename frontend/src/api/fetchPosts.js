async function fetchPosts() {
    let res = await fetch("http://localhost:5000");
    res = await res.json()
    
    return res;
}

export default fetchPosts;