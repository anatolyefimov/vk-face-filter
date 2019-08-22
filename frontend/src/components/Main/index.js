import React from 'react'
import './Main.css'
import Post from '@/components/Post'
import fetchPosts from '@/api/fetchPosts';

class Main extends React.Component {
    constructor(props) {
        super(props)

        // fetchPosts().then(
        //     (posts) => {
        //         this.state.posts = posts
        //     }
        // );
        
        this.state = {
            posts: []
        }
    }

    async componentDidMount() {
        let res = await fetch("http://localhost:5000");
        res = await res.json()

        this.setState({
            posts: res
        })
    }

    render() {
        const posts = this.state.posts.map((post, index) =>  <Post key={index} text={post.text} photos={post.photos} /> )
        
        return (
            <div className="Main">
                { posts}
            </div>
        );
    }
}

export default Main;