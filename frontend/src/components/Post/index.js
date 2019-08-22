import React from 'react';
import './Post.css';

class Post extends React.Component {
    render() {
        return ( 
            <div className="Post">
                {this.props.text}
                {this.props.photos.map((photo, index) => <img key={index} src={photo} />)}
            </div> 
        );
    };
}

export default Post;